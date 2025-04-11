import psycopg2
from config import load_config


def update_data(cur, conn):
    field = input("What you need to update (name/phone): ")
    old_value = input("Wraite current value: ")
    new_value = input("Write new value: ")

    try:
        if field == 'name':
            cur.execute("UPDATE PhoneBook SET first_name = %s WHERE first_name = %s", (new_value, old_value))
        elif field == 'phone':
            cur.execute("UPDATE PhoneBook SET phone = %s WHERE phone = %s", (new_value, old_value))
        else:
            print("Impossible(write name or phone)")
            return
        conn.commit()
        print("Updated successfully")
    except Exception as e:
        print("Error:", e)
        conn.rollback()

def main():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            update_data(cur, conn)

if __name__ == "__main__":
    main()