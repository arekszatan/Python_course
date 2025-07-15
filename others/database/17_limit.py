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

    print("Pierwsze 3 rekordy z tabeli 'employees'")
    cursor.execute("SELECT * FROM employees LIMIT 3")
    for row in cursor.fetchall():
        print(row)

    print("\nMaksymalnie 2 rekordy menedżeróœ z wynagrodzeniem powyżej 4000:")
    cursor.execute("SELECT * FROM employees WHERE salary > 4000 LIMIT 2")
    for row in cursor.fetchall():
        print(row)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
