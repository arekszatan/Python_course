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

    # Zapytanie SQL z użyciem GROUP BY
    # użyjemy GROUP BY do zgrupowania pracowników z tabeli employees według ich stanowiska
    group_by_query = """
    SELECT position, AVG(salary) AS average_salary
    FROM employees
    GROUP BY position
    """
    cursor.execute(group_by_query)
    records = cursor.fetchall()

    print("Średnie wynagrodzenie dla każdego stanowiska:")
    for row in records:
        print(f"Stanowisko: {row[0]}. Średnie wynagrodzenie: {row[1]:.2f}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
