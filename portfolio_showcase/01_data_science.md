# English Text Readability: An Interpretable NLP Prototype

Gutemberg Rapôso | Python · pandas · scikit-learn · NLP · Linguistics

## Project at a glance

This learning project explores how an interpretable Python pipeline can summarize the readability and lexical characteristics of English literary excerpts. It connects linguistic analysis with reusable software components rather than treating a single readability score as a complete assessment of reading difficulty.

**Status:** educational prototype with saved notebook outputs. Not a deployed product, validated proficiency classifier, or demonstrated improvement in learning outcomes.

[View the source notebook](https://github.com/Gutembergfox/Portfolio/blob/master/01_python_basics/2026-10-20_python_oop_for_ds.ipynb)

## Question

How can a small, transparent NLP workflow help an educator inspect differences between English excerpts, while making the limitations of automated readability metrics visible?

## Data and scope

The notebook includes eight short excerpts attributed to Potter, Carroll, Austen, Dickens, Melville, Lincoln, Jefferson and Twain. The source describes these as public-domain texts. Exact edition and source-URL provenance still need to be documented. The analysis covers these excerpts, not the full books, learners' abilities, or a representative educational corpus. No student records are used in the readability analysis.

A separate Titanic example illustrates numerical scaling. It is a programming demonstration, not part of the educational NLP findings.

## Implementation

- A `TextCleaner` normalizes text, with optional stopword removal.
- A `ReadabilityScorer` implements the scikit-learn estimator interface and computes Flesch Reading Ease, Flesch–Kincaid grade, average sentence length, average syllables per word and word count.
- An `NLPPipeline` composes cleaning and readability components. Readability is calculated on the original text, preserving punctuation; lexical statistics use the cleaned text.
- pandas combines the measurements into a report. Matplotlib and Seaborn visualize excerpt-level differences.
- The notebook demonstrates estimator cloning, parameter changes and a three-feature scikit-learn pipeline with an output shape of 8 × 3.

These are deterministic measurements and software-interface demonstrations. No predictive model is trained or evaluated in this case study.

## What the saved outputs show

| Excerpt | Flesch Reading Ease |
|---|---:|
| The Adventures of Tom Sawyer | 99.86 |
| The Tale of Peter Rabbit | 76.02 |
| Moby-Dick | 63.03 |
| Pride and Prejudice | 48.04 |
| Gettysburg Address | 44.70 |
| Declaration of Independence | 43.40 |
| A Tale of Two Cities | 40.18 |
| Alice's Adventures in Wonderland | 30.24 |

These values are copied from the notebook's stored outputs, not independently reproduced in this review. They describe the selected passages under the notebook's tokenization and syllable-counting rules.

The Carroll excerpt illustrates an important limitation: its long sentence lowers the score even when much of its vocabulary is familiar. The Twain excerpt contains short, repeated dialogue; its high score does not establish that the whole novel is easy for a learner.

The stopword comparison also makes preprocessing choices visible. For the Twain passage, the stored type-token ratio is 0.538 with stopwords removed versus 0.647 with them retained. This is an example of how a short, repetitive passage can behave differently from a general expectation.

## Limitations and responsible use

- Eight short, hand-selected excerpts cannot establish general performance or curriculum suitability.
- Syllables are counted using a spelling heuristic. Sentence boundaries use punctuation matching, not a linguistic sentence segmenter.
- The source uses different tokenization rules in `TextDocument` and `ReadabilityScorer`. For example, the Potter excerpt has 34 words in the former and 37 in the latter because hyphenated forms are treated differently. The reported scores use the latter.
- Flesch scores and US grade-level formulas are not validated CEFR labels. The original notebook's A1–A2 and B2–C1 suggestions should not be treated as established findings.
- Correlations between a formula and its own inputs are descriptive, not evidence of predictive performance or a causal explanation of comprehension.
- No held-out evaluation, learner study, deployment, business-impact measurement or automated test suite is demonstrated here.

## Next iteration

1. Separate the readability case from unrelated programming exercises.
2. Document exact text sources, edition provenance and applicable reuse terms.
3. Make tokenization consistent and add tests for hyphens, apostrophes, empty input, abbreviations and non-string values.
4. Record dependencies and rerun from a clean environment, publishing the execution log and reproducible report.
5. If proficiency assessment becomes a goal, use an appropriately licensed and independently annotated corpus, with held-out evaluation and error analysis. Keep this separate from the current demonstration.

## Evidence and verification

Reviewed on 21 October 2026. The source notebook contains 43 cells, including 25 code cells with saved execution counts 1–25 and no stored error outputs. This is evidence of recorded execution, not proof of a fresh, reproducible run.

[Pinned source version](https://github.com/Gutembergfox/Portfolio/blob/58b1db1d720e83b8121e73576f6b0d660655ea25/01_python_basics/2026-10-20_python_oop_for_ds.ipynb)

[Back to portfolio showcase](README.md)
