# Gutemberg Rapôso — Data, Language & NLP

![Currently Learning](https://img.shields.io/badge/%F0%9F%94%AC%20Currently%20Learning-EDA%20Fundamentals%20%E2%80%94%20Exploratory%20Data%20Analysis-blue)
![Phase 1](https://img.shields.io/badge/Phase%201-28%2F28%20complete-brightgreen)
![Phase 2](https://img.shields.io/badge/Phase%202-1%2F28%20in%20progress-orange)

🔬 Currently Learning: EDA Fundamentals — Exploratory Data Analysis

**Junior → Senior Data Scientist | Open to Remote Opportunities**

Learning path — a long-term development goal, not a claim of current seniority.

### Phase 2 started — Exploratory Data Analysis

🔄 **Day 29 / Phase 2, Day 1 (28 Nov 2026):** [EDA Fundamentals](02_eda/2026-11-28_eda-fundamentals.ipynb) opens the EDA phase with a complete exploratory pass over the public seaborn Titanic dataset (891 passengers × 15 columns): where EDA fits in CRISP-DM, initial inspection and redundancy checks, missing-value analysis with a discussion of MCAR/MAR/MNAR, univariate statistics (mean, median, mode, standard deviation, skewness, kurtosis, IQR outliers), Pearson vs Spearman correlations, survival by sex, class, age and family size, and advanced plots (pairplot, split violin plots, countplots with hue, faceted bar charts). The analysis is descriptive: associations are not yet tested formally and are not causal claims.

✅ **Phase 1 complete:** 28 / 28 days of Python Basics (4 Sep – 27 Nov 2026), closing with [GitHub Actions & CI/CD for Data Science](01_python_basics/2026-11-27_github_actions_ci_ds.ipynb).

### Unique Background: Linguistics + Data Science + NLP applied to Education

- **Linguística:** sociolinguistics, register variation and language-teaching experience shape how I clean, tokenize and interpret text.
- **Data Science:** Python, pandas, NumPy, visualization, automated testing with pytest (Day 10), decorators and context managers (Day 11), `itertools`/`functools` for lazy, memory-efficient pipelines (Day 12) the `typing` module and type hints (Day 13), concurrency with `threading`, `multiprocessing`, `concurrent.futures` and `joblib` for parallel data pipelines (Day 14) reproducible environments with `venv`, `pip`/`pip-tools`, `conda`, `uv` and `pyproject.toml` (Day 15) logging and debugging for data pipelines (Day 16), profiling and performance optimization (Day 17) and — as of Day 18, closing Phase 1 — Python packaging and reusable DS modules (`__init__.py`/`__all__`, `pyproject.toml` with `[project.scripts]`, `argparse` and Click CLIs, editable installs and wheels built with `python -m build`), and SQL with Python (Day 19: `sqlite3`, pandas `to_sql()`/`read_sql_query()`, CTEs, window functions and SQLAlchemy), and `argparse` command-line tools for DS pipelines (Day 20: subcommands, validation, train/evaluate/predict CLIs called via `subprocess`, CLI testing with `pytest`), and data modeling with `dataclasses`, `attrs` and `pydantic` (Day 21: validators, converters, nested models, JSON Schema, validated ML configs/results and DataFrame error reports), and configuration management for reproducible pipelines (Day 22: `configparser`, environment variables, `python-dotenv`, YAML anchors/aliases, `tomllib`/`tomli_w`, Hydra-style config composition with overrides and Pydantic-validated experiment configs), and design patterns for DS/ML code (Day 23: Pipeline, Factory, Strategy, Observer, Repository and Template Method built from scratch with `abc` and `typing.Protocol`), and abstract base classes and protocols (Day 24: `abc.ABC`/`@abstractmethod`, `typing.Protocol` structural subtyping, `@runtime_checkable`, `__subclasshook__` and type-safe NLP pipeline components), and working with web APIs (Day 25: `requests` and `httpx` sync/async clients, sessions and connection pooling, rate limiting, retries with exponential backoff and `tenacity`, offset and cursor pagination, response caching, and a small corpus built from the Wikipedia, Open Library and Datamuse public APIs), and memory management and memory-efficient patterns (Day 26: reference counting and the cyclic `gc`, the GIL, generators and `itertools` streaming, `tracemalloc`, pandas dtype downcasting and `category`, NumPy views vs copies and chunked processing of large CSVs), and data validation with Pandera (Day 27: `DataFrameSchema`/`Column`/`Check`, schema inference, `@check_input`/`@check_output` pipeline contracts, statistical `Hypothesis` checks, class-based `DataFrameModel`, a validation step inside scikit-learn pipelines and failure-case reports), and GitHub Actions & CI/CD for data science (Day 28: workflow anatomy and a PyYAML workflow validator, an `ast`-based code-quality checker, pytest fixture/parametrize/conftest patterns, a DataFrame contract validator, `nbformat` notebook checks, `nbconvert --execute` and a real CI workflow for this repository).
- **EDA (Phase 2, from Day 29):** structured exploratory analysis — data quality, missing-data mechanisms, distributions, bivariate relationships and confounding checks — as the bridge between Python skills and statistics/ML.
- **NLP aplicado à educação:** text-difficulty profiling, vocabulary-level heuristics and feedback tools for English learners.

### About Me

I am Gutemberg Rapôso, an English teacher and language researcher based in Palmas-TO, Brazil, building practical skills in data analysis and natural language processing. I am a doctoral student at the Federal University of Tocantins (UFT) and completed my master's degree in Letras (language and literature studies) in December 2025.

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
| 1 — Python basics | [01_python_basics](01_python_basics/) | **28 / 28** `▓▓▓▓▓▓▓▓▓▓` 100% | ✅ Complete — closed with GitHub Actions & CI/CD for Data Science (Day 28) |
| 2 — Exploratory data analysis | [02_eda](02_eda/) | **1 / 28** `▓░░░░░░░░░` 4% | 🔄 In progress — started with EDA Fundamentals (Day 29) |
| 3 — Statistics | [03_statistics](03_statistics/) | 0 / 28 | ⏳ Waiting |
| 4 — Machine learning | [04_machine_learning](04_machine_learning/) | 0 / 42 | ⏳ Waiting |
| 5 — Advanced ML | [05_advanced_ml](05_advanced_ml/) | 0 / 42 | ⏳ Waiting |
| 6 — NLP & time series | [06_nlp_timeseries](06_nlp_timeseries/) | 0 / 42 | ⏳ Waiting |
| 7 — Advanced projects | [07_advanced_projects](07_advanced_projects/) | 0 / 28 | ⏳ Waiting |

### Five most recent notebooks

1. **Day 29** — [Day 29 - EDA Fundamentals](02_eda/2026-11-28_eda-fundamentals.ipynb) (Phase 2 opener: EDA and CRISP-DM; inspection of seaborn Titanic with `shape`/`dtypes`/`info`/`describe`, unique values and programmatic checks of redundant columns; missing-value table and heatmap with an MCAR/MAR/MNAR discussion — `deck` ≈77% missing, `age` ≈20%; histograms, KDE, boxplots, IQR outliers, skewness and kurtosis; Pearson vs Spearman heatmaps; survival by sex (≈74% women vs ≈19% men), class, age group and family size; pairplot, split violin plots, countplots with hue and faceted charts that expose class composition as a likely confounder of embarkation port; descriptive only, no formal tests)
2. **Day 28** — [Day 28 - GitHub Actions & CI/CD for Data Science](01_python_basics/2026-11-27_github_actions_ci_ds.ipynb) (CI/CD concepts for DS vs. software; workflow anatomy with a PyYAML validator that handles YAML 1.1's `on` → `True`; an `ast`-based `CodeQualityChecker` for docstrings, type-hint coverage and basic cyclomatic complexity applied to the repository's own scripts; pytest fixture, `parametrize` and `conftest.py` patterns around a `DataPipelineValidator` on seaborn iris, tips and penguins; a scikit-learn wine smoke test against a majority baseline; a `NotebookMetadataChecker` run over all Phase 1 notebooks with a dashboard of real cell counts; and generation of `.github/workflows/ds_ci.yml`; the workflow is validated locally, not yet on GitHub)
3. **Day 27** — [Day 27 - Data Validation with Pandera](01_python_basics/2026-11-26_data_validation_pandera.ipynb) (`DataFrameSchema`, `Column` and `Check` contracts on seaborn tips with eager vs lazy validation and type coercion; `infer_schema`/`to_yaml` on titanic, then replacing sample-derived ranges with domain rules and cross-column consistency checks; `@check_input`/`@check_output`/`@check_io` contracts for a penguins cleaning pipeline; custom vectorized, element-wise, aggregate and grouped checks, plus `Hypothesis` t-test and chi-square checks on titanic; a class-based `DataFrameModel` with `@check_types` for clearly labeled synthetic English-learner assessment data (CEFR level, score, hours, seed 27); a `PanderaValidator` scikit-learn transformer guarding training and inference on iris; and failure-case reports, a quarantine pattern and charts showing pass rates; statistical checks monitor known properties and are not full inferential analyses)
4. **Day 26** — [Day 26 - Memory Management & Efficient Patterns](01_python_basics/2026-11-25_memory_management_ds.ipynb) (Python's object model with `id()`, shallow vs deep `sys.getsizeof`, small-int caching and `sys.intern` for repeated tokens; mutable vs immutable objects, list over-allocation, shallow/deep copies and `__slots__`; reference counting, the generational cyclic `gc` and `weakref` caches; the GIL contrasted on pure-Python vs NumPy threaded work; generators vs lists and `itertools` (`islice`, `batched`, `chain`, `groupby`, `pairwise`) for streaming; `tracemalloc` peaks and snapshot diffs; pandas dtype downcasting and `category` on seaborn titanic/diamonds/penguins; NumPy dtypes, views vs copies, in-place ops and `memmap`; chunked, typed `read_csv` aggregation of a 539,400-row diamonds replica; `float32` features for scikit-learn on wine; and a generator-based word-by-word corpus pipeline over scikit-learn `DESCR` texts with tokens, types, TTR and bigram collocation candidates; frequency bands are heuristic, not CEFR levels, and memory figures are machine-dependent)
5. **Day 25** — [Day 25 - Working with APIs & Requests](01_python_basics/2026-11-24_working_with_apis_requests.ipynb) (HTTP/REST basics, `requests` and `httpx` sync/async clients, sessions and retries, rate limiting, `tenacity`, offset and cursor pagination, response caching and a small corpus built from the Wikipedia, Open Library and Datamuse public APIs; API outputs reflect content at execution time)

## Learning archive

The existing notebooks and directory structure are preserved. As of 28 November 2026, the archive contains twenty-eight Python-fundamentals notebooks (Phase 1 complete), the first EDA notebook (Phase 2) and an additional `Módulo_2.ipynb`. The later phase directories contain placeholders, not completed advanced projects.

| Directory | Current status |
| --- | --- |
| [01_python_basics](01_python_basics/) | Twenty-eight learning notebooks (Phase 1 complete): pandas, NumPy, visualization (Matplotlib/Seaborn, Plotly), functions, strings/regex, file I/O, OOP, datetime/pandas, pytest, decorators/context managers, itertools/functools, typing/type hints, concurrency/parallel pipelines, environment management (venv, pip, conda, uv, pyproject.toml), logging & debugging, profiling & performance optimization, Python packaging & reusable DS modules (pyproject.toml, CLIs, wheels), SQL with Python (sqlite3, pandas + SQL, SQLAlchemy), `argparse` CLI scripts for data science, data modeling with dataclasses, attrs and pydantic, configuration management (YAML, TOML, dotenv, Hydra-style composition, Pydantic validation), and design patterns for DS/ML (Pipeline, Factory, Strategy, Observer, Repository, Template Method), abstract base classes & `typing.Protocol` interfaces for DS components, and working with web APIs (`requests`, `httpx`, rate limiting, retries, pagination, caching), and Python memory management & memory-efficient patterns (`gc`, GIL, generators, `tracemalloc`, dtype optimization, chunked processing), and data validation with Pandera (schemas, decorators, hypothesis checks, `DataFrameModel`, scikit-learn integration), and GitHub Actions & CI/CD for data science (workflow validation, `ast` quality checks, notebook validation with `nbformat`/`nbconvert`). |
| [Módulo_2.ipynb](Módulo_2.ipynb) | Additional historical notebook. |
| [02_eda](02_eda/) | Phase 2 in progress — 1 notebook: [EDA Fundamentals](02_eda/2026-11-28_eda-fundamentals.ipynb) (Titanic). |
| [03_statistics](03_statistics/) | Planned study phase; placeholder. |
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
