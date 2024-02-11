"""
Python and SQL Project: db_operations_tesfamariam.py

This script contains the main logic for SQL operations, including database initialization,
data insertion, updating records, deleting records, and various querying operations.

Author: Tesfamariam
Date: 2024-02-08

Usage:
- Ensure the database is initialized using db_initialize_tesfamariam.py before running this script.
- Make sure to review and adjust the SQL queries as needed for your specific project requirements.
"""

import sqlite3
import logging
import pandas as pd
from pathlib import Path

# Configure logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Program started") 

# Define the database file path
db_file = Path.cwd() / "library.db"

def create_database():
    """Create SQLite database."""
    try:
        conn = sqlite3.connect(db_file)
        logging.info("Database created successfully.")
        return conn
    except sqlite3.Error as e:
        logging.error("Error creating the database: %s", e)
        raise

def create_tables(conn):
    """Create tables in the database."""
    try:
        with conn:
            sql_file = Path("create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
        logging.info("Tables created successfully.")
    except sqlite3.Error as e:
        logging.error("Error creating tables: %s", e)
        raise

def insert_data_from_csv(conn):
    """Insert data from CSV files into tables."""
    try:
        with conn:
            author_data_path = Path("data", "authors.csv")
            book_data_path = Path("data", "books.csv")
            authors_df = pd.read_csv(author_data_path)
            books_df = pd.read_csv(book_data_path)
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
        logging.info("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        logging.error("Error inserting data: %s", e)
        raise

def main():
    try:
        conn = create_database()
        create_tables(conn)
        insert_data_from_csv(conn)
        logging.info("All SQL operations completed successfully")
    except Exception as e:
        logging.error("An error occurred during SQL operations: %s", e)
    finally:
        if conn:
            conn.close()
            logging.info("Database connection closed.")

if __name__ == "__main__":
    main()
    print("Database updated successfully.")

