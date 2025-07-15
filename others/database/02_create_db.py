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
    # Ustawiane poziomu izolacji na AUTOCOMMIT
    # Pozwala to na natychmiastowe wykonanie poleceń SQL bez konieczności wywołania
    # commit()
    # Jest to potrzebne, ponieważ niektóre polecenia, takie jak tworzenie baz danych,
    # muszą być wykonywane poza transakcją.
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # Utworzenie kursora
    cursor = connection.cursor()

    # Tworzenie nowej bazy danych
    cursor.execute("CREATE DATABASE py_test2")
    print("Baza danych py_test2 została pomyślnie utworzona.")


except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    # Zawsze zamykaj połączenie i kursor, aby zwolnić zasoby
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
