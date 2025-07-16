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

    # Ustawienie trybu autocommit na False, aby móc zarządzać transakcjami
    connection.autocommit = False

    cursor = connection.cursor()

    # Tworzenie tabeli 'departments'
    cursor.execute("""
    DROP TABLE IF EXISTS employees;
    DROP TABLE IF EXISTS departments;
    CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(255) NOT NULL
    );
    """)

    # Tworzenie tabeli 'employees'
    cursor.execute("""
    CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    department_id INTEGER REFERENCES departments(department_id)
    );
    """)

    # Dodawanie danych do tabeli 'departments'
    cursor.execute("""
    INSERT INTO departments (department_name)
    VALUES ('HR'), ('Development'), ('Marketing');
    """)

    # Dodanie nowego pracownika i aktualizacja informacji o dziale w ramach transakcji
    cursor.execute("""
    INSERT INTO employees (first_name, last_name, department_id)
    VALUES ('Tomasz', 'Nowak', 2);
    """)
    cursor.execute("""
    UPDATE departments SET department_name = 'IT' WHERE department_id = 2;
    """)

    # Zatwierdzanie transakcji
    connection.commit()
    print("Transakcja została pomyślnie zatwierdzona.")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
