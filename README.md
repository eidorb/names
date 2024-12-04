# Names

An API for naming things


## Getting started

It's easy to get started using [uv](https://docs.astral.sh/uv/):

<!-- TODO: update once package published to PyPI -->
```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh
$ git clone git@github.com:eidorb/names.git
$ cd names
$ uv run python -m names --seed "seedy"
gravity
postage
salary
lobster
garden
```

uv will install or update a suitable Python interpreter and Python packages dependencies as required.

Some command line poetry:

```bash
$ echo "generate a brief sorrowful poem using the following words:\n`uv run -m names --seed poetry --end 10`" | uvx llm -m grok-beta
In the land of Austria, where the mountains stand,
A sorrowful tale, a virus swept the land.
Like a rodeo, it rode through the towns,
Stamping its mark, leaving hearts with deep frowns.

The cover of night, no longer a shield,
As the granite of hope, began to yield.
Lava of despair, flowing through the streets,
A slogan of fear, in every heart it beats.

Colombo, the city, once vibrant and bright,
Now echoes with silence, a somber sight.
The sultan of health, now a distant dream,
As the world watches, with eyes that gleam.

In this time of trial, we stand together,
Hoping for a future, a world to weather.
```
