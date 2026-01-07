FROM python:3.11-slim

WORKDIR /Task2

COPY app.py /Task2/

# Install psycopg2 and any other dependencies
RUN pip install --no-cache-dir psycopg2-binary

CMD ["python", "app.py"]
