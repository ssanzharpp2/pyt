import psycopg2
from config import load_config

def query_data(cur):
    filter_type = input("Filter by name or phone (name/phone): ")
    value = input("Write a value: ")
    if filter_type == "name":
        cur.execute("SELECT * FROM PhoneBook WHERE first_name ILIKE %s", ('%' + value + '%',))
    elif filter_type == "phone":
        cur.execute("SELECT * FROM PhoneBook WHERE phone LIKE %s", ('%' + value + '%',))
    else:
        print("Impossible(write name or phone)")
        return
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            query_data(cur)


if __name__ == "__main__":
    main()