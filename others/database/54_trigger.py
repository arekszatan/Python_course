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

    # Stworzymy teraz prosty przykład wykorzystując TRIGGER w PostgreSQL,
    # który będzie aktualizował dane rekordu przy  zapisie, odnosząc się do tematu monitorów.
    # Utworzymy tabelę monitors z kolumnami id, model, price i last_updated.
    # Następnie zdefinujemy TRIGGER, który zaktualizuje kolumną last_updated
    # do bieżącej daty i godziny przy każdej aktualizacji rekordu w tabeli monitors.

    cursor.execute("""
        DROP TABLE IF EXISTS monitors;
        CREATE TABLE monitors (
            id SERIAL PRIMARY KEY,
            model VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Dodawanie danych do tabeli 'monitors'
    cursor.execute("""
        INSERT INTO monitors (model, price)
        VALUES
            ('Monitor A', 200.00),
            ('Monitor B', 250.00)
    """)

    # Tworzenie funkcji wyzwalającej 'trigger'
    cursor.execute("""
        CREATE OR REPLACE FUNCTION update_last_updated()
        RETURNS TRIGGER AS $$
        BEGIN 
            NEW.last_updated = CURRENT_TIMESTAMP;
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
    """)

    # Utworzenie 'TRIGGER'
    cursor.execute("""
        CREATE TRIGGER update_monitor_last_updated
        BEFORE UPDATE ON monitors
        FOR EACH ROW
        EXECUTE FUNCTION update_last_updated();
    """)

    # Aktualizacja rekordu, aby wyzwolić 'TRIGGER'
    cursor.execute("""
        UPDATE monitors SET price = 210.00 WHERE model = 'Monitor A';
    """)

    # Wyświetlanie zaktualizowanych danych
    cursor.execute("SELECT * FROM monitors")
    monitors = cursor.fetchall()
    for monitor in monitors:
        print(monitor)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
