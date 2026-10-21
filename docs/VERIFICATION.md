# Verification record — 21 October 2026

## Scope

The new `projects/readability_demo` and `projects/bike_demand` examples were executed in an isolated Linux Python 3.13.13 environment. Seven standard-library unit tests passed. Both analysis scripts ran successfully, produced the committed results, and the two bike-demand charts were rendered and visually inspected. Dependency versions are recorded in `requirements-lock.txt`. A fresh installation from the pinned requirements passed `pip check`; all eight committed result files reproduced byte-for-byte. An interrupted temporary environment installation was discarded and recreated before the final verification.

The bike pipeline checks 731 rows, exact dates, source SHA-256, SQL constraints and reconciliation with independent Python aggregation. Its reported totals and percentages come from the executed SQL queries. No paid APIs, credentials or private data are used. The included UCI daily dataset is attributed under CC BY 4.0.

The readability example uses original synthetic, AI-assisted text and one tokenizer across metrics. Its syllable estimator is approximate; software tests are not linguistic validation.

## Boundaries

Historical notebooks remain unchanged and were not re-executed as a complete collection. Their source/licensing questions are not resolved by the new companion example. The root requirements files intentionally cover only the new demonstrations.

The selected-work pages retain their original source snapshots and original evidence limits. No client outcomes, expert linguistic ratings or model benchmark results were created.

The local connected computer's execution service and Chrome transport became unavailable during this task. Public source files were subsequently retrieved and tested in an isolated remote sandbox using the available Composio execution tool; publication used the authorized GitHub connector. No browser actions or LinkedIn edits were completed.

The workflow file runs only public-repository software/data checks with read-only repository permissions and no secrets. A committed workflow is not by itself evidence of a successful GitHub Actions run; check the Actions tab for the current run status.
