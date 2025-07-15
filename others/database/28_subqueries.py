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

    # Zapytanie SQL z użyciem podzapytania
    # W tym przypadku, użyjemy podzapytania z tabeli employees
    # do znalezienia pracownikóœ, któ©ych wynagrodzenie jest wyższe niż średnie
    # wynagridzenie we wszystkich rekordach.
    subquery_query = """
    SELECT first_name, last_name, salary FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)
    """
    cursor.execute(subquery_query)
    records = cursor.fetchall()

    print("Pracownicy z wynagrodzeniem wyższym niż średnia w firmie:")
    for row in records:
        print(row)


except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
