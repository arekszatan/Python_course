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

    # Dodanie pracownika i zwrócenie jego ID
    insert_query = """
    INSERT INTO employees (first_name, last_name, position, salary)
    VALUES ('Jan', 'Nowak', 'Developer', 5000)
    RETURNING id
    """

    cursor.execute(insert_query)
    new_employee_id = cursor.fetchone()[0]

    print(f"Id nowo dodanego pracownika: {new_employee_id}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
