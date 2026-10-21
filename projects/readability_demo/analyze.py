"""English-only educational readability demo using original synthetic samples."""
import json
import re
from pathlib import Path

TOKEN = re.compile(r"[A-Za-z]+(?:['’][A-Za-z]+)*")


def words(text):
    return TOKEN.findall(text)


def syllables(word):
    # Deliberately simple heuristic, not a pronunciation dictionary.
    word = word.lower().replace("’", "").replace("'", "")
    groups = len(re.findall(r"[aeiouy]+", word))
    if word.endswith("e") and not word.endswith(("le", "ye")) and groups > 1:
        groups -= 1
    return max(1, groups)


def analyze(text):
    tokens = words(text)
    sentences = [part for part in re.split(r"[.!?]+", text) if words(part)]
    count = len(tokens)
    sentence_count = len(sentences)
    syllable_count = sum(syllables(word) for word in tokens)
    return {
        "word_count": count,
        "sentence_count": sentence_count,
        "estimated_syllables": syllable_count,
        "lexical_diversity": round(len({w.lower().replace("’", "'") for w in tokens}) / count, 4) if count else None,
        "estimated_flesch_reading_ease": round(206.835 - 1.015 * count / sentence_count - 84.6 * syllable_count / count, 2) if count and sentence_count else None,
    }


def main():
    root = Path(__file__).resolve().parent
    samples = json.loads((root / "samples.json").read_text())
    results = [{"id": sample["id"], **analyze(sample["text"])} for sample in samples]
    (root / "results.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
