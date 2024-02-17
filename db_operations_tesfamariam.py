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

#This python program is responsible for sql script executions and modifications

# Imports
from pathlib import Path
import pandas as pd
import pathlib
import logging
import sqlite3
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

def main():from pathlib import Path

# Define the directory path
directory_path = Path("C:/Users/Tesfamariam/datafun-05-sql-project")

# Join the directory path with the filename to get the full file path
db_filepath = directory_path / "library.db"

# Convert the path to string if needed
db_filepath_str = str(db_filepath)

# Now, db_filepath contains the full path to the "library.db" file
print(db_filepath_str)

    
db_filepath = pathlib.Path("C:/Users/Tesfamariam/datafun-05-sql-project")
execute_sql_from_file(db_filepath, 'C:/Users/blehman/Projects/datafun-05-sql/sql_file/insert_records.sql')
execute_sql_from_file(db_filepath, 'C:/Users/blehman/Projects/datafun-05-sql/sql_file/update_records.sql')
execute_sql_from_file(db_filepath, 'C:/Users/blehman/Projects/datafun-05-sql/sql_file/delete_records.sql')
execute_sql_from_file(db_filepath, 'C:/Users/blehman/Projects/datafun-05-sql/sql_file/query_aggregation.sql')
execute_sql_from_file(db_filepath, 'C:/Users/blehman/Projects/datafun-05-sql/sql_file/query_filter.sql')
execute_sql_from_file(db_filepath, 'C:/Users/blehman/Projects/datafun-05-sql/sql_file/query_sorting.sql')
execute_sql_from_file(db_filepath, 'C:/Users/blehman/Projects/datafun-05-sql/sql_file/query_group_by.sql')
execute_sql_from_file(db_filepath, 'C:/Users/blehman/Projects/datafun-05-sql/sql_file/query_join.sql')

logging.info("All SQL operations completed successfully")

if __name__ == "__main__":     main()
