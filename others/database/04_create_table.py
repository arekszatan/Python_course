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

    # Zapytanie SQL do utworzenia nowej tabeli
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employee (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_day DATE,
    position VARCHAR(50)
    )
    """
    cursor.execute(create_table_query)

    # Zatwierdzenie zmian w bazie danych
    connection.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    # Zawsze zamykaj połączenie i kursor, aby zwolnić zasoby
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
