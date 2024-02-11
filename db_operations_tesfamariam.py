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
import pandas as pd
import pathlib

# Define the database file path
db_file = 'library.db'

# Connect to the SQLite database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Define SQL statements to create tables
create_authors_table = """
CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER PRIMARY KEY,
    author_name TEXT NOT NULL,
    author_email TEXT,
    author_country TEXT
);
"""

create_books_table = """
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    book_title TEXT NOT NULL,
    book_genre TEXT,
    book_published_date TEXT,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors (author_id)
);
"""

# Execute SQL statements to create tables
cursor.execute(create_authors_table)
cursor.execute(create_books_table)

# Load data from CSV files
authors_df = pd.read_csv('data/authors.csv')
books_df = pd.read_csv('data/books.csv')

# Insert data into tables
authors_df.to_sql('authors', conn, if_exists='replace', index=False)
books_df.to_sql('books', conn, if_exists='replace', index=False)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database updated successfully.")
