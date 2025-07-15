import psycopg2

# Dane do połączenia z bazą danych PostgreSQL
host = "127.0.0.1"
user = "postgres"
password = "test123"
database = "py_test"

# Nawiązywanie połączenia z bazą danych
try:
    # Utworzenie połączenia z bazą danych
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # Utworzenie kursora, który umożliwia wykonywanie operacji na bazie danych
    cursor = connection.cursor()

    #Zapytanie z użyciem LIKE dla "Imie3"
    select_query_like = """
    SELECT * FROM employee
    WHERE first_name LIKE 'Imie_3%'
    """
    cursor.execute(select_query_like)
    records = cursor.fetchall()

    print("Pracownicy, których imię zaczyna się od 'Imie3'")
    for row in records:
        print(row)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    # Zawsze zamykaj połączenie i kursor, aby zwolnić zasoby
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
