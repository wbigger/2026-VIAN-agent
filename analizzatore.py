import argparse
import re
import sys
from collections import Counter
from pathlib import Path


WORD_RE = re.compile(r"\b[\w']+\b", re.UNICODE)
SENTENCE_RE = re.compile(r"[^.!?]+(?:[.!?]+|$)", re.UNICODE | re.DOTALL)


def read_text(path: str | None) -> str:
    """Read text from a file path or from standard input."""
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def analyze_text(text: str) -> dict:
    """Compute basic writing metrics for a text."""
    cleaned_text = text.strip()
    if not cleaned_text:
        return {
            "character_count": 0,
            "word_count": 0,
            "sentence_count": 0,
            "paragraph_count": 0,
            "avg_words_per_sentence": 0.0,
            "top_words": [],
        }

    words = [w.lower() for w in WORD_RE.findall(cleaned_text)]
    sentences = [s.strip() for s in SENTENCE_RE.findall(cleaned_text) if s.strip()]
    if not sentences and words:
        sentences = [cleaned_text]
    paragraphs = [p for p in re.split(r"\n\s*\n", cleaned_text) if p.strip()]

    word_counts = Counter(words)
    top_words = word_counts.most_common(10)

    sentence_count = len(sentences)
    avg_words_per_sentence = len(words) / sentence_count if sentence_count else 0.0

    return {
        "character_count": len(cleaned_text),
        "word_count": len(words),
        "sentence_count": len(sentences),
        "paragraph_count": len(paragraphs),
        "avg_words_per_sentence": round(avg_words_per_sentence, 2),
        "top_words": top_words,
    }


def format_report(metrics: dict) -> str:
    """Render the analysis as a readable terminal report."""
    lines = [
        "Analizzatore di testi per scrittura professionale",
        "=" * 52,
        f"Caratteri: {metrics['character_count']}",
        f"Parole: {metrics['word_count']}",
        f"Frasi: {metrics['sentence_count']}",
        f"Paragrafi: {metrics['paragraph_count']}",
        f"Parole medie per frase: {metrics['avg_words_per_sentence']:.2f}",
        "",
        "Parole più frequenti:",
    ]

    if metrics["top_words"]:
        for word, count in metrics["top_words"]:
            lines.append(f"  - {word}: {count}")
    else:
        lines.append("  (nessun contenuto da analizzare)")

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Analizza un testo per supportare la scrittura di romanzi."
    )
    parser.add_argument("path", nargs="?", help="Percorso del file da analizzare")
    args = parser.parse_args(argv)

    text = read_text(args.path)
    metrics = analyze_text(text)
    print(format_report(metrics))
    return 0


if __name__ == "__main__":
    raise SystemExit(main()) 