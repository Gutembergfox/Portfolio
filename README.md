# Gutemberg Rapôso — Data, Language & NLP

![Currently Learning](https://img.shields.io/badge/%F0%9F%94%AC%20Currently%20Learning-Python%20Packaging%20%26%20DS%20Modules-blue)

🔬 Currently Learning: Python Packaging & DS Modules

**Junior → Senior Data Scientist | Open to Remote Opportunities**

Learning path — a long-term development goal, not a claim of current seniority.

### Unique background: Linguística + Data Science + NLP aplicado à educação

- **Linguística:** sociolinguistics, register variation and language-teaching experience shape how I clean, tokenize and interpret text.
- **Data Science:** Python, pandas, NumPy, visualization, automated testing with pytest (Day 10), decorators and context managers (Day 11), `itertools`/`functools` for lazy, memory-efficient pipelines (Day 12) the `typing` module and type hints (Day 13), concurrency with `threading`, `multiprocessing`, `concurrent.futures` and `joblib` for parallel data pipelines (Day 14) reproducible environments with `venv`, `pip`/`pip-tools`, `conda`, `uv` and `pyproject.toml` (Day 15) logging and debugging for data pipelines (Day 16), profiling and performance optimization (Day 17) and — as of Day 18, closing Phase 1 — Python packaging and reusable DS modules (`__init__.py`/`__all__`, `pyproject.toml` with `[project.scripts]`, `argparse` and Click CLIs, editable installs and wheels built with `python -m build`).
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
| 1 — Python basics | [01_python_basics](01_python_basics/) | **18 / 28** `▓▓▓▓▓▓░░░░` 64% | 🟢 In progress — Python-fundamentals block complete |
| 2 — Exploratory data analysis | [02_eda](02_eda/) | 0 / 28 | ⚪ Planned |
| 3 — Statistics | [03_statistics](03_statistics/) | 0 / 28 | ⚪ Planned |
| 4 — Machine learning | [04_machine_learning](04_machine_learning/) | 0 / 42 | ⚪ Planned |
| 5 — Advanced ML | [05_advanced_ml](05_advanced_ml/) | 0 / 42 | ⚪ Planned |
| 6 — NLP & time series | [06_nlp_timeseries](06_nlp_timeseries/) | 0 / 42 | ⚪ Planned |
| 7 — Advanced projects | [07_advanced_projects](07_advanced_projects/) | 0 / 28 | ⚪ Planned |

### Five most recent notebooks

1. **Day 18** — [2026-10-31 — Python packaging & reusable DS modules](01_python_basics/2026-10-31_python_packaging_ds_modules.ipynb) (closes Phase 1's Python-fundamentals block: packages, sub-packages, `__init__.py`, `__all__` and relative imports; an annotated `pyproject.toml` parsed with `tomllib`; a `src/`-layout `dskit` package with a cached seaborn `data_loader`, a leakage-safe fit/transform `preprocessor` and figure-returning `visualizer` applied to titanic, penguins and tips; the same CLI in `argparse` and Click with subcommands, JSON/CSV output and exit codes; 17 `pytest` tests, a real `pip install -e .` in a temporary venv with working console scripts, and an sdist/wheel built with `python -m build` and inspected; plus a pure-Python `nlp_edu` package — `word_frequency()`, Flesch/Flesch-Kincaid `readability_score()` and a heuristic, CEFR-inspired `cefr_classifier()` — applied to the NLTK Gutenberg corpus; the CEFR-like bands are not official CEFR levels)
2. **Day 17** — [2026-10-30 — Python profiling & performance optimization](01_python_basics/2026-10-30_profiling_performance_optimization.ipynb) (`timeit`, `cProfile` and `pstats` on a 20 Newsgroups word-frequency function, a didactic line profiler built on `sys.settrace`, `tracemalloc` snapshots of a bag-of-words pipeline, memory of text representations (dense vs sparse CSR), manual TF-IDF, cosine similarity and feature standardization as Python loops vs NumPy vs scipy/sklearn — each checked with `np.allclose`, string operations on seaborn titanic, pandas `apply`/`iterrows`/`itertuples` vs vectorized code, categoricals and `query()` on replicated seaborn tips/titanic, `dict`/`set`/`heapq` for NLP vocabularies, and a profiled `StandardScaler` → `PCA` → `SVC` pipeline on `load_digits`; timings are machine-dependent)
3. **Day 16** — [2026-10-29 — Python logging & debugging for DS](01_python_basics/2026-10-29_logging_debugging_ds.ipynb) (logger/handler/formatter architecture and log levels, named-logger hierarchy, a `DataPipelineLogger` for shape/dtypes/missing values on seaborn titanic, JSON Lines structured logging on tips with the logs parsed back into pandas, a `@log_execution` decorator on penguins cleaning functions, `logger.exception()` and fallback patterns, `warnings` filters and `captureWarnings`, `assert`-based data validation, a logged scikit-learn `StandardScaler` + `LogisticRegression` experiment on iris, a `RotatingFileHandler` with observed rotation, text-pipeline logging on 20 Newsgroups plus short-text/mojibake QA on illustrative learner sentences, and a reusable `setup_ds_logger()` template; timings are machine-dependent)
4. **Day 15** — [2026-10-28 — Python environment management for DS](01_python_basics/2026-10-28_environment_management.ipynb) (the dependency problem shown with real `importlib.metadata` dependency graphs, a real `venv` and `uv venv` created in a temporary folder and inspected, `pip`/`pip check`/`pip freeze` vs. `pip-tools`, `conda` and `environment.yml`, the `uv` project workflow and `uv.lock`, a `pyproject.toml` with extras vs. PEP 735 dependency groups parsed with `tomllib`, `.gitignore` and prod/dev splits, a verified lock plus an environment fingerprint stored with a scikit-learn wine experiment, a pandas tool-comparison table, and a commented `requirements.txt` for an educational NLP project; install/conda/uv-project commands are shown as dry-runs, not executed)
5. **Day 14** — [2026-10-27 — Python concurrency for DS: parallel pipelines](01_python_basics/2026-10-27_concurrency_parallel_pipelines.ipynb) (the GIL demonstrated with threads vs processes, `threading.Thread`/`Lock` and `ThreadPoolExecutor` for I/O-bound loading, `multiprocessing.Pool`/`ProcessPoolExecutor` for chunked feature engineering on seaborn titanic/penguins, `joblib.Parallel` + `delayed` for feature transforms and cross-validation on iris/wine/breast_cancer, a timed benchmark with `time.perf_counter`, parallel lexical-complexity profiling of the NLTK Brown Corpus by genre and 20 Newsgroups, and a parallel ETL across seven public datasets; timings are machine-dependent)

## Learning archive

The existing notebooks and directory structure are preserved. As of 31 October 2026, the archive contains eighteen Python-fundamentals notebooks and an additional `Módulo_2.ipynb`. The later phase directories contain placeholders, not completed advanced projects.

| Directory | Current status |
| --- | --- |
| [01_python_basics](01_python_basics/) | Eighteen learning notebooks: pandas, NumPy, visualization (Matplotlib/Seaborn, Plotly), functions, strings/regex, file I/O, OOP, datetime/pandas, pytest, decorators/context managers, itertools/functools, typing/type hints, concurrency/parallel pipelines, environment management (venv, pip, conda, uv, pyproject.toml), logging & debugging, profiling & performance optimization, and Python packaging & reusable DS modules (pyproject.toml, CLIs, wheels) for data science. |
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
