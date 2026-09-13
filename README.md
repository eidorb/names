# Names

Generate deterministic duplicate-free mnemonic names.

![](image.jpeg)

Names are created from short, human-readable words. e.g., `melon-export` or
`extend-judge-machine-ritual`. Words come from Oren Tirosh's mnemonic encoding [project](https://web.archive.org/web/20090918202746/http://tothink.com/mnemonic/wordlist.html) (originally discovered in this [post](https://mnx.io/blog/a-proper-server-naming-scheme/) about server naming).

Given the same seed, words per name, and position, the same name is always returned.

## Usage

Generate names on a website: https://names.brodie.id.au

Generate names on the command line:

```console
$ git clone git@github.com:eidorb/names.git
$ cd names
$ python names.py "my seed"
city-memphis
diesel-deluxe
focus-yellow
julius-gordon
hostel-option
pardon-mayor
mouse-sailor
jacob-image
desert-owner
coral-ravioli
```

Configure words per name, count and starting position:

```console
$ python names.py "my seed" --n 4 --count 5 --start 7085131327670
lava-demand-meaning-sabrina
saint-sponsor-victor-paper
cheese-nixon-cadet-henry
rufus-hamlet-spray-viva
fiction-paper-mission-prefer
```

## How it works

For a given seed and word count, `names` treats every ordered selection of distinct words as a numbered namespace.
It uses a seeded permutation to shuffle that namespace, so any position can be generated directly without storing previous results or producing duplicates.
Then, a shuffled position is converted to a name using factoradic
unranking.

This provides

- deterministic output
- random access to very large namespaces
- no stored sequence or mutable state
- distinct words within each name
- no duplicate names within a namespace

## CLI help

```console
$ python names.py --help
usage: names.py [-h] [--n N] [--count COUNT] [--start START] seed

Generate deterministic unique mnemonic names.

positional arguments:
  seed           Seed that determines the ordering of names

options:
  -h, --help     show this help message and exit
  --n N          Number of words in each name (default: 2)
  --count COUNT  Number of names to generate (default: 10)
  --start START  Zero-based position of the first name (default: 0)
```
