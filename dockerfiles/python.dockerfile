FROM python:3.9

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

ENV PROJECT_DIR /usr/local/src/app

WORKDIR ${PROJECT_DIR}

COPY Pipfile* ${PROJECT_DIR}/

RUN pipenv install --system --deploy
