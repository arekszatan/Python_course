import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Dane do połączenia z bazą danych PostgreSQL
host = "127.0.0.1"
user = "postgres"
password = "test123"
database = "py_test"# Łączymy się z bazą domyślną, aby stworzyć nową bazę danych

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=database
    )
    cursor = connection.cursor()

    # Aktualizacja wszystkich rekordów
    update_query_all = """
    UPDATE employees
    SET position = 'Senior Manager'
    """
    cursor.execute(update_query_all)

    update_query_single = """
    UPDATE employees
    SET position = 'Lead Developer'
    WHERE id = 1
    """
    cursor.execute(update_query_single)

    # Zatwierdzanie zmian
    connection.commit()

    print("Rekordy zostały zaktualizowane w tabeli 'employees'")


except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    # Zawsze zamykaj połączenie i kursor, aby zwolnić zasoby
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
