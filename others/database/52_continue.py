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

    # Utowrzymy tabelę vegetables z kolumnami id, namer i quantity.
    # Następnie stworzymy procedurę, któ©a iteruje przez warzywa w tabeli i
    # jeśli ilość danego warzywa jest poniżęj określonego progu, procedura użyje
    # instrukcji CONTINUE do pominięcia aktualizacji ceny tego warzywa.

    # Twqorzenie tabeli 'vegetables'
    cursor.execute("""
        DROP TABLE IF EXISTS vegetables;
        CREATE TABLE vegetables (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            quantity INT NOT NULL,
            price DECIMAL(10, 2) NOT NULL DEFAULT 0.00
        );
    """)

    # Dodawanie danych do tabeli 'vegetables'
    cursor.execute("""
        INSERT INTO vegetables (name, quantity, price)
        VALUES
            ('Tomato', 100, 0.50),
            ('Cucumber', 30, 0.30),
            ('Carrot', 50, 0.20),
            ('Lettuce', 10, 0.40);
    """)

    # Tworzenie procedury składowanej
    cursor.execute("""
        CREATE OR REPLACE FUNCTION update_vegetable_prices(min_quantity INT, price_increase DECIMAL)
        RETURNS VOID AS $$
        DECLARE
            vegetable RECORD;
        BEGIN
            FOR vegetable IN SELECT * FROM vegetables
            LOOP
                IF vegetable.quantity < min_quantity THEN
                    CONTINUE;
                END IF;
                UPDATE vegetables SET price = price + price_increase WHERE id = vegetable.id;
            END LOOP;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlanie wyniku
    cursor.callproc('update_vegetable_prices', (20, 0.05))
    connection.commit()

    cursor.execute("SELECT * FROM vegetables;")
    vegetables = cursor.fetchall()
    for vegetable in vegetables:
        print(vegetable)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
