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

    # Tworzenie typu ENUM
    cursor.execute("""
    DROP TYPE IF EXISTS project_status;
    CREATE TYPE project_status AS ENUM ('Active', 'Pending', 'Completed');
    """)

    # Tworzenie tabeli 'projects'
    cursor.execute("""
    DROP TABLE IF EXISTS projects;
    CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    status project_status
    );
    """)

    # Dodawanie  do tabeli 'projects'
    cursor.execute("""
    INSERT INTO projects (name, status)
    VALUES ('Project A', 'Active');
    """)

    cursor.execute("""
    INSERT INTO projects (name, status)
    VALUES ('Project B', 'Pending');
    """)

    cursor.execute("""
    INSERT INTO projects (name, status)
    VALUES ('Project C', 'Completed');
    """)

    # Zatwierdzanie zmian
    connection.commit()

    # Pobieranie i wyświetlanie rekordów
    cursor.execute("SELECT * FROM projects;")
    records = cursor.fetchall()

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
