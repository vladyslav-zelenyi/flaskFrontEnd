# syntax=docker/dockerfile:1
FROM python:3.11-alpine
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
RUN apk add --no-cache gcc musl-dev linux-headers

WORKDIR /app
COPY . .
RUN pip install poetry
RUN pip install python-dotenv
RUN poetry config virtualenvs.create false && poetry install
EXPOSE 5000
CMD [ "flask", "run" ]
