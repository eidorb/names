# Names

An API for naming things


## Getting started

It's easy to start developing locally:

1. Install [uv](https://docs.astral.sh/uv/):

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
2. Clone this repository:

  ```bash
  git clone git@github.com:eidorb/names.git
  cd names
  ```
3. Generate some names:

  ```bash
  uv run -m names "seedy"
  gravity
  postage
  salary
  lobster
  garden
  ```
4. 🙇

uv will find, install and update a suitable Python interpreter and Python package dependencies as required. It's pretty fast.

Alternatively, you could activate a shell in the environment:

```bash
uv sync
source .venv/bin/activate
```

And run commands as usual:

```bash
(om-names) $ python -m names --help

 Usage: names.py [OPTIONS] [SEED]

 Generates a random sequence of names, seeded with SEED.
 Name things in your collection using the same SEED. Increase --offset as the collection grows. (You can name up to 1633 things.)

╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   seed      [SEED]  Use a fixed seed to ensure names are shuffled in the same order. It can be any value, even nothing. Just be sure to remember it.                                                            │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --count                     INTEGER             Returns this many names. [default: 5]                                                                                                                           │
│ --offset                    INTEGER             Skip over this many names. [default: 0]                                                                                                                         │
│ --format                    [text|python|json]  [default: text]                                                                                                                                                 │
│ --install-completion                            Install completion for the current shell.                                                                                                                       │
│ --show-completion                               Show completion for the current shell, to copy it or customize the installation.                                                                                │
│ --help                                          Show this message and exit.                                                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```


Deactivate when you're done:

```bash
(om-names) $ deactivate
$
```

Some command line poetry:

```bash
echo "write the most insightful and terse poem you can about the difficulties of " \
"naming things using these words:\n$(uv run -m names)" \
  | uvx llm -m grok-beta

In the spirit of naming, we embark,
A toga of words, a daunting task.
Concert of thoughts, a symphony of choice,
A period of struggle, a ranger's voice.
```


## Quick links

From the command line.

- Actions

  ```bash
  open "https://github.com/eidorb/${PWD##*/}/actions"
  ```
- Actions secrets

  ```bash
  open "https://github.com/eidorb/${PWD##*/}/settings/secrets/actions"
  ```
