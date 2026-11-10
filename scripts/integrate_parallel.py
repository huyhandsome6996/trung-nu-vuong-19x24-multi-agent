#!/usr/bin/env python3
"""Coordinator only: accept a completed lane into the global queue after evidence checks."""
import argparse
import copy
import hashlib
import json
import workflow as w
import parallel_workflow as p


def integrate(lane):
    state = p.check_lane(lane)
    owned = p.owned_tasks(lane)
    tasks = [t for t in state['tasks'] if t['id'] in owned]
    if any(t['status'] != 'done' for t in tasks):
        raise ValueError('Complete all owned page steps before coordinator integration')
    global_state = w.read(p.GLOBAL_STATE)
    for source in tasks:
        target = w.task_by_id(global_state, source['id'])
        if target.get('evidence') and target['evidence'] != source['evidence']:
            source = copy.deepcopy(source)
            source.setdefault('previous_evidence', []).append(target['evidence'])
        target.update(copy.deepcopy(source))
    errors = w.check(global_state)
    if errors:
        raise ValueError('\n'.join(errors))
    path = p.ROOT / p.state_path(lane)
    record = {'lane': lane, 'at': w.now(), 'source_state_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
              'accepted_tasks': sorted(owned), 'user_approved': False, 'print_ready': False}
    folder = p.ROOT / '10_agent_workflow/parallel/coordinator'
    folder.mkdir(exist_ok=True)
    version = 1
    while (folder / f'{lane}.integration.v{version:03d}.json').exists():
        version += 1
    w.write(f'10_agent_workflow/parallel/coordinator/{lane}.integration.v{version:03d}.json', record)
    global_state['history'].append({'at': w.now(), 'task': lane, 'action': 'integrate',
                                    'note': 'Coordinator verified and accepted scoped evidence; no user/print approval'})
    w.write(p.GLOBAL_STATE, global_state)
    print('Accepted ' + lane + ': ' + str(len(owned)) + ' verified tasks')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lane', choices=['agent_a', 'agent_b'], required=True)
    integrate(parser.parse_args().lane)
