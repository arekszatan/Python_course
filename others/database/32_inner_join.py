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

    # Załóżmy, że mamy tabelę authors i powiązaną z nią tabelę books.
    # Każda książka będzie przypisana do jednego autora.
    # Najpierw utworzymy obie tabele,dodamy do nich dane, a potem połączymy
    # je za pomocą INNER JOIN

    # Tworzenie tabeli 'authors'
    cursor.execute("""
    DROP TABLE IF EXISTS books;
    DROP TABLE IF EXISTS authors;
    CREATE TABLE authors(
    author_id SERIAL PRIMARY KEY,
    name VARCHAR (255) NOT NULL
    );
    """)

    # Tworzenie tabeli 'books'
    cursor.execute("""
    CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR (255) NOT NULL,
    author_id INTEGER REFERENCES authors (author_id) 
    );
    """)

    # Dodanie rekordów do tabeli 'authors'
    cursor.execute("""
    INSERT INTO authors (name)
    VALUES ('Adam Mickiewicz'), ('Juliusz Słowacki'), ('Bolesław Prus');
    """)

    # Dodanie rekordów do tabeli 'books'
    cursor.execute("""
    INSERT INTO books (title, author_id)
    VALUES ('Pan Tadeusz', 1), ('Balladyna', 2), ('Lalka', 3);
    """)

    # Zatwierdzanie zmian
    connection.commit()

    # Pobieranie i wyświetlanie rekordów za pomacą INNER JOIN
    cursor.execute("""
    SELECT a.name, b.title
    FROM authors a 
    INNER JOIN books b ON a.author_id = b.author_id;
    """)
    records = cursor.fetchall()

    print("Książki i ich autorzy:")
    for row in records:
        print(f"Autor: {row[0]}, Tytuł książki: {row[1]}")

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
