# db_initialize_tesfamariam.py

import sqlite3
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Program started") 

def create_database():
    conn = sqlite3.connect('library.db')
    conn.close()

def create_tables():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        with open('create_tables.sql', 'r') as file:
            sql_script = file.read()
        cursor.executescript(sql_script)
        logging.debug("Tables created successfully")

def insert_data_from_csv():
    try:
        conn = sqlite3.connect('library.db')
        authors_df = pd.read_csv('data/authors.csv')
        books_df = pd.read_csv('data/books.csv')
        authors_df.to_sql('authors', conn, if_exists='append', index=False)
        books_df.to_sql('books', conn, if_exists='append', index=False)
        logging.debug("Data inserted successfully")
    except Exception as e:
        logging.exception(f"Error occurred while inserting data: {e}")
    finally:
        conn.close()

def main():
    create_database()
    create_tables()
    insert_data_from_csv()
    logging.info("Program ended")

if __name__ == "__main__":
    main()
