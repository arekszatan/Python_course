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

    # Stworzymy przykład procedury, która przyjmuje tablic≥ę identyfikatorów (ID)
    # jako parametr i zwraca rekordy pasujące do tych ID. W tym przykładzie utworzymy
    # tabelę products z kolumnami id, name i category. Następnie stowrzymy procedurę,
    # która przyjmuje tablice ID produktów i zwraca szczegóły tych produktów.

    # Tworzenie tabeli 'products'
    cursor.execute("""
        DROP TABLE IF EXISTS products;
        CREATE TABLE products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            category VARCHAR(50) NOT NULL
        );
    """)

    # Dodawanie danych do tabeli 'products'
    cursor.execute("""
        INSERT INTO products (name, category)
        VALUES 
            ('Laptop', 'Electronics'),
            ('Książka', 'Books'),
            ('Smartfon', 'electronics'),
            ('Kawa', 'Food');
    """)

    # Tworzenie procedury składowanej
    cursor.execute("""
        CREATE OR REPLACE FUNCTION get_products_by_ids(ids INT[])
        RETURNS TABLE(id INT, name VARCHAR, category VARCHAR) AS $$
        BEGIN
            RETURN QUERY SELECT p.id, p.name, p.category FROM products p WHERE p.id = ANY(ids);
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlanie wyniku.
    cursor.callproc('get_products_by_ids', ([1, 3],))
    products = cursor.fetchall()
    for product in products:
        print(product)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
