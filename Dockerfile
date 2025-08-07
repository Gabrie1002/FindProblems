FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install poetry --no-cache-dir && \
    poetry config virtualenvs.create false && \
    poetry install --only main

ENV PATH="/usr/local/bin:$PATH"

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.wsgi:app", "--workers", "4"]