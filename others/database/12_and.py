import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import random
import datetime

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

    for _ in range(5):
        first_name = f"Imię_{random.randint(1, 100)}"
        last_name = f"Nazwisko_{random.randint(1, 100)}"
        birth_day = datetime.date(1990, 1, 1) + datetime.timedelta(days=random.randint(1, 10000))
        position = random.choice(['Developer', 'Manager', 'Analyst'])
        salary = round(random.uniform(3000, 7000), 2)

        insert_query = """
        INSERT INTO employees (first_name, last_name, birth_day, position, salary)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (first_name, last_name, birth_day, position, salary))

    # Zapytanie z użyciem AND
    select_query_and = """
    SELECT * FROM employees
    WHERE position = 'Developer' AND salary > 5000
    """
    cursor.execute(select_query_and)
    records = cursor.fetchall()
    print("Pracownicy na stanowisku 'Developer' z pensją powyżej 5000")
    for row in records:
        print(row)

    # Zapytanie z użyciem podwójnego AND
    select_query_double_and = """
    SELECT * FROM employees
    WHERE position = 'Manager' AND salary > 4000 AND birth_day > '1990-01-01'
    """
    cursor.execute(select_query_double_and)
    records = cursor.fetchall()
    print("Pracownicy na stanowisku 'Manager' z pensją powyżej 4000 i urodzeni po 1990-01-01")
    for row in records:
        print(row)

    # Zatwierdzanie zmian
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
