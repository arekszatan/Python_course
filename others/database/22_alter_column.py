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

    # Modyfikacja kolumny 'salary' na typ INTEGER
    alter_column_query = "ALTER TABLE employees ALTER COLUMN salary TYPE INTEGER"
    cursor.execute(alter_column_query)

    # Pobieranie danych po modyfikacji
    cursor.execute("SELECT id, first_name, salary FROM employees")
    records = cursor.fetchall()

    print("Dane z tabeli 'employees' po zmianie typu kolumny 'salary':")
    for row in records:
        print(row)

    connection.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
