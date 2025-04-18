import psycopg2
from config import load_config

def drop():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE phonebook;")

if __name__ == "__main__":
    drop()