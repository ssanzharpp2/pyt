import psycopg2
from config import load_config
import csv

def insert_from_csv(filename):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    if not row or len(row) < 2:
                        continue
                    try:
                        cur.execute("INSERT INTO PhoneBook (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
                    except Exception as e:
                        print("Error:", e)
                conn.commit()

def main():
    insert_from_csv('C:/Users/Admin/work/lab10/task1/samp.csv')

if __name__ == '__main__':
    main()
    