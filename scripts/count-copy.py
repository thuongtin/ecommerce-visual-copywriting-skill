#!/usr/bin/env python3
"""Count copy lengths using the skill's internal layout convention, not platform rules."""
import argparse
import json


def count(text: str, language: str) -> int:
    if language in ("vi", "en"):
        return sum(any(char.isalnum() for char in token) for token in text.split())
    return sum(not char.isspace() for char in text)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", choices=("vi", "en", "zh"), default="vi")
    parser.add_argument("texts", nargs="+")
    args = parser.parse_args()
    print(json.dumps([
        {"text": text, "count": count(text, args.language), "unit": {"vi": "syllables", "en": "words"}.get(args.language, "characters")}
        for text in args.texts
    ], ensure_ascii=False))


if __name__ == "__main__":
    main()
