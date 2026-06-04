import unittest

import analizzatore


SAMPLE_TEXT = """Luna osservava il mare. Il vento era fresco.

La notte sembrava calma."""


class AnalyzeTextTests(unittest.TestCase):
    def test_analyze_text_returns_basic_metrics(self):
        result = analizzatore.analyze_text(SAMPLE_TEXT)

        self.assertGreater(result["character_count"], 0)
        self.assertEqual(result["word_count"], 12)
        self.assertEqual(result["sentence_count"], 3)
        self.assertEqual(result["paragraph_count"], 2)
        self.assertGreater(result["avg_words_per_sentence"], 0)
        self.assertIsInstance(result["top_words"], list)

    def test_analyze_text_ignores_punctuation_and_case(self):
        result = analizzatore.analyze_text("Luna, luna! luna?")

        self.assertEqual(result["word_count"], 3)
        self.assertEqual(result["top_words"][:1], [("luna", 3)])

    def test_analyze_text_counts_sentences_across_newlines(self):
        result = analizzatore.analyze_text("Luna osservava il mare.\nIl vento era fresco")

        self.assertEqual(result["sentence_count"], 2)
        self.assertEqual(result["word_count"], 8)
        self.assertEqual(result["avg_words_per_sentence"], 4.0)


if __name__ == "__main__":
    unittest.main()
