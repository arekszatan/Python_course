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

    # W tym przykładnie stowrzymy tabelę employees z kolumnami id, name, department i salary.
    # Następnie napiszemy procedurę, która aktualizuje wynagrodzenia pracowników w zależności
    # od ich działu.

    # Tworzenie tabeli 'employee'
    cursor.execute("""
        DROP TABLE IF EXISTS employees;
        CREATE TABLE employees (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            department VARCHAR(50) NOT NULL,
            salary DECIMAL(10, 2) NOT NULL
        );
    """)

    # Dodawanie danych do tabeli 'employees'
    cursor.execute("""
        INSERT INTO employees (name, department, salary)
        VALUES
            ('Jan Kowalski', 'IT', 5000.00),
            ('Anna Nowak', 'HR', 4500.00),
            ('Piotr Zalewski', 'Marketing', 4000.00)
    """)

    # Tworzenie procedury składowanej z instrukcją CASE,
    # która zwróci wartość aktualizującą wynagrodzenie ze wzgędu
    # na stanowisko
    cursor.execute("""
        CREATE OR REPLACE FUNCTION update_employee_salaries()
        RETURNS VOID AS $$
        BEGIN
            UPDATE employees
            SET salary = salary * CASE
                WHEN department = 'IT' THEN 1.10
                WHEN department = 'HR' THEN 1.05
                ELSE 1.03
            END;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury
    cursor.callproc('update_employee_salaries')

    # Zatwierdzanie zmian
    connection.commit()

    # Pobieranie i wyświetlanie wszystkich rekordów
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    print("Stan pracowników po aktualizacji wynagrodzeń: ")
    for emp in employees:
        print(emp)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
