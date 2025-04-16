import json

import mysql.connector

def _init_connection() -> mysql.connector.MySQLConnection:
    """
    Initiate a database connection, configured via a JSON file
    """
    try:
        with open("db_cfg.json", "r") as file:
            db_cfg = json.load(file)

    except FileNotFoundError:
        print("ERROR: Database config file not found. Creating default file...")

        with open("db_cfg.json", "w+") as file:
            db_cfg = {
                "host": "127.0.0.1",
                "user": "",
                "password": "",
            }
            json.dump(db_cfg, file)
    try:
        dbname = db_cfg.pop("database")
    except KeyError:
        dbname = "351_group9"

    db_conn = mysql.connector.MySQLConnection(**db_cfg)

    cursor = db_conn.cursor()

    # Note: using %s to properly sanitize inputs does 
    # not work with table, column, database, etc. names
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbname}")
        cursor.execute(f"USE {dbname}")
    except mysql.connector.DatabaseError as e:
        print(f"Something went wrong while trying to create/use the database: {e}")

    db_conn.commit()
    return db_conn

def _populate_db(connection: mysql.connector.MySQLConnection):
    """
    Populate the connected database with the contents of CFG.sql
    """
    cursor = connection.cursor()

    with open("CFG.sql", "r") as db_init:
        # The file starts with a use command, and we don't really want that
        _ = db_init.readline()
            
        statement = ""
        for i in db_init:
            if "CREATE TABLE" in i:
                i = i.replace("CREATE TABLE", "CREATE TABLE IF NOT EXISTS")
            statement += i
            if ";" not in i:
                continue
            print(statement)
            cursor.execute(statement)
            statement = ""
        
db_conn = _init_connection()

if __name__ == "__main__":
    _populate_db(db_conn)
