FROM python:3.9.6-alpine

WORKDIR /usr/src/lomax

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install pipenv
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/lomax/entrypoint.sh
RUN chmod +x /usr/src/lomax/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/lomax/entrypoint.sh"]
