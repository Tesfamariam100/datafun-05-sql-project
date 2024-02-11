"""
Python script to perform SQL operations on the database.
This script executes various SQL statements and queries,
including table creation, data insertion, update, deletion,
and querying with filters, sorting, and joins.
"""
import sqlite3
import logging
import os

# Configure logging
logging.basicConfig(filename='sql_operations_log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

def execute_sql_from_file(db_filepath, sql_file):

#Execute SQL commands from a file.
    try:
        with sqlite3.connect(db_filepath) as conn:
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed SQL from {sql_file}")
    except sqlite3.Error as e:
        logging.error(f"Error executing SQL from {sql_file}: {e}")

def main():
    # Define the database file path
    db_filepath = os.path.join(os.getcwd(), 'library.db')

    # Define the path to the SQL directory
    sql_dir = os.path.join(os.getcwd(), 'sql')

    # Execute SQL operations
    execute_sql_from_file(db_filepath, os.path.join(sql_dir, 'create_tables.sql'))
    execute_sql_from_file(db_filepath, os.path.join(sql_dir, 'insert_records.sql'))
    execute_sql_from_file(db_filepath, os.path.join(sql_dir, 'update_records.sql'))
    execute_sql_from_file(db_filepath, os.path.join(sql_dir, 'delete_records.sql'))
    execute_sql_from_file(db_filepath, os.path.join(sql_dir, 'query_aggregation.sql'))
    execute_sql_from_file(db_filepath, os.path.join(sql_dir, 'query_filter.sql'))
    execute_sql_from_file(db_filepath, os.path.join(sql_dir, 'query_sorting.sql'))
    execute_sql_from_file(db_filepath, os.path.join(sql_dir, 'query_group_by.sql'))
    execute_sql_from_file(db_filepath, os.path.join(sql_dir, 'query_join.sql'))

    logging.info("All SQL operations completed successfully")

if __name__ == "__main__":
    main()
