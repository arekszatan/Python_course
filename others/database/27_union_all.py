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

    # Zapytanie SQL z użyciem UNION ALL
    # W tym przykładzie, wykorzystamt UNION ALL do połączenia dwóch zapytań
    # z tabeli employees: jedno zapytanie wybierze pracowników na stanowisku "manager',
    # a drugie pracowników na stanowisku 'Developer'.

    union_all_query = """
    SELECT first_name, last_name, position FROM employees WHERE position = 'Manager'
    UNION ALL
    SELECT first_name, last_name, position FROM employees WHERE position = 'Developer'
    """
    cursor.execute(union_all_query)
    records = cursor.fetchall()

    print("Pracownicy na stanowiskach 'Manager' i 'Developer'")
    for row in records:
        print(row)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgreSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
