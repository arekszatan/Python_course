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

    cursor.execute("""
    DROP TABLE IF EXISTS documents;
    CREATE TABLE documents (
    document_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(255) NOT NULL
    );
    """)

    # Dodawanie danych do tabeli 'documents'
    cursor.execute("""
    INSERT INTO documents (title,status)
    VALUES 
        ('Dokument A', 'Pending'),
        ('Dokument B', 'Approved'),
        ('Dokument C', 'Pending');
    """)

    # Tworzenie procedury składowanej z pętlą
    cursor.execute("""
    CREATE OR REPLACE FUNCTION update_document_statuses()
    RETURNS VOID AS $$
    DECLARE 
        record RECORD;
    BEGIN
        FOR record IN SELECT * FROM documents WHERE status = 'Pending'
        LOOP
            UPDATE documents SET status = 'Reviewed' WHERE document_id = record.document_id;
        END LOOP;
    END;
    $$ LANGUAGE plpgsql;
    """)

    # Wywołanie procedury
    cursor.callproc('update_document_statuses')

    # Zatwierdzanie zmian
    connection.commit()

    # Pobieranie i wyświetlanie wszystkich rekordóœ
    cursor.execute("SELECT * FROM documents")
    documents = cursor.fetchall()

    print("Stan dokumpentów po aktualizacji:")
    for doc in documents:
        print(doc)

except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
