import psycopg2

host = "127.0.0.1"
user = "postgres"
password = "test123"
database = "py_test"

connection = None
cursor = None
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = connection.cursor()

    # Zapytanie SQL z użyciem AS do nadania aliasów
    cursor.execute("SELECT first_name AS \"First Name\", last_name AS \"Last Name\" FROM employees")
    records = cursor.fetchall()

    print("Imiona i nazwiska pracowników:")
    for row in records:
        first_name, last_name = row
        print(f"First Name: {first_name}, Last Name: {last_name}.")
except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
