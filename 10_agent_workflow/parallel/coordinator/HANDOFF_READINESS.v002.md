# Handoff readiness —10Nov2026

Verified production base:18d65f4645fca3cbc123ba795a6314ce7ab92b73. User confirms external A/B not started; clone latest main for this handoff.

| Owner | Pages | Existing accepted steps | Initial next | Remaining |
| --- | --- | --- | --- | --- |
| agent_a |14–20|TEXT14–18|PAGE14_ART|23page steps|
| agent_b |21–28|none; SOURCE_EPILOGUE prerequisite verified|PAGE21_TEXT|32page steps|
| coordinator |01–13/covers/matter/assembly|PAGE04LAYOUTv003/PAGE12LAYOUTv003/PAGE13LAYOUTv002 illustrated lettering accepted by agent|PAGE06_LAYOUT|PAGE03blocked; other legacy speech and book production pending|

Current full prompts: agent_a/PROMPT.md, agent_b/PROMPT.md; immutable copies PROMPT.v002.md; old copies PROMPT.v001.md. File ownership remains assignments.json. Private state/logs and immutable shared source prevent ordinary text overlap; publish fetch/rebase/retry handles push races. It also rejects foreign unpublished commits even in a clean worktree. These are client workflow checks, not GitHub server ACLs. Agents must use the wrapper.

Validation:17unit/integration tests, including two real independent clones/local bare main, actual non-fast-forward retry, committed-foreign-path refusal, scope/global-state/deletion/dependency/evidence checks. check_repo and scoped queue checks required before publish. This report does not claim user approval or print readiness.
