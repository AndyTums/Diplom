FROM python:3.12-slim

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

#FROM python:3.12-slim
#
#RUN pip install --no-cache-dir poetry
#
#WORKDIR /app
#
#COPY pyproject.toml poetry.lock ./
#RUN poetry install --no-root
#
#COPY . .
#
#EXPOSE 8000
#
#CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

#FROM python:3.12-slim
#WORKDIR /app
#RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
#COPY pyproject.toml poetry.lock ./
#RUN poetry install --no-dev # Установка без зависимостей для разработки

