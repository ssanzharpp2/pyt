import psycopg2
from config import load_config

def pagination(cur, conn):
    offset = input("Write initial row: ")
    limit = input("Write a number of rows: ")
    cur.execute("""
        SELECT id, first_name, phone FROM phonebook
        ORDER BY id
        LIMIT %s OFFSET %s
    """, (limit, offset))
    return cur.fetchall()

def main():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            pagination(cur, conn)

if __name__ == "__main__":
    main()