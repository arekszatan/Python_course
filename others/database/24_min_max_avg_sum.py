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

    # Zapytania SQL z użyciem MIN, MAX, AVG, SUM
    cursor.execute("SELECT MIN(salary) FROM employees")
    min_salary = cursor.fetchone()[0]

    cursor.execute("SELECT MAX(salary) FROM employees")
    max_salary = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(salary) FROM employees")
    avg_salary = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(salary) FROM employees")
    sum_salary = cursor.fetchone()[0]

    print(f"Minimalne wynagrodzenie: {min_salary}")
    print(f"Maksymalne wynagrodzenie: {max_salary}")
    print(f"Średnie wynagrodzenie: {avg_salary:.2f}")
    print(f"Suma wszystkich wynagrodzeń: {sum_salary}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
