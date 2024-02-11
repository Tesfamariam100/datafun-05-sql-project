import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Open the SQL file
with open('create_tables.sql', 'r') as sql_file:
    sql_script = sql_file.read()

# Execute the SQL script
cursor.executescript(sql_script)

# Commit changes and close connection
conn.commit()
conn.close()
