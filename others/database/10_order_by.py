import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Dane do połączenia z bazą danych PostgreSQL
host = "127.0.0.1"
user = "postgres"
password = "test123"
database = "py_test"
try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=database
    )
    cursor = connection.cursor()

    # Zapytanie SQL z użyciem ORDER BY do sortowania danych
    select_query = """
    SELECT id , first_name, last_name, salary FROM employees ORDER BY id DESC
    """
    cursor.execute(select_query)
    records = cursor.fetchall()

    print("Dane z tabeli 'employees' posortowane według wynagrodzenia id (malejąco):")
    for row in records:
        print(f"ID: {row[0]}, Imię: {row[1]}, Nazwisko: {row[2]}, Wynagrodzenie: {row[3]}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    # Zawsze zamykaj połączenie i kursor, aby zwolnić zasoby
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
