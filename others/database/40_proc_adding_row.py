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

    # Tworzenie tabeli 'customers'
    cursor.execute("""
    DROP TABLE IF EXISTS customers;
    CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255)
    );
    """)

    # Dodawanie przykładowych rekordów
    cursor.execute("""
    INSERT INTO customers (name, email)
    VALUES ('Jan Kowalski', 'jan@example.com'), ('Anna Nowak', 'anna@example.com');
    """)

    # Tworzenie procedury składowanej
    cursor.execute("""
    CREATE OR REPLACE FUNCTION add_customer (cust_name VARCHAR, cust_mail VARCHAR)
    RETURNS VOID AS $$
    BEGIN
        INSERT INTO customers (name, email) VALUES (cust_name, cust_mail);
    END;
    $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury do dodania nowego klienta
    cursor.callproc('add_customer', ('Tomasz Wiśniewski', 'tomasz@example.com'))

    # Zatwierdzanie zmian
    connection.commit()

    # Pobieranie i wyświetlanie wszystkich rekordów
    cursor.execute("SELECT * FROM customers")
    records = cursor.fetchall()

    print("Wszystkie rekordy w tabeli 'customers':")
    for row in records:
        print(row)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
