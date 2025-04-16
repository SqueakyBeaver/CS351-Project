import dbcfg

if dbcfg.db_conn.is_connected():
    print("Database is connected and configured")
else:
    print("Database not connected. Ohno")
