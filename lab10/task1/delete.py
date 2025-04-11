import psycopg2
from config import load_config

def delete_entry(cur, conn):
    choice = input("Delete by name or phone (name/phone): ")
    value = input("Write a value: ")
    if choice == "name":
        cur.execute("DELETE FROM PhoneBook WHERE first_name = %s", (value,))
    elif choice == "phone":
        cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (value,))
    else:
        print("Impossible(write name or phone)")
        return
    conn.commit()

def main():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            delete_entry(cur, conn)

if __name__ == '__main__':
    main()