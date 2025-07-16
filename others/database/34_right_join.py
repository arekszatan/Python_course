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

    # RIGHT JOIN podobnie do LEFT JOIN, ale tym razem pobiera wszystkie rekordy
    # z prawej tabeli (tabeli po prawej stronie JOIN) i dopasowane rekordy z lewej tabeli
    # (tabeli po lewej stronie JOIN). Jeśli nie ma dopasowania, wynikiem
    # dla lewej tabeli będzie NULL.

    # Stworzymy dwie nowe tabele: artists i albums. Tabela albums będzie zawierała
    # albumy muzyczne, które mogą, ale nie muszą być przypisane do artystów
    # z tabeli artists. Wykorzystamy RIGHT JOIN do wyświetlania wszystkich albumów
    # wraz z informacjami o artystach, jeśli taka informacja istnieje.

    # Tworzenie tabeli 'artists'
    cursor.execute("""
    DROP TABLE IF EXISTS albums;
    DROP TABLE IF EXISTS artists;
    CREATE TABLE artists (
    artist_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
    );
    """)

    # Tworzenie tabeli 'albums'
    cursor.execute("""
    CREATE TABLE albums (
    album_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    artist_id INTEGER REFERENCES artists(artist_id)
    );
    """)

    # Dodawanie rekordów do tabeli 'artist'
    cursor.execute("""
    INSERT INTO artists (name)
    VALUES ('The Beatles'), ('Led Zeppelin');
    """)

    # Dodawanie rekordów do tabeli 'albums'
    cursor.execute("""
    INSERT INTO albums (title, artist_id)
    VALUES ('Abbey Road', 1), ('Led Zeppelin IV', 2), ('Random Album', NULL);
    """)

    # Zatwierdzanie zmian
    connection.commit()

    # Pobieranie i wyświetlanie rekordów za pomocą RIGHT JOIN
    cursor.execute("""
    SELECT a.name, al.title
    FROM artists a
    RIGHT JOIN albums al ON a.artist_id = al.artist_id;
    """)

    records = cursor.fetchall()

    for row in records:
        print(f"Artysta: {row[0]}, Album: {row[1]}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
