"""Tests names.py module."""

import subprocess

from names import generate, permutations, sample, words


def test_words():
    """Tests the word list parses correctly."""
    # The first name should be acrobat.
    assert words[0] == "acrobat"

    # The last name should be yes.
    assert words[-1] == "yes"

    # There should be 1633 names.
    assert len(words) == 1633


def test_sample():
    """Tests random sampling of words."""
    # The first name with seed "" is known.
    assert sample(seed="", population=words, start=0, stop=1)[0] == "spirit"

    # Same seed should produce the same words.
    first = sample(seed="", population=words, start=0, stop=5)
    second = sample(seed="", population=words, start=0, stop=5)
    assert first == second

    # Different seed should return different words.
    first = sample(seed="1", population=words, start=0, stop=5)
    second = sample(seed="2", population=words, start=0, stop=5)
    assert first != second

    # Different slice should not change order of words.
    first = sample(seed="", population=words, start=0, stop=5)
    second = sample(seed="", population=words, start=2, stop=5)
    assert first[2:] == second

    # Names should be exhausted when slice goes beyond number of words.
    assert (
        sample(seed="", population=words, start=len(words), stop=len(words) + 5) == []
    )


def test_generate():
    """Tests generated sequences of names."""
    names = generate(seed="test", count=4, offset=1630)
    # Yes, these should be 1-length tuples as this is the general form.
    assert dict(names) == {1630: ("absorb",), 1631: ("textile",), 1632: ("brush",)}


def test_cli():
    """Tests output generated when invoked by CLI."""
    # Go nuclear and capture text output from subprocess.
    completed = subprocess.run(
        "python -m names test --count 4 --offset 1630 --format json".split(),
        capture_output=True,
        text=True,
    )
    # Keys should be strings in JSON output.
    assert (
        completed.stdout
        == """
{
  "1630": [
    "absorb"
  ],
  "1631": [
    "textile"
  ],
  "1632": [
    "brush"
  ]
}
"""
    )

    # Run help.
    completed = subprocess.run(
        "python -m names --help".split(),
        capture_output=True,
        text=True,
    )
    # Help text should be 'dynamic'.
    assert "2665056 things" in completed.stdout

    # Attempt --r > 2.
    completed = subprocess.run(
        "python -m names --r 3".split(),
        capture_output=True,
        text=True,
    )
    assert "Aborted." in completed.stderr

    # Test text output is hyphenated for --r=2.
    completed = subprocess.run(
        "python -m names --r 2 --format text".split(),
        capture_output=True,
        text=True,
    )
    assert (
        """
prosper-harmony
sherman-castro
flute-noise
village-block
graph-serial
"""
        == completed.stdout
    )


def test_permutations():
    # Default r=1.
    assert len(list(permutations())) == 1633

    # 2-word permutations.
    r2_permutations = list(permutations(2))
    assert len(r2_permutations) == 2665056
    assert ("acrobat", "africa") == r2_permutations[0]
    assert ("yes", "ski") == r2_permutations[-1]
