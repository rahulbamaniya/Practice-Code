import os
import psycopg2
from psycopg2 import sql, OperationalError

# Read environment variables
db_host = os.environ.get("DB_HOST", "db")
db_user = os.environ.get("DB_USER", "postgres")
db_password = os.environ.get("DB_PASSWORD", "")
db_name = os.environ.get("DB_NAME", "testdb")

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        dbname=db_name
    )
    cursor = conn.cursor()
    cursor.execute("SELECT current_database();")
    current_db = cursor.fetchone()[0]
    print(f"Connected to database: {current_db}")
    cursor.close()
    conn.close()
except OperationalError as e:
    print(f"Error connecting to database: {e}")
