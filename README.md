# Gutemberg Rapôso — Data, Language & NLP

![Currently Learning](https://img.shields.io/badge/%F0%9F%94%AC%20Currently%20Learning-Python%20Logging%20%26%20Debugging%20for%20DS-blue)

🔬 Currently Learning: Python Logging & Debugging for DS

**Junior → Senior Data Scientist | Open to Remote Opportunities**

Learning path — a long-term development goal, not a claim of current seniority.

### Unique background: Linguística + Data Science + NLP aplicado à educação

- **Linguística:** sociolinguistics, register variation and language-teaching experience shape how I clean, tokenize and interpret text.
- **Data Science:** Python, pandas, NumPy, visualization, automated testing with pytest (Day 10), decorators and context managers (Day 11), `itertools`/`functools` for lazy, memory-efficient pipelines (Day 12) the `typing` module and type hints (Day 13), concurrency with `threading`, `multiprocessing`, `concurrent.futures` and `joblib` for parallel data pipelines (Day 14) reproducible environments with `venv`, `pip`/`pip-tools`, `conda`, `uv` and `pyproject.toml` (Day 15) and — as of Day 16 — logging and debugging for data pipelines (named loggers, JSON logs, `RotatingFileHandler`, `warnings`, `logger.exception()`).
- **NLP aplicado à educação:** text-difficulty profiling, vocabulary-level heuristics and feedback tools for English learners.

I am an English teacher and language researcher in Brazil, building practical skills in data analysis and natural language processing. I am a doctoral student at the Federal University of Tocantins (UFT) and completed my master's degree in Letras (language and literature studies) in December 2025.

I am interested in international remote opportunities in entry-level data analysis/data science, language-focused AI projects, and Portuguese–English linguistic services. This repository shows my learning process and selected demonstrations; it does not represent senior-level or production-validated experience.

## Start with these three demonstrations

| Sample | What you can inspect | Evidence and limits |
| --- | --- | --- |
| [English text readability](portfolio_showcase/01_data_science.md) | Python text analysis, reusable components and interpretation | Educational prototype; the case study audits saved notebook outputs, not a new benchmark. |
| [Tino: context-aware NLP](portfolio_showcase/02_tino_nlp.md) | Register-sensitive feedback, sociolinguistic reasoning and a FastAPI application | LLM-backed prototype; no measured model accuracy or educational efficacy is claimed. |
| [Academic editing & PT–EN translation](portfolio_showcase/03_academic_editing_pt_en.md) | Before/after editing, translation and explained terminology choices | Original fictional, AI-assisted demonstration, not client work or proof of unaided performance. |

[Browse all selected work](portfolio_showcase/) · [Tino source](https://github.com/Gutembergfox/tino) · [Tradutor Pro workflow](https://github.com/Gutembergfox/tradutor-pro)

## Reproducible technical demonstrations

- [Bike demand — SQL + Python + visualization](projects/bike_demand/): an executed analysis of 731 daily observations from a public CC BY 4.0 dataset, with a planning question, SQL queries, charts, quality checks and explicit limits.
- [English readability companion](projects/readability_demo/): an offline example using original synthetic passages and consistent tokenization, with no third-party literary excerpts.

From this repository's root, use Python 3.13 and `python -m pip install -r requirements.txt`, then `python -m unittest discover -s tests -v`. Each project documents its execution command. The pinned dependencies cover these new demonstrations; they do not certify all historical notebooks. See [verification details](docs/VERIFICATION.md).

## Background and direction

My background in language teaching and sociolinguistics informs my interest in text analysis, register variation, language-data quality and clear academic communication. I am developing Python, pandas, NumPy and visualization skills through the exercises here. Technical proficiency should be assessed from the code and reproducible evidence, not inferred from a list of tools or AI-assisted output.

For PT/EN language work, the portfolio includes an academic editing and translation sample with explicit scope and limitations. I welcome conversations about remote research support, language-focused AI evaluation and appropriately scoped data projects.

## Study progress

| Phase | Folder | Days completed | Status |
| --- | --- | --- | --- |
| 1 — Python basics | [01_python_basics](01_python_basics/) | **16 / 28** | 🟢 In progress |
| 2 — Exploratory data analysis | [02_eda](02_eda/) | 0 / 28 | ⚪ Planned |
| 3 — Statistics | [03_statistics](03_statistics/) | 0 / 28 | ⚪ Planned |
| 4 — Machine learning | [04_machine_learning](04_machine_learning/) | 0 / 42 | ⚪ Planned |
| 5 — Advanced ML | [05_advanced_ml](05_advanced_ml/) | 0 / 42 | ⚪ Planned |
| 6 — NLP & time series | [06_nlp_timeseries](06_nlp_timeseries/) | 0 / 42 | ⚪ Planned |
| 7 — Advanced projects | [07_advanced_projects](07_advanced_projects/) | 0 / 28 | ⚪ Planned |

### Five most recent notebooks

1. **Day 16** — [2026-10-29 — Python logging & debugging for DS](01_python_basics/2026-10-29_logging_debugging_ds.ipynb) (logger/handler/formatter architecture and log levels, named-logger hierarchy, a `DataPipelineLogger` for shape/dtypes/missing values on seaborn titanic, JSON Lines structured logging on tips with the logs parsed back into pandas, a `@log_execution` decorator on penguins cleaning functions, `logger.exception()` and fallback patterns, `warnings` filters and `captureWarnings`, `assert`-based data validation, a logged scikit-learn `StandardScaler` + `LogisticRegression` experiment on iris, a `RotatingFileHandler` with observed rotation, text-pipeline logging on 20 Newsgroups plus short-text/mojibake QA on illustrative learner sentences, and a reusable `setup_ds_logger()` template; timings are machine-dependent)
2. **Day 15** — [2026-10-28 — Python environment management for DS](01_python_basics/2026-10-28_environment_management.ipynb) (the dependency problem shown with real `importlib.metadata` dependency graphs, a real `venv` and `uv venv` created in a temporary folder and inspected, `pip`/`pip check`/`pip freeze` vs. `pip-tools`, `conda` and `environment.yml`, the `uv` project workflow and `uv.lock`, a `pyproject.toml` with extras vs. PEP 735 dependency groups parsed with `tomllib`, `.gitignore` and prod/dev splits, a verified lock plus an environment fingerprint stored with a scikit-learn wine experiment, a pandas tool-comparison table, and a commented `requirements.txt` for an educational NLP project; install/conda/uv-project commands are shown as dry-runs, not executed)
3. **Day 14** — [2026-10-27 — Python concurrency for DS: parallel pipelines](01_python_basics/2026-10-27_concurrency_parallel_pipelines.ipynb) (the GIL demonstrated with threads vs processes, `threading.Thread`/`Lock` and `ThreadPoolExecutor` for I/O-bound loading, `multiprocessing.Pool`/`ProcessPoolExecutor` for chunked feature engineering on seaborn titanic/penguins, `joblib.Parallel` + `delayed` for feature transforms and cross-validation on iris/wine/breast_cancer, a timed benchmark with `time.perf_counter`, parallel lexical-complexity profiling of the NLTK Brown Corpus by genre and 20 Newsgroups, and a parallel ETL across seven public datasets; timings are machine-dependent)
4. **Day 13** — [2026-10-26 — Python typing & type hints for DS](01_python_basics/2026-10-26_typing_type_hints_ds.ipynb) (basic annotations, built-in generics, `X | None`, PEP 695 `type` aliases and `class Pipeline[T]`, `NewType`, sklearn-style `Protocol`s, `TypedDict`, `Callable`, `Literal` + `assert_never`, typed dataclasses, runtime validation with `beartype`, a real `mypy` run; a typed lexical-profile pipeline on the NLTK Brown Corpus with CEFR-inspired frequency bands — a heuristic, not official CEFR levels; typed scikit-learn experiments on iris/wine and 20 Newsgroups)
5. **Day 12** — [2026-10-25 — itertools & functools — Efficient Data Pipelines](01_python_basics/2026-10-25_itertools_functools.ipynb) (infinite, finite and combinatorial iterators, `partial`, `reduce`, `lru_cache`, `total_ordering`; a lexical-profile pipeline on the NLTK Brown Corpus using frequency bands as a CEFR-inspired proxy — not official CEFR levels; functional pipelines on seaborn titanic/penguins and scikit-learn wine/diabetes; memory and speed comparisons with `sys.getsizeof` and `timeit`)

## Learning archive

The existing notebooks and directory structure are preserved. As of 29 October 2026, the archive contains sixteen Python-fundamentals notebooks and an additional `Módulo_2.ipynb`. The later phase directories contain placeholders, not completed advanced projects.

| Directory | Current status |
| --- | --- |
| [01_python_basics](01_python_basics/) | Sixteen learning notebooks: pandas, NumPy, visualization (Matplotlib/Seaborn, Plotly), functions, strings/regex, file I/O, OOP, datetime/pandas, pytest, decorators/context managers, itertools/functools, typing/type hints, concurrency/parallel pipelines, environment management (venv, pip, conda, uv, pyproject.toml), and logging & debugging for data science. |
| [Módulo_2.ipynb](Módulo_2.ipynb) | Additional historical notebook. |
| [02_eda](02_eda/), [03_statistics](03_statistics/) | Planned study phases; placeholders. |
| [04_machine_learning](04_machine_learning/), [05_advanced_ml](05_advanced_ml/) | Planned study phases; placeholders. |
| [06_nlp_timeseries](06_nlp_timeseries/), [07_advanced_projects](07_advanced_projects/) | Planned study phases; placeholders. |

The former 210-day schedule was a personal study plan, not a promise of progressing from junior to senior or a claim that the code was production-ready. The [original README is preserved as a dated historical record](docs/archive/README-2026-10-21.md).

The historical readability notebook includes literary excerpts whose provenance and reuse rights require further checking. Its outputs should not be treated as validated reading levels or learner outcomes. No license is granted here for third-party material.

## Reproducibility and transparency

The historical notebooks have not all been re-executed in a single verified environment. Their stored outputs are evidence of the saved exercises, not a guarantee that every notebook currently runs unchanged. See each demonstration for its sources, assumptions and validation gaps.

AI assistance was used to prepare the selected-work documentation and this presentation, with factual claims checked against the public repository and the background supplied by the author. AI-assisted artifacts do not establish independent professional experience or unaided skill.

## Contact

[LinkedIn — Gutemberg Rapôso](https://www.linkedin.com/in/gutemberg-raposo-a8aa1937b/) · [GitHub](https://github.com/Gutembergfox) · [gtmbrgfox@gmail.com](mailto:gtmbrgfox@gmail.com)

Based in Palmas-TO, Brazil; open to international remote opportunities.
