"""Tests names.py module."""

from names import sample, words


def test_names():
    # The first name should be acrobat.
    assert words[0] == "acrobat"

    # The last name should be yes.
    assert words[-1] == "yes"

    # There should be 1633 names.
    assert len(words) == 1633


def test_sample():
    # The first name with seed "" is known.
    assert sample(seed="", start=0, stop=1)[0] == "spirit"

    # Same seed should produce the same words.
    first = sample(seed="", start=0, stop=5)
    second = sample(seed="", start=0, stop=5)
    assert first == second

    # Different seed should return different words.
    first = sample(seed="1", start=0, stop=5)
    second = sample(seed="2", start=0, stop=5)
    assert first != second

    # Different slice should not change order of words.
    first = sample(seed="", start=0, stop=5)
    second = sample(seed="", start=2, stop=5)
    assert first[2:] == second

    # Names should be exhausted when slice goes beyond number of words.
    assert sample(seed="", start=len(words), stop=len(words) + 5) == []
