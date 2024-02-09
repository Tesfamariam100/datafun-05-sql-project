# datafun-05-sql-project
Datafun-05-sql-project: Integrating Python and SQL for database interactions and analytics.

## Project Structure
- **GitHub Repository**: datafun-05-sql
- **Documentation**: README.md
- **Initialize Script**: db_initialize_tesfamariam.py
- **Operations Script**: db_operations_tesfamariam.py

## External Dependencies
This project requires the following external modules, so it's recommended to use a virtual environment:
- pandas
- pyarrow

## Environment Setup
1. Clone the GitHub repository to your local machine.
2. Set up a Python virtual environment for the project.
   - On Windows:
     ```
     py -m venv .venv
     .\.venv\Scripts\activate
     py -m pip install -r requirements.txt
     ```
   - On macOS/Linux:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     python3 -m pip install -r requirements.txt
     ```
3. Create a `.gitignore` file to exclude unnecessary files and directories.
.venv/
.vscode/

4. Install required dependencies and record them in `requirements.txt`.

py -m pip freeze > requirements.txt


## Python Scripts
- **db_initialize_tesfamariam.py**: Script for initializing the database schema and populating it with initial data.
- **db_operations_tesfamariam.py**: Script for performing various SQL operations on the database.

## Logging
- Configure logging to write to a file named `log.txt`.
- Log important program events, such as the start and end of the program, exceptions, and major functions.

## Schema Design and Database Creation
- Design a schema with at least two related tables, including foreign key constraints.
- Implement a Python script to create the database, create the tables, and populate them with data.

## SQL Operations
- Implement SQL statements and queries for data manipulation and retrieval.
- Include SQL files for creating tables, inserting records, updating records, deleting records, and performing queries (aggregation, filtering, sorting, grouping, joining).

## Python and SQL Integration
- Use Python to interact with the SQL database and execute SQL commands.
- Define a main() function in the operations script to execute SQL operations logic.

## Conditional Script Execution
- Ensure the main function only executes when the script is run directly, not when imported as a module.

## Documentation and Contributions
- Document your project workflow, commands, and structure in the README.md file.
- Contributions and suggestions for improvement are welcome. Open issues or submit pull requests as needed.
