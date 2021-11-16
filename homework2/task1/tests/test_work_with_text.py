import os

import pytest
from task1.work_with_text import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)

path = os.path.dirname(__file__)


def test_get_longest_diverse_words():
    assert get_longest_diverse_words(path + "/data.txt") == [
        "3-608-93071-XSchutzumschlag:Autograph",
        "3-608-95022-2Maxima-MinimaAdnoten",
        "Heilungen.Selbstverständlich",
        "her-auf.ÜBERSICHT1.",
        "außenpolitischbemerkbar",
        "Waldgänger.Historisch",
        "Maskenwelthinausgeführt.",
        "Souveränitätsan-sprüche",
        "Menschauftrete.Soviel",
        "mythischeZeugungskraft.",
    ]


def test_get_rarest_char():
    assert get_rarest_char(path + "/data.txt") == ")"


def test_count_punctuation_chars():
    assert count_punctuation_chars("data.txt") == 5305


def test_count_non_ascii_chars():
    assert count_non_ascii_chars("data.txt") == 84


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char("data.txt") == "—"
