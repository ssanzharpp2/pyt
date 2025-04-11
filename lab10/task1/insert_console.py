import psycopg2
from config import load_config

def insert_from_console(cur, conn):
    name = input("Name: ")
    phone = input("Your number: ")
    try:
        cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
    except Exception as e:
        print("Error:", e)
        conn.rollback()

def main():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            insert_from_console(cur, conn)

if __name__ == '__main__':
    main()