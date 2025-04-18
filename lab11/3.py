import psycopg2
from config import load_config

def many_users(cur, conn):
    s = input("Write name and number: ")
    lst = s.split(" ")
    for it in range(len(lst)):
        if it % 2 == 0:
            name = lst[it] 
            phone = lst[it + 1]
            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))

def main():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            many_users(cur, conn)

if __name__ == "__main__":
    main()