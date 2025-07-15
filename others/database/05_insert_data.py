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

    # Dodawanie pojedyńczego rekordu do tabeli 'employee'
    insert_query_single = """
    INSERT INTO employees (first_name, last_name, birth_day, position)
    VALUES ('Jan', 'Kowalski', '1980-01-01', 'Manager')
    """
    cursor.execute(insert_query_single)

    # Dodawanie wielu rekordów za jednym razem
    employee_to_insert = [
        ('Anna', 'Nowak', '1990-05-05', 'Developer'),
        ('Piotr', 'Wiśniewski', '1985-07-09', 'Analyst'),
        ('Ewa', 'Maj', '1992-03-15', 'Designer')
    ]

    # Dodawanie wielu rekordów za jednym razem
    insert_query_multiple = """
    INSERT INTO employees (first_name, last_name, birth_day, position)
    VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(insert_query_multiple, employee_to_insert)

    # Zatwierdzanie zmian
    connection.commit()

    print("Rekordy zostały dodane do tabeli 'employees'")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    # Zawsze zamykaj połączenie i kursor, aby zwolnić zasoby
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
