import string
from collections import Counter
from typing import List

from task1.utils import (
    is_char_ascii,
    not_ascii_chars,
    read_file_text,
    read_text_words,
    unique_symbols_count,
)


def get_longest_diverse_words(file_path: str) -> List[str]:
    words = read_text_words(file_path)
    return sorted(words, key=unique_symbols_count, reverse=True)[:10]


def get_rarest_char(file_path: str) -> str:
    return list(Counter(read_file_text(file_path)).keys())[-1]


def count_punctuation_chars(file_path: str) -> int:
    text = read_file_text(file_path)
    return sum(text.count(char) for char in string.punctuation)


def count_non_ascii_chars(file_path: str) -> int:
    text = read_file_text(file_path)
    count = 0
    for char in text:
        if not is_char_ascii(char):
            count += 1
    return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    return list(Counter(not_ascii_chars(read_file_text(file_path))).keys())[0]
