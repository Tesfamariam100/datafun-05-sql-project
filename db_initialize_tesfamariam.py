"""
Python and SQL Project: db_initialize_tesfamariam.py

This script initializes the database schema and populates it with initial data for the project.

Author: Tesfamariam
Date: 2023-09-02

Usage:
- Run this script to create the database schema and populate it with initial data.
- Make sure to review and adjust the SQL queries as needed for your specific project requirements.
"""

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Define SQL statements to create tables
create_authors_table = """
CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER PRIMARY KEY,
    author_name TEXT NOT NULL
);
"""

create_books_table = """
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    book_title TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors (author_id)
);
"""

# Execute SQL statements to create tables
cursor.execute(create_authors_table)
cursor.execute(create_books_table)

# Read data from CSV files using pandas
authors_df = pd.read_csv('data/authors.csv')
books_df = pd.read_csv('data/books.csv')

# Insert data into the tables
authors_df.to_sql('authors', conn, if_exists='append', index=False)
books_df.to_sql('books', conn, if_exists='append', index=False)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database initialized successfully.")

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Alter the authors table to add a new column
alter_table_query = """
ALTER TABLE authors
ADD COLUMN author_email TEXT;
"""

# Execute the ALTER TABLE statement
cursor.execute(alter_table_query)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()



