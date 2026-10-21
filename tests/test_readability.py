import importlib.util
from pathlib import Path
import unittest

path = Path(__file__).parents[1] / "projects/readability_demo/analyze.py"
spec = importlib.util.spec_from_file_location("readability", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ReadabilityTests(unittest.TestCase):
    def test_empty_and_punctuation(self):
        for text in ["", "...?!", "123"]:
            result = module.analyze(text)
            self.assertEqual(result["word_count"], 0)
            self.assertIsNone(result["estimated_flesch_reading_ease"])

    def test_shared_tokenization(self):
        self.assertEqual(module.words("It's a well-known fact."), ["It's", "a", "well", "known", "fact"])
        result = module.analyze("It's a well-known fact.")
        self.assertEqual(result["word_count"], 5)
        self.assertEqual(result["sentence_count"], 1)

    def test_sentence_and_case_rules(self):
        result = module.analyze("We read. WE read!")
        self.assertEqual(result["word_count"], 4)
        self.assertEqual(result["sentence_count"], 2)
        self.assertEqual(result["lexical_diversity"], 0.5)

    def test_hand_calculated_simple_example(self):
        result = module.analyze("We read.")
        self.assertEqual(result["estimated_syllables"], 2)
        self.assertAlmostEqual(result["estimated_flesch_reading_ease"], 120.21, places=2)
