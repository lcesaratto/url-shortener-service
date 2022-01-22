ARG PYTHON_VER=3.9

FROM python:$PYTHON_VER as requirements-stage

WORKDIR /tmp

ARG POETRY_VER=1.1.12

RUN pip install --no-cache-dir poetry==$POETRY_VER

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

ARG PYTHON_VER=3.9

FROM python:$PYTHON_VER

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

COPY ./README.md /code/README.md

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
