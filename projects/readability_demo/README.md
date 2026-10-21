# Reproducible English readability demonstration

This companion demonstration leaves the [historical OOP notebook](../../01_python_basics/2026-10-20_python_oop_for_ds.ipynb) unchanged. It uses two **original, synthetic, AI-assisted passages**, created for this repository on 21 October 2026. They are not literary excerpts, learner data or client material.

Run from the repository root with Python 3.13:

```bash
python projects/readability_demo/analyze.py
python -m unittest discover -s tests -v
```

No downloads, credentials or third-party Python dependencies are needed for this demonstration. See [samples](samples.json), [implementation](analyze.py) and [generated results](results.json).

## Consistent counting

A single word tokenizer supplies word count, lexical diversity and syllable estimation. It keeps straight/curly apostrophes within a token, splits hyphens, and excludes numbers. Sentence boundaries use periods, exclamation marks and question marks; segments without words are ignored. Lexical diversity folds case and normalizes curly apostrophes.

Flesch Reading Ease = 206.835 − 1.015 × words/sentences − 84.6 × estimated syllables/words. Syllables use vowel groups with a limited final-e adjustment. Empty or punctuation-only input returns null scores, not division errors.

## Interpretation limits

The two passages illustrate how surface measures respond to sentence length and estimated syllable counts. They do not constitute a controlled experiment, a validated reading-level predictor, a CEFR classifier or evidence of learner comprehension. Syllable estimates can be wrong; abbreviations and sentence fragments can distort sentence counts. The tokenizer is intended for these English examples and is not a general multilingual tokenizer. Scores are not clipped to 0–100.

No text of uncertain third-party provenance was copied into this example. The historical notebook's source and rights questions remain open. AI assistance supported code, samples and documentation; passing software tests does not validate a linguistic construct.
