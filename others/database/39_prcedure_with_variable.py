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

    # Tworzenie tabeli 'employees'
    cursor.execute("""
    DROP TABLE IF EXISTS employees;
    CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
    );
    """)

    # Dodawanie danych do tabeli 'employee'
    cursor.execute("""
    INSERT INTO employees (name)
    VALUES ('Jan Kowalski'), ('Anna Nowak');
    """)

    # Tworzenie procedury składowanej
    cursor.execute("""
    CREATE OR REPLACE FUNCTION count_employees()
    RETURNS INTEGER AS $$
    DECLARE 
        emp_count INTEGER;
    BEGIN
        SELECT COUNT(*) INTO emp_count FROM employees;
        RETURN emp_count;
    END;
    $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlanie wyniku
    cursor.callproc("count_employees")
    count = cursor.fetchone()[0]
    print(f"Liczba pracowników: {count}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
