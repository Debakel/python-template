# 🍪 Python Cookie Cutter

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a Python package.

## Features
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Formatting, linting and import sorting with [Ruff](https://docs.astral.sh/ruff/)
- Static typing with [mypy](http://mypy-lang.org/)
- Git hooks that run all the above with [pre-commit](https://pre-commit.com/)
- Deployment ready with [Docker](https://docker.com/)
- Continuous Integration with [GitHub Actions](https://github.com/features/actions)

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

    pip install -U cookiecutter

Generate a Python package project:

    cookiecutter gh:Debakel/python-cookiecutter

Or, with `pipx` installed:

    pipx run cookiecutter gh:Debakel/python-cookiecutter

**Then:**

    # Enter project directory
    cd <repo_name>
    
    # Initialise git repo
    git init
    
    # Install dependencies
    pipenv install --dev
    
    # Setup pre-commit and pre-push hooks
    pipenv run pre-commit install

