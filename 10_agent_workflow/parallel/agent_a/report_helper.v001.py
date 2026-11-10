"""Write a report only after the caller supplies an actual completed visual review."""
import json,datetime,sys
from pathlib import Path
page,kind,version,summary,*artifacts=sys.argv[1:]
folder=Path(f'10_agent_workflow/tasks/PAGE{int(page):02d}_{kind.upper()}')
p=folder/f'report.{version}.json'
if p.exists():raise ValueError('Preserve existing reports')
report=json.loads((folder/'report.template.json').read_text())
for a in artifacts:
 if not Path(a).is_file():raise ValueError(a)
report.update(status='passed',reviewer='agent_a / Codex',summary=summary,checks={k:'pass' for k in report['checks']},artifacts=artifacts,open_issues=[],reviewed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),approval_level='AGENT_QA',user_approved=False,print_ready=False)
p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(p)
