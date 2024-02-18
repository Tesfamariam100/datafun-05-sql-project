import sqlite3
import logging
import pandas as pd
from pathlib import Path

# Configure logging
logging.basicConfig(filename='sql_operations_log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Program started")
# Define the database file path
db_file = Path.cwd() / "library.db"


def execute_sql_from_file(db_file, sql_file):
    """Function to execute SQL commands from a file."""
    try:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        with sqlite3.connect(db_file) as conn:
            conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")
        logging.info(f"Executed SQL from {sql_file}")
    except sqlite3.Error as e:
        print(f"Error executing SQL from {sql_file}: {e}")
        logging.error(f"Error executing SQL from {sql_file}: {e}")

def main():
    try:
        directory_path = Path('c:/Users/Tesfamariam/datafun-05-sql-project/')
        db_filepath = directory_path / "library.db"

        # Specify the correct path for SQL file
        db_files = [
            'insert_records.sql',
            'update_records.sql',
            'delete_records.sql',
            'query_aggregation.sql',
            'query_filter.sql',
            'query_sorting.sql',
            'query_group_by.sql',
            'query_join.sql'
        ]

        for sql_file in db_files:
            execute_sql_from_file(db_filepath, sql_file)

        logging.info("All SQL operations completed successfully")

    except Exception as e:
        print(f"An exception occurred: {e}")
        logging.error(f"An exception occurred: {e}")

if __name__ == "__main__":
    main()
