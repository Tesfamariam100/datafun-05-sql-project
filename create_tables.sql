-- create_tables.sql
-- create_tables.sql

CREATE TABLE IF NOT EXISTS authors (
    author_id INTEGER PRIMARY KEY,
    author_name TEXT,
    author_email TEXT
);

CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    book_title TEXT,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);
