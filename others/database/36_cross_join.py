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

    # CROSS JOIN w SQL jest używany do tworzenia kombinacji kartezjańskich dwóch tabel
    # co oznacza, że każdy wiersz z pierwszej tabeli jest łączony z każdym wierszem
    # z drugiej tabeli. W rezultacie liczba wierszy w wynikowym zbiorze danych
    # jest równa iloczynowi liczby wierszy w obu tabelach.

    # Załóżmy, że mamy dwie tabele: colors i shapes i chcemy stworzyć wszystkie
    # możliwe kombinacje kolorów i kształtów.

    # Tworzenie tabeli 'colors'
    cursor.execute("""
    DROP TABLE IF EXISTS shapes;
    DROP TABLE IF EXISTS colors;
    CREATE TABLE colors (
    color_id SERIAL PRIMARY KEY,
    color_name VARCHAR(255) NOT NULL
    );
    """)

    # Tworzenie tabeli 'shapes'
    cursor.execute("""
    CREATE TABLE shapes (
    shape_id SERIAL PRIMARY KEY,
    shape_name VARCHAR(255) NOT NULL
    );
    """)

    # Dodawanie rekordów do tabeli 'colors'
    cursor.execute("""
    INSERT INTO colors (color_name)
    VALUES ('Red'), ('Green'), ('Blue');
    """)

    # Dodawanie rekordów do tabeli 'shapes'
    cursor.execute("""
    INSERT INTO shapes (shape_name)
    VALUES ('Circle'), ('Square'), ('Triangle'); 
    """)

    # Zatwierdzanie zmian
    connection.commit()

    # Pobieranie i wyświetlanie rekordów za pomocą CROSS JOIN
    cursor.execute("""
    SELECT c.color_name, s.shape_name
    FROM colors c
    CROSS JOIN shapes s    
    """)

    records = cursor.fetchall()

    print("Wszystkie kombinacje kolorów i kształtów:")
    for row in records:
        print(f"Kolor: {row[0]}, Kształt: {row[1]}")


except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
