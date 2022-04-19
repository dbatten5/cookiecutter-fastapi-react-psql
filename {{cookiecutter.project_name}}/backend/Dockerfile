ARG APP_DIRECTORY=/{{cookiecutter.project_slug}}
ARG ARG_POETRY_VERSION=1.1.11
ARG PYTHON_VERSION=3.9.7

FROM python:${PYTHON_VERSION}-slim as python-base

ARG APP_DIRECTORY
ARG ARG_POETRY_VERSION

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get autoclean && \
    apt-get autoremove && \
    apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/*

# Set configuration
# python
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=${ARG_POETRY_VERSION} \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

##############################################################################
# This stage is used to install dependencies and create the environment
##############################################################################
FROM python-base as builder-base

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    # deps for installing poetry
    curl \
    # deps for building python deps
    build-essential

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# copy project requirement files here to build env without depending on app code
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock* ./pyproject.toml ./

# Install runtime dependencies - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-dev

##############################################################################
# CI/Development
##############################################################################
FROM python-base as development

ARG APP_DIRECTORY

# Set the working directory
WORKDIR $PYSETUP_PATH

# copy in our built poetry + venv
COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# Run poetry install again to install the dev dependencies
RUN poetry install

# Will become mountpoint of our code
WORKDIR ${APP_DIRECTORY}

# Copy project source into the working directory
COPY . .

# Webserver will be running on this port
EXPOSE {{cookiecutter.backend_port}}

##############################################################################
# Production
##############################################################################
FROM python-base as production

ARG APP_DIRECTORY

# Set the working directory
WORKDIR ${APP_DIRECTORY}

COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# Copy project source into the working directory
COPY . .

# Webserver will be running on this port
EXPOSE {{cookiecutter.backend_port}}
