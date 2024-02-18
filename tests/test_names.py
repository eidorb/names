"""Tests names.py module."""

from names import names, sample_names


def test_names():
    # The first name should be acrobat.
    assert names[0] == "acrobat"

    # The last name should be yes.
    assert names[-1] == "yes"

    # There should be 1633 names.
    assert len(names) == 1633


def test_sample_names():
    # The first name with seed "" is known.
    assert sample_names(seed="", start=0, stop=1)[0] == "spirit"

    # Same seed should produce the same names.
    first = sample_names(seed="", start=0, stop=5)
    second = sample_names(seed="", start=0, stop=5)
    assert first == second

    # Different seed should return different names.
    first = sample_names(seed="1", start=0, stop=5)
    second = sample_names(seed="2", start=0, stop=5)
    assert first != second

    # Different slice should not change order of names.
    first = sample_names(seed="", start=0, stop=5)
    second = sample_names(seed="", start=2, stop=5)
    assert first[2:] == second

    # Names should be exhausted when slice goes beyond number of names.
    assert sample_names(seed="", start=len(names), stop=len(names) + 5) == []
