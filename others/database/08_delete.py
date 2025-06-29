import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Dane do połączenia z bazą danych PostgreSQL
host = "localhost"
user = "postgres"
password = "admin"
database = "py_test" # Łączymy się z bazą domyślną, aby stworzyć nową bazę danych

try:
    # Nawiązywanie połączenia z bazą danych
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=database
    )
    cursor = connection.cursor()

    # Identyfikator rekordu do usunięcia
    id_to_delete = 1

    # Zapytanie SQL do usunięcia rekordu z tabeli 'employee'
    delete_query = """
    DELETE FROM employee WHERE id = %s
    """
    cursor.execute(delete_query, (id_to_delete,))

    # Zatwierdzanie zmian
    connection.commit()

    print(f"Rekord o ID {id_to_delete} został usunięty z tabeli employee")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    # Zawsze zamykaj połączenie i kursor, aby zwolnić zasoby
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
