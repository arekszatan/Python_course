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

    # Tworzenie procedury składowanej 'add_numbers'
    cursor.execute("""
    CREATE OR REPLACE FUNCTION add_numbers(a INTEGER, b INTEGER)
    RETURNS INTEGER AS $$
    BEGIN
        RETURN a + b;
    END;
    $$ LANGUAGE plpgsql;
    """)

    # Wywołąnie procedury i wyświetlanie wyniku
    cursor.callproc('add_numbers', (10, 20))
    adding_sum = cursor.fetchone()[0]
    print(f"Wynik dodawania: {adding_sum}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
