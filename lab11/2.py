import psycopg2
from config import load_config

def aau(cur, conn):
    name = input("Write name: ")
    phone = input("Write a phone: ")
    cur.execute("SELECT 1 FROM phonebook WHERE first_name = %s", (name,))
    if cur.fetchone():
        cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (phone, name))
    else:
        cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))

def main():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            aau(cur, conn)

if __name__ == '__main__':
    main()