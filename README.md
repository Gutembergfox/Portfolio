# Gutemberg Rapôso — Data, Language & NLP

![Currently Learning](https://img.shields.io/badge/%F0%9F%94%AC%20Currently%20Learning-dataclasses%20%C2%B7%20attrs%20%C2%B7%20pydantic-blue)

🔬 Currently Learning: dataclasses · attrs · pydantic — Data Modeling for DS

**Junior → Senior Data Scientist | Open to Remote Opportunities**

Learning path — a long-term development goal, not a claim of current seniority.

### Unique background: Linguística + Data Science + NLP aplicado à educação

- **Linguística:** sociolinguistics, register variation and language-teaching experience shape how I clean, tokenize and interpret text.
- **Data Science:** Python, pandas, NumPy, visualization, automated testing with pytest (Day 10), decorators and context managers (Day 11), `itertools`/`functools` for lazy, memory-efficient pipelines (Day 12) the `typing` module and type hints (Day 13), concurrency with `threading`, `multiprocessing`, `concurrent.futures` and `joblib` for parallel data pipelines (Day 14) reproducible environments with `venv`, `pip`/`pip-tools`, `conda`, `uv` and `pyproject.toml` (Day 15) logging and debugging for data pipelines (Day 16), profiling and performance optimization (Day 17) and — as of Day 18, closing Phase 1 — Python packaging and reusable DS modules (`__init__.py`/`__all__`, `pyproject.toml` with `[project.scripts]`, `argparse` and Click CLIs, editable installs and wheels built with `python -m build`), and SQL with Python (Day 19: `sqlite3`, pandas `to_sql()`/`read_sql_query()`, CTEs, window functions and SQLAlchemy), and `argparse` command-line tools for DS pipelines (Day 20: subcommands, validation, train/evaluate/predict CLIs called via `subprocess`, CLI testing with `pytest`), and data modeling with `dataclasses`, `attrs` and `pydantic` (Day 21: validators, converters, nested models, JSON Schema, validated ML configs/results and DataFrame error reports).
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
| 1 — Python basics | [01_python_basics](01_python_basics/) | **21 / 28** `▓▓▓▓▓▓▓▓░░` 75% | 🟢 In progress — Python-fundamentals block complete; SQL with Python, CLI scripts and data modeling (dataclasses/attrs/pydantic) done |
| 2 — Exploratory data analysis | [02_eda](02_eda/) | 0 / 28 | ⚪ Planned |
| 3 — Statistics | [03_statistics](03_statistics/) | 0 / 28 | ⚪ Planned |
| 4 — Machine learning | [04_machine_learning](04_machine_learning/) | 0 / 42 | ⚪ Planned |
| 5 — Advanced ML | [05_advanced_ml](05_advanced_ml/) | 0 / 42 | ⚪ Planned |
| 6 — NLP & time series | [06_nlp_timeseries](06_nlp_timeseries/) | 0 / 42 | ⚪ Planned |
| 7 — Advanced projects | [07_advanced_projects](07_advanced_projects/) | 0 / 28 | ⚪ Planned |

### Five most recent notebooks

1. **Day 21** — [2026-11-20 — Data modeling with dataclasses, attrs & pydantic](01_python_basics/2026-11-20_dataclasses_pydantic_ds.ipynb) (`@dataclass` with `__post_init__` validation, `field()`/`default_factory`, `asdict()`/`astuple()`, `frozen=True`, `slots=True`, `ClassVar` and a `BaseRecord → LinguisticRecord → CEFRRecord` hierarchy; seaborn iris rows round-tripped through dataclasses; `attrs` `@define` classes with custom CEFR/positive-number validators and converters, and a frozen `PassengerRecord` validating all 891 titanic rows; Pydantic v2 `Field` constraints, `field_validator`/`model_validator`, `computed_field`, `model_validate`/`model_dump_json`/JSON Schema, a `Course → Module → Lesson` nested model, and a reusable row-level validator producing error reports on a deliberately corrupted copy of penguins; a 10,000-instance construction benchmark and feature-comparison table; a frozen `MLDatasetConfig` and `ModelResult` driving three scikit-learn iris pipelines saved/reloaded as JSON Lines (single split, not a model ranking); and a `CEFRVocabularyEntry` model validating 6,000 NLTK Brown Corpus word forms with frequency bands derived from the corpus itself (CEFR-inspired, not official CEFR levels); timings are machine-dependent)
2. **Day 20** — [2026-11-19 — argparse & CLI scripts for Data Science](01_python_basics/2026-11-19_argparse_cli_ds.ipynb) (positional/optional arguments, flags, `type`/`choices`/defaults and auto-generated help on seaborn iris, tips and titanic; custom type validators, a custom `argparse.Action`, parent parsers, argument groups and mutually exclusive groups; an `analyze`/`visualize`/`export` subcommand tool with `set_defaults(func=...)` dispatch and `parser.error()` validation; a `ds_pipeline.py` script with `train`/`evaluate`/`predict` subcommands on scikit-learn iris, wine and breast_cancer, run through `subprocess` with JSON/CSV outputs, exit codes 0/1/2 and a 3×3 dataset × model grid (single split, not a model ranking); a `vocab_cli.py` tool (`--corpus`, `--language`, `--min-freq`, `--output-format`) profiling NLTK Brown Corpus registers with frequency bands derived from the corpus itself (CEFR-inspired, not official CEFR levels); `nbconvert --to script`, `argparse` + `logging` verbosity, 7 passing `pytest` CLI tests and `[project.scripts]` entry points)
3. **Day 19** — [2026-11-18 — SQL with Python for Data Science](01_python_basics/2026-11-18_sql_python_ds.ipynb) (`sqlite3` in-memory databases, `CHECK` constraints, parameterized inserts and transactional rollback; seaborn tips, titanic, penguins and flights loaded with `to_sql()`; `SELECT`/`WHERE`/`ORDER BY`/`LIMIT`, `CASE WHEN`, `GROUP BY`/`HAVING` and `COUNT(*)` vs `COUNT(col)` checked against pandas; `INNER`/`LEFT JOIN` on dimension tables derived from the real data; subqueries and CTEs; `ROW_NUMBER`, `RANK`, `LAG`/`LEAD` and running totals on the flights series, validated against `shift()`; `read_sql_query()` with `params`, `dtype` and `chunksize`; SQLAlchemy 2.x `text()`, reflected Core `select()` and a small ORM table storing real iris cross-validation scores; a relational NLTK Brown Corpus database measuring lexical coverage by genre with frequency bands derived from the corpus itself (not CEFR levels); and an index shown changing `EXPLAIN QUERY PLAN` from `SCAN` to `SEARCH`; timings are machine-dependent)
4. **Day 18** — [2026-10-31 — Python packaging & reusable DS modules](01_python_basics/2026-10-31_python_packaging_ds_modules.ipynb) (closes Phase 1's Python-fundamentals block: packages, sub-packages, `__init__.py`, `__all__` and relative imports; an annotated `pyproject.toml` parsed with `tomllib`; a `src/`-layout `dskit` package with a cached seaborn `data_loader`, a leakage-safe fit/transform `preprocessor` and figure-returning `visualizer` applied to titanic, penguins and tips; the same CLI in `argparse` and Click with subcommands, JSON/CSV output and exit codes; 17 `pytest` tests, a real `pip install -e .` in a temporary venv with working console scripts, and an sdist/wheel built with `python -m build` and inspected; plus a pure-Python `nlp_edu` package — `word_frequency()`, Flesch/Flesch-Kincaid `readability_score()` and a heuristic, CEFR-inspired `cefr_classifier()` — applied to the NLTK Gutenberg corpus; the CEFR-like bands are not official CEFR levels)
5. **Day 17** — [2026-10-30 — Python profiling & performance optimization](01_python_basics/2026-10-30_profiling_performance_optimization.ipynb) (`timeit`, `cProfile` and `pstats` on a 20 Newsgroups word-frequency function, a didactic line profiler built on `sys.settrace`, `tracemalloc` snapshots of a bag-of-words pipeline, memory of text representations (dense vs sparse CSR), manual TF-IDF, cosine similarity and feature standardization as Python loops vs NumPy vs scipy/sklearn — each checked with `np.allclose`, string operations on seaborn titanic, pandas `apply`/`iterrows`/`itertuples` vs vectorized code, categoricals and `query()` on replicated seaborn tips/titanic, `dict`/`set`/`heapq` for NLP vocabularies, and a profiled `StandardScaler` → `PCA` → `SVC` pipeline on `load_digits`; timings are machine-dependent)

## Learning archive

The existing notebooks and directory structure are preserved. As of 20 November 2026, the archive contains twenty-one Python-fundamentals notebooks and an additional `Módulo_2.ipynb`. The later phase directories contain placeholders, not completed advanced projects.

| Directory | Current status |
| --- | --- |
| [01_python_basics](01_python_basics/) | Twenty-one learning notebooks: pandas, NumPy, visualization (Matplotlib/Seaborn, Plotly), functions, strings/regex, file I/O, OOP, datetime/pandas, pytest, decorators/context managers, itertools/functools, typing/type hints, concurrency/parallel pipelines, environment management (venv, pip, conda, uv, pyproject.toml), logging & debugging, profiling & performance optimization, Python packaging & reusable DS modules (pyproject.toml, CLIs, wheels), SQL with Python (sqlite3, pandas + SQL, SQLAlchemy), `argparse` CLI scripts for data science, and data modeling with dataclasses, attrs and pydantic. |
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
