# Gutemberg Rapôso — Data, Language & NLP

![Currently Learning](https://img.shields.io/badge/%F0%9F%94%AC%20Currently%20Learning-Abstract%20Classes%20%26%20Protocols%20for%20DS-blue)

🔬 Currently Learning: Abstract Classes & Protocols for DS

**Junior → Senior Data Scientist | Open to Remote Opportunities**

Learning path — a long-term development goal, not a claim of current seniority.

### Unique background: Linguística + Data Science + NLP aplicado à educação

- **Linguística:** sociolinguistics, register variation and language-teaching experience shape how I clean, tokenize and interpret text.
- **Data Science:** Python, pandas, NumPy, visualization, automated testing with pytest (Day 10), decorators and context managers (Day 11), `itertools`/`functools` for lazy, memory-efficient pipelines (Day 12) the `typing` module and type hints (Day 13), concurrency with `threading`, `multiprocessing`, `concurrent.futures` and `joblib` for parallel data pipelines (Day 14) reproducible environments with `venv`, `pip`/`pip-tools`, `conda`, `uv` and `pyproject.toml` (Day 15) logging and debugging for data pipelines (Day 16), profiling and performance optimization (Day 17) and — as of Day 18, closing Phase 1 — Python packaging and reusable DS modules (`__init__.py`/`__all__`, `pyproject.toml` with `[project.scripts]`, `argparse` and Click CLIs, editable installs and wheels built with `python -m build`), and SQL with Python (Day 19: `sqlite3`, pandas `to_sql()`/`read_sql_query()`, CTEs, window functions and SQLAlchemy), and `argparse` command-line tools for DS pipelines (Day 20: subcommands, validation, train/evaluate/predict CLIs called via `subprocess`, CLI testing with `pytest`), and data modeling with `dataclasses`, `attrs` and `pydantic` (Day 21: validators, converters, nested models, JSON Schema, validated ML configs/results and DataFrame error reports), and configuration management for reproducible pipelines (Day 22: `configparser`, environment variables, `python-dotenv`, YAML anchors/aliases, `tomllib`/`tomli_w`, Hydra-style config composition with overrides and Pydantic-validated experiment configs), and design patterns for DS/ML code (Day 23: Pipeline, Factory, Strategy, Observer, Repository and Template Method built from scratch with `abc` and `typing.Protocol`), and abstract base classes and protocols (Day 24: `abc.ABC`/`@abstractmethod`, `typing.Protocol` structural subtyping, `@runtime_checkable`, `__subclasshook__` and type-safe NLP pipeline components).
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
| 1 — Python basics | [01_python_basics](01_python_basics/) | **24 / 28** `▓▓▓▓▓▓▓▓▓░` 86% | 🟢 In progress — Python-fundamentals block complete; SQL with Python, CLI scripts, data modeling (dataclasses/attrs/pydantic), configuration management, design patterns and ABCs/Protocols for DS done |
| 2 — Exploratory data analysis | [02_eda](02_eda/) | 0 / 28 | ⚪ Planned |
| 3 — Statistics | [03_statistics](03_statistics/) | 0 / 28 | ⚪ Planned |
| 4 — Machine learning | [04_machine_learning](04_machine_learning/) | 0 / 42 | ⚪ Planned |
| 5 — Advanced ML | [05_advanced_ml](05_advanced_ml/) | 0 / 42 | ⚪ Planned |
| 6 — NLP & time series | [06_nlp_timeseries](06_nlp_timeseries/) | 0 / 42 | ⚪ Planned |
| 7 — Advanced projects | [07_advanced_projects](07_advanced_projects/) | 0 / 28 | ⚪ Planned |

### Five most recent notebooks

1. **Day 24** — [2026-11-23 — Abstract classes & Protocols for Data Science](01_python_basics/2026-11-23_abstract_classes_protocols_ds.ipynb) (`abc.ABC`/`@abstractmethod`, `@property` + `@abstractmethod` instead of the deprecated `abstractproperty`, and `collections.abc` checks; a template-method `DataTransformer` ABC with shared validation whose StandardScaler-like and MinMax-like subclasses match scikit-learn on iris; a typed `TextProcessor[InT, OutT]` ABC (normalizer, regex tokenizer, stopword remover) applied to a corpus built from the real `DESCR` documentation of scikit-learn and statsmodels datasets; `typing.Protocol` structural subtyping with `Fittable`, `Transformable`, `Scorable` and composite protocols satisfied by scikit-learn objects without inheritance; `@runtime_checkable` `isinstance()` matrices and the pitfall that only member names are checked; an `EvaluationMetric` ABC with Accuracy, F1 and RMSE matching scikit-learn on breast_cancer and driving direction-aware model selection; CSV/JSON/seaborn `DataLoader`s with shared validation; an ABC + Protocol educational-text pipeline computing illustrative difficulty heuristics (not validated readability or CEFR levels); `__subclasshook__` and `register()` virtual subclasses; an ABC vs Protocol vs duck-typing comparison and metaclass-conflict pitfalls; results come from single splits and a 10-document corpus and are illustrative)
2. **Day 23** — [2026-11-22 — Python design patterns for Data Science](01_python_basics/2026-11-22_design_patterns_ds.ipynb) (a from-scratch **Pipeline** of single-responsibility text steps — lowercasing, accent stripping, tokenization, stopwords, minimum length and a light stemmer — applied to an educational corpus made of the real `DESCR` documentation of 13 scikit-learn and statsmodels datasets, with per-document type-token ratios; a registry-based **Factory** (decorator registration, defaults merged with config) building LogisticRegression, RandomForest, SVM, SGD and Ridge estimators compared with 5-fold CV on breast_cancer; a **Strategy** interface via `typing.Protocol` swapping Standard/MinMax/Robust scalers and a custom log-standard strategy on seaborn tips and wine, showing convergence differences without scaling; an **Observer** trainer using `partial_fit` with console logger, history recorder, early stopping and best-model checkpoint observers; a **Repository** layer serving scikit-learn, seaborn, statsmodels and CSV data through a cached `DataCatalog`; a **Template Method** `MLExperiment` base class driving classification and regression experiments; an integration project classifying paragraph origin (scikit-learn vs statsmodels documentation) with from-scratch count/TF-IDF vectorizer strategies and a document-grouped split; five `assert` tests with a fake in-memory repository; and a PT-BR comparison table of when to use each pattern; all results come from single splits or small CV runs and are illustrative, not model rankings)
3. **Day 22** — [2026-11-21 — Configuration management for Data Science](01_python_basics/2026-11-21_configuration_management_ds.ipynb) (`configparser` INI files with typed getters and `[DEFAULT]` inheritance, `os.environ` defaults and a defaults < file < env < CLI precedence resolver with `argparse`; `.env` files loaded with `python-dotenv` (`dotenv_values`/`load_dotenv`), `.env.example`, `.gitignore` and secret masking, driving a decision tree on seaborn titanic; YAML with `yaml.safe_load`/`safe_dump`, nested sections, anchors, aliases and `<<:` merges powering Ridge experiments on seaborn tips; TOML read with `tomllib` and written with `tomli_w` for an NLTK Brown Corpus vocabulary profiler with frequency bands derived from the corpus itself (CEFR-inspired, not official CEFR levels) and a YAML-vs-TOML comparison; a Hydra-style composer (config groups, deep merge, dotted overrides, frozen dataclasses) running four scikit-learn iris LogisticRegression experiments; Pydantic v2 `PipelineConfig` validation with `extra="forbid"`, level validators and tabular error reports; dev/staging/prod configs with hashes and env-var secrets; and a YAML → Pydantic → scikit-learn penguins pipeline producing five experiments, resolved-config snapshots and metrics without code changes (single split, not a model ranking); all config files live in a temporary directory)
4. **Day 21** — [2026-11-20 — Data modeling with dataclasses, attrs & pydantic](01_python_basics/2026-11-20_dataclasses_pydantic_ds.ipynb) (`@dataclass` with `__post_init__` validation, `field()`/`default_factory`, `asdict()`/`astuple()`, `frozen=True`, `slots=True`, `ClassVar` and a `BaseRecord → LinguisticRecord → CEFRRecord` hierarchy; seaborn iris rows round-tripped through dataclasses; `attrs` `@define` classes with custom CEFR/positive-number validators and converters, and a frozen `PassengerRecord` validating all 891 titanic rows; Pydantic v2 `Field` constraints, `field_validator`/`model_validator`, `computed_field`, `model_validate`/`model_dump_json`/JSON Schema, a `Course → Module → Lesson` nested model, and a reusable row-level validator producing error reports on a deliberately corrupted copy of penguins; a 10,000-instance construction benchmark and feature-comparison table; a frozen `MLDatasetConfig` and `ModelResult` driving three scikit-learn iris pipelines saved/reloaded as JSON Lines (single split, not a model ranking); and a `CEFRVocabularyEntry` model validating 6,000 NLTK Brown Corpus word forms with frequency bands derived from the corpus itself (CEFR-inspired, not official CEFR levels); timings are machine-dependent)
5. **Day 20** — [2026-11-19 — argparse & CLI scripts for Data Science](01_python_basics/2026-11-19_argparse_cli_ds.ipynb) (positional/optional arguments, flags, `type`/`choices`/defaults and auto-generated help on seaborn iris, tips and titanic; custom type validators, a custom `argparse.Action`, parent parsers, argument groups and mutually exclusive groups; an `analyze`/`visualize`/`export` subcommand tool with `set_defaults(func=...)` dispatch and `parser.error()` validation; a `ds_pipeline.py` script with `train`/`evaluate`/`predict` subcommands on scikit-learn iris, wine and breast_cancer, run through `subprocess` with JSON/CSV outputs, exit codes 0/1/2 and a 3×3 dataset × model grid (single split, not a model ranking); a `vocab_cli.py` tool (`--corpus`, `--language`, `--min-freq`, `--output-format`) profiling NLTK Brown Corpus registers with frequency bands derived from the corpus itself (CEFR-inspired, not official CEFR levels); `nbconvert --to script`, `argparse` + `logging` verbosity, 7 passing `pytest` CLI tests and `[project.scripts]` entry points)

## Learning archive

The existing notebooks and directory structure are preserved. As of 23 November 2026, the archive contains twenty-four Python-fundamentals notebooks and an additional `Módulo_2.ipynb`. The later phase directories contain placeholders, not completed advanced projects.

| Directory | Current status |
| --- | --- |
| [01_python_basics](01_python_basics/) | Twenty-four learning notebooks: pandas, NumPy, visualization (Matplotlib/Seaborn, Plotly), functions, strings/regex, file I/O, OOP, datetime/pandas, pytest, decorators/context managers, itertools/functools, typing/type hints, concurrency/parallel pipelines, environment management (venv, pip, conda, uv, pyproject.toml), logging & debugging, profiling & performance optimization, Python packaging & reusable DS modules (pyproject.toml, CLIs, wheels), SQL with Python (sqlite3, pandas + SQL, SQLAlchemy), `argparse` CLI scripts for data science, data modeling with dataclasses, attrs and pydantic, configuration management (YAML, TOML, dotenv, Hydra-style composition, Pydantic validation), and design patterns for DS/ML (Pipeline, Factory, Strategy, Observer, Repository, Template Method), and abstract base classes & `typing.Protocol` interfaces for DS components. |
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
