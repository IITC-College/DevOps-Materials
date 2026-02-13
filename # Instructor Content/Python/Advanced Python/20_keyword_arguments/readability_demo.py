#!/usr/bin/env python3
# Keyword arguments improve readability

def create_database_connection(host, port, username, password, database, timeout):
    print(f"Connecting to {database} at {host}:{port}")
    print(f"User: {username}, Timeout: {timeout}s")

# Without keyword arguments - hard to understand
create_database_connection("localhost", 5432, "admin", "secret", "mydb", 30)

print("---")

# With keyword arguments - much clearer!
create_database_connection(
    host="localhost",
    port=5432,
    username="admin",
    password="secret",
    database="mydb",
    timeout=30
)
