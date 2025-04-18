import psycopg2
from pconfig import load_config


def create_tables():
    commands = [
        """
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
        );
        """
        """
        CREATE TABLE IF NOT EXISTS user_score (
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
        level INTEGER NOT NULL,
        score INTEGER NOT NULL,
        saved_at TIMESTAMP DEFAULT NOW(),
        PRIMARY KEY (user_id)
        );
        """
    ]
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()
