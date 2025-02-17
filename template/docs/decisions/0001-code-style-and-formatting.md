# Python Code Style

## Status

Accepted

## Context

Having consistent formatting is a great thing.

## Decision

Therefore, we agree to use [pre-commit](https://pre-commit.com/) together with [Ruff](https://docs.astral.sh/ruff/) to enforce a consistent and deterministic (!) code style, conformity with [PEP8](https://peps.python.org/pep-0008/) and other code quality standards (see [pyproject.toml](see [pyproject.toml](../../pyproject.toml)).

We chose Ruff over [Black](https://github.com/psf/black) due to performance reasons.

## Consequences


The Ruff formatter is quite opinionated and does not support configuring code styles. *Some people may
not like that code style.* But we "will save time and mental energy for more important matters".

Code reviews get faster thanks to smaller diffs.
