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

    # Zapytanie SQL z użyciem COUNT
    count_query = "SELECT COUNT(*) FROM employees"
    cursor.execute(count_query)

    # Pobieranie wyniku
    count_result = cursor.fetchone()
    total_employees = count_result[0]

    print(f"Łączna liczba pracownikóœ: {total_employees}")


except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
