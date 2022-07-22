FROM python:3.10.5-alpine as pybase

RUN apk --update add gcc make g++ zlib-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

# do pytest here.
FROM pybase as pytest

WORKDIR /app

COPY requirements.dev.txt .

RUN pip install -r requirements.dev.txt

COPY squirrel_core ./squirrel_core
COPY tests ./tests

RUN pytest -v -s tests

FROM pybase

COPY --from=pytest /app/squirrel_core .

CMD ["/usr/local/bin/uvicorn", "--host", "0.0.0.0", "--port", "8000", "squirrel_core:app"]