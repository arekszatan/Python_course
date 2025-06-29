import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Dane do połączenia z bazą danych PostgreSQL
host = "localhost"
user = "postgres"
password = "admin"
database = "postgres" # Łączymy się z bazą domyślną, aby stworzyć nową bazę danych

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=database
    )

    # Ustawienie poziomu izolacji na AUTOCOMMIT
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Utworzenie kursora
    cursor = connection.cursor()

    # Usuwanie bazy danych
    cursor.execute("DROP DATABASE IF EXISTS py_test2")

    print("Baza danych py_test2 została pomyślnie usunięta.")


except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    # Zawsze zamykaj połączenie i kursor, aby zwolnić zasoby
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
