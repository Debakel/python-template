# 🍪 Copier Python Template

A [Copier](https://copier.readthedocs.io/en/stable/)  template for a Python package.

## Features
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Formatting, linting and import sorting with [Ruff](https://docs.astral.sh/ruff/)
- Static typing with [mypy](http://mypy-lang.org/)
- Git hooks that run all the above with [pre-commit](https://pre-commit.com/)
- Deployment ready with [Docker](https://docker.com/)
- Continuous Integration with [GitHub Actions](https://github.com/features/actions)
- Architecture decisions documented in an [Architecture Decision Record](https://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions)


## Getting started 🚀
### Prerequisites
To use this template, first [install `copier`](https://github.com/copier-org/copier?tab=readme-ov-file#installation):
```
pip install pipx
pipx install copier
```

### Usage
Once `copier` is installed, generate a new python project with:


```
copier copy https://github.com/Debakel/python-template.git --trust
```
