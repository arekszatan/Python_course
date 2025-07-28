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

    # Tworzenie tabeli 'manufactures'
    cursor.execute("""
        DROP TABLE IF EXISTS manufactures;
        CREATE TABLE manufactures(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    """)

    # Tworzenie tabeli 'laptops'
    cursor.execute("""
        DROP TABLE IF EXISTS laptops;
        CREATE TABLE laptops(
            id SERIAL PRIMARY KEY,
            model VARCHAR(255) NOT NULL,
            manufacture_id INT NOT NULL,
            price DECIMAL(10, 2),
            FOREIGN KEY (manufacture_id) REFERENCES manufactures(id)
        );
    """)

    # Dodawanie danych do tabeli 'manufactures'
    cursor.execute("""
        INSERT INTO manufactures (name) VALUES ('Lenovo'), ('HP'), ('Dell');
    """)

    # Dodawanie danych do tabeli 'laptops'
    cursor.execute("""
        INSERT INTO laptops (model, manufacture_id, price) VALUES
            ('ThinkPad X1', 1, 1200.00),
            ('Pavilon 15', 2, 800.00),
            ('XPS 15', 3, 1600.00);
    """)

    # Aktualizacja rekordu w 'laptops'
    cursor.execute("""
        UPDATE laptops SET price = 1300.00 WHERE model = 'ThinkPad X1';
    """)

    # Usuwanie rekordu z 'laptops'
    cursor.execute("""
        DELETE FROM laptops WHERE model = 'XPS 15';
    """)

    # Odczytywanie danych z 'laptops'
    cursor.execute("SELECT * FROM laptops")
    laptops = cursor.fetchall()
    print("Laptopy:")
    for laptop in laptops:
        print(laptop)

    # JOIN między 'manufactures' i 'laptops'
    cursor.execute("""
        SELECT manufactures.name, laptops.model, laptops.price
        FROM manufactures
        JOIN laptops ON manufactures.id = laptops.manufacture_id;
    """)

    joined_data = cursor.fetchall()
    print("\nLaptopy z producentami:")
    for item in joined_data:
        print(item)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
