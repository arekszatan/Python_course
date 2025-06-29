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

    # Rozszerzenie tabeli 'employee' o dodatkowe kolumny
    alter_table_query = """
    ALTER TABLE employee
    ADD COLUMN email VARCHAR(100) default 'unknown@email.com',
    ADD COLUMN salary DECIMAL DEFAULT 0.0
    """
    cursor.execute(alter_table_query)

    # Aktualizacja niektórych rekordów
    update_records_query = """
    UPDATE employee
    SET email = 'anna.kowalska@example.com', salary = 5000.00
    WHERE id = 2
    """
    cursor.execute(update_records_query)

    # Zatwierdzanie zmian
    connection.commit()

    # Wyświetlanie zaktualizowanych danych rekordów
    select_query = """
    SELECT * FROM employee
    """
    cursor.execute(select_query)
    records = cursor.fetchall()

    print("Zaktualizowane dane z tabeli 'employee'")
    for row in records:
        print(row)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    # Zawsze zamykaj połączenie i kursor, aby zwolnić zasoby
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
