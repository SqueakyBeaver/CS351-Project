import json
import argon2

import mysql.connector
from mysql.connector import errorcode


def _init_connection(_dbname: str | None = None) -> mysql.connector.MySQLConnection:
    """
    Initiate a database connection, configured via a JSON file

    :param _dbname: Optional name of database to use for all operations \n
    (mainly used for testing)
    :type _dbname: Optional[str]
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
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {_dbname or dbname}")
        cursor.execute(f"USE {_dbname or dbname}")
    except mysql.connector.DatabaseError as e:
        print(f"Something went wrong while trying to create/use the database: {e}")

    db_conn.commit()
    db_conn.autocommit = True
    return db_conn


def _generate_logins() -> list[tuple[str, str]]:
    usernames: list[str] = ["FlippantCarp84", "NobleGar37", "ChickenNugget9", "joem1997", "1c1cl3"]
    # Not meant to be secure, please don't use these
    passwords: list[str] = [
        "supersecurepassword",
        "correcthorsebatterystaple",
        "hotdog",
        "19970806",
        "3xfa#ggrsH884@fCdx",
    ]

    users: list[tuple[str, str]] = []
    hasher = argon2.PasswordHasher()

    for u, p in zip(usernames, passwords):
        users.append((u, hasher.hash(p)))
    
    return users


def _populate_db(connection: mysql.connector.MySQLConnection):
    """
    Populate the connected database with the contents of CFG.sql
    """
    cursor = connection.cursor()

    with open("CFG.sql", "r") as db_init:
        # The file starts with a use command, and we don't really want that
        _ = db_init.readline()

        statement = ""
        skipped = False
        for i in db_init:
            if "CREATE TABLE" in i:
                i = i.replace("CREATE TABLE", "CREATE TABLE IF NOT EXISTS")
            statement += i
            if ";" not in i:
                continue
            try:
                cursor.execute(statement)
            except mysql.connector.IntegrityError as e:
                if e.errno == errorcode.ER_DUP_ENTRY:
                    skipped = True
            finally:
                statement = ""

        if skipped:
            print("Skipped some duplicate entries (this is okay)")

    for username, hash in _generate_logins():
        try:
            cursor.execute("INSERT INTO User VALUES (%s, %s)", params=[username, hash])
        except:
            pass
        

db_conn = _init_connection()
_populate_db(db_conn)
