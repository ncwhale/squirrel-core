FROM python:3.10.5-alpine as build-3rd-party-libs

RUN apk --update add gcc make g++ zlib-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["/usr/local/bin/uvicorn", "--host", "0.0.0.0", "--port", "8000", "squirrel_core:app", "--reload"]