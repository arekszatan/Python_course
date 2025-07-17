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

    # W kolejnym przykładzie stworzymy procedure składowaną z parametrem wyjściowym out,
    # który pozwoli zwrócić dane z procedury. Załóżmy, że mamy tabelę 'products'
    # i chcemy utworzyć procedurę, która zwraca ilość produktów danego typu.

    # Tworzenie tabeli 'products'
    cursor.execute("""
    DROP TABLE IF EXISTS products;
    CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
    );
    """)

    # Dodawanie danych do tabeli 'products'
    cursor.execute("""
    INSERT INTO products (name, category, price)
    VALUES 
    ('Laptop', 'Electronics', 3000.00),
    ('Smartphone', 'Electronics', 2000.00),
    ('Book "Learn SQL"', 'Books', 100.00),
    ('Coffee', 'Food', 20.00)
    """)

    # Tworzenie procedury składowanej
    cursor.execute("""
    CREATE OR REPLACE FUNCTION count_products_by_category(category_name VARCHAR)
    RETURNS INTEGER AS $$
    DECLARE
        product_count INTEGER;
    BEGIN
        SELECT COUNT(*) INTO product_count FROM products WHERE category = category_name;
        RETURN product_count;
    END;
    $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlanie wyniku.
    cursor.callproc('count_products_by_category', ('Electronics',))
    count = cursor.fetchone()[0]
    print(f"Ilość produktów w kategorii 'Electronics': {count}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
