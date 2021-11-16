from typing import List


def read_file_text(file_path: str) -> str:
    with open(file_path, encoding="unicode-escape") as file:
        return file.read()


def read_text_words(file_path: str) -> List[str]:
    return [
        word for word in read_file_text(file_path).replace("\n", "").split(" ") if word
    ]


def unique_symbols_count(word: str) -> int:
    return len(set(word))


def is_char_ascii(char: str) -> bool:
    return ord(char) <= 255


def not_ascii_chars(text: str) -> List[str]:
    return [char for char in text if not is_char_ascii(char)]
