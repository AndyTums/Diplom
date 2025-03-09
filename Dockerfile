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


#FROM python:3.12
#
## Configure Poetry
#ENV POETRY_VERSION=2.1.1
#ENV POETRY_HOME=/opt/poetry
#ENV POETRY_VENV=/opt/poetry-venv
#ENV POETRY_CACHE_DIR=/opt/.cache
#
## Install poetry separated from system interpreter
#RUN python3 -m venv $POETRY_VENV \
#	&& $POETRY_VENV/bin/pip install -U pip setuptools \
#	&& $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}
#
## Add `poetry` to PATH
#ENV PATH="${PATH}:${POETRY_VENV}/bin"
#
#WORKDIR /app
#
## Install dependencies
#COPY poetry.lock pyproject.toml ./
#RUN poetry install
#
## Run your app
#COPY . /app
#
#EXPOSE 8000
#
#CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

# Используем образ Python
FROM python:3.12

# Устанавливаем необходимые зависимости для Poetry
RUN pip install --upgrade pip && \
    pip install poetry

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы конфигурации Poetry
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости приложения
RUN poetry install --no-root

# Копируем остальные файлы проекта
COPY . .

# Запускаем ваше приложение (замените на вашу команду запуска)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]