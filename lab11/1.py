import psycopg2
from config import load_config

def pattern(cur, conn):
    pat = input("Write a pattern: ")
    query = """
    SELECT id, name, phone FROM phonebook
    WHERE name ILIKE %s OR phone ILIKE %s;
    """
    cur.execute(query, (f"%{pat}%", f"%{pat}%"))
    return cur.fetchall()

def main():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            pattern(cur, conn)

if __name__ == '__main__':
    main()