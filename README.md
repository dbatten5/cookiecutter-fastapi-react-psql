# Modern FastAPI Cookiecutter

A modern cookiecutter template to get started with a FastAPI + React + Postgres project.

## Installation

You'll first need to have `python3` and cookiecutter installed:

```bash
pip3 install --user cookiecutter
# or
pipx install cookiecutter
```

Then to install this cookiecutter:

```bash
cookiecutter https://github.com/dbatten5/cookiecutter-fastapi-react-psql
```

## Objectives

- Sane defaults.
- Minimal boilerplate.
- Useful packages installed for both dev and production.

## Features

- A dev environment compliant with modern standards, eg. `flake8`, `eslint` etc.
- Run dev environment locally (backend in a virtual environment) for faster development
  cycle and easy integration with code editors.
- Production ready deployment with `docker-compose` and `nginx`.
- Modern `react` app with `Typescript` made with `create-react-app` on the frontend.
- Github actions CI for building docker images and testing, and dependabot config to
  keep project dependencies up to date.
- `pytest` ready to go with sample test.
- `ormar` installed for a `django`-flavoured `python` async ORM.

## Licence

MIT
