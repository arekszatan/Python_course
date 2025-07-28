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

    # Strowrzymy prosty przykład dwóch procedur w PostggreSQL, gdzie jadna procedura
    # wywołuje inną. Tematem będą ksiązki. Utworzymy tabelę books z kolumnami id,
    # title i price. Następnie stowrzymy dwie procedury: update_book_price
    # doi aktual;izacji ceny książki i bulk_update_book_price do wywołania
    # up[date_book_price dla każdej książki w tabeli z określoną zmianą ceny.

    # Tworzenie tabeli 'books'
    cursor.execute("""
        DROP TABLE IF EXISTS books;
        CREATE TABLE books(
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL
        );
    """)

    # Dodawanie danych do tabeli 'books'
    cursor.execute("""
        INSERT INTO books (title, price)
        VALUES
            ('Book A', 20.00),
            ('Book B', 25.00),
            ('Book C', 22.50)
    """)

    # Tworzenie funkcji 'update_book_price'
    cursor.execute("""
        CREATE OR REPLACE FUNCTION update_book_price(book_id INT, new_price DECIMAL)
        RETURNS VOID AS $$
        BEGIN 
            UPDATE books SET price = new_price WHERE id = book_id;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Tworzenie funkcji 'bulk_update_book_prices'
    cursor.execute("""
        CREATE OR REPLACE FUNCTION bulk_update_book_prices(price_change DECIMAL)
        RETURNS VOID AS $$
        DECLARE
            book RECORD;
        BEGIN
            FOR book IN SELECT * FROM books
            LOOP 
                PERFORM update_book_price(book.id, book.price + price_change);
            END LOOP;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie funkcji 'bulk_update_book_prices'
    cursor.execute("SELECT bulk_update_book_prices(5)")
    connection.commit()

    # Wyświetlanie zaktualizowanycvh danych
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    for book in books:
        print(book)


except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
