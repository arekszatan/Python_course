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

    # W tym przykładzie stworzymy procedurę składowną z użyciem JOIN, która połączy
    # dane z dwóch tabel. Załóżmy, że mamy dwie tabele: trucks (ciężarówki)
    # i drivers (kierowcy), gdzie każda ciężarówka jest przypisana do określonego kierowcy.
    # Utworzymy procedórę, która zwróci listę cieżarówek wraz z informacjami o ich kierowcach.

    cursor.execute("""
    DROP TABLE IF EXISTS trucks;
    DROP TABLE IF EXISTS drivers;
    CREATE TABLE drivers (
        driver_id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    );
    """)

    # Tworzenie tabeli 'trucks'
    cursor.execute("""
    CREATE TABLE trucks (
        truck_id SERIAL PRIMARY KEY,
        model VARCHAR(255) NOT NULL,
        driver_id INTEGER REFERENCES drivers(driver_id)
    );
    """)

    # Dodawanie danych do tabeli 'drivers'
    cursor.execute("""
        INSERT INTO drivers (name) VALUES ('Jan Kowalski'), ('Adam Nowak');
    """)

    # Dodawanie danych do tabeli 'trucks'
    cursor.execute("""
        INSERT INTO trucks (model, driver_id)
        VALUES
            ('Volvo FH', 1),
            ('Scania R500', 2);
    """)

    # Tworzenie procedury składowanej z JOIN
    cursor.execute("""
        CREATE OR REPLACE FUNCTION get_trucks_with_drivers()
        RETURNS TABLE(truck_model VARCHAR, driver_name VARCHAR)
        AS $$
        BEGIN
            RETURN QUERY
            SELECT t.model, d.name
            FROM trucks t
            JOIN drivers d ON t.driver_id = d.driver_id;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury i wyświetlanie wyniku
    cursor.callproc('get_trucks_with_drivers')
    trucks = cursor.fetchall()
    print("Ciężarówki i ich kierowcy: ")
    for truck in trucks:
        print(truck)


except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
