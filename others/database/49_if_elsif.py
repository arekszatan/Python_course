import psycopg2

host = "127.0.0.1"
user = "postgres"
password = "test123"
database = "postgres"

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

    # Stworzymy przykład procedury, która używa instrukcji if-elsif w PostgreSQL
    # i jest wywoływana za pomocą metody cursor.callproc, a następnie zwraca wynik.
    # Stworzymy prostą procedurę, która zlicza pracowników w różnych działach.

    # Tworzenie tabeli 'employees'
    cursor.execute("""
        DROP TABLE IF EXISTS employees;
        CREATE TABLE employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            department VARCHAR(50) NOT NULL
        );
    """)

    # Dodawanie danych do tabeli 'employees'
    cursor.execute("""
        INSERT INTO employees (name, department)
        VALUES
            ('Jan Kowalski', 'IT'),
            ('Anna Nowak', 'HR'),
            ('Piotr Zalewski', 'Marketing'),
            ('Ewa Maj', 'IT')
    """)

    # Tworzenie procedury składowanej
    cursor.execute("""
        CREATE OR REPLACE FUNCTION count_employees_by_department(dept VARCHAR)
        RETURNS INTEGER AS $$
        DECLARE
            count INTEGER;
        BEGIN
            IF dept = 'IT' THEN
                SELECT COUNT(*) INTO count FROM employees WHERE department = 'IT';
            ELSIF dept = 'HR' THEN
                SELECT COUNT(*) INTO count FROM employees WHERE department = 'HR';
            ELSE
                SELECT COUNT(*) INTO count FROM employees WHERE department = dept;
            END IF;
            RETURN count;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlanie wyniku
    cursor.callproc('count_employees_by_department', ('IT',))
    count = cursor.fetchone()[0]
    print(f" Ilośc pracowników w dziale IT: {count}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
