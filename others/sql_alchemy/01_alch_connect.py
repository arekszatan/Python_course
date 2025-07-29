from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import declarative_base, Session

# Parametry połączenie z bazą danych
DATABASE_URI = 'postgresql+psycopg2://postgres:test123@127.0.0.1/sqlalchemy'

# Nawiązywanie połączenia
engine = create_engine(DATABASE_URI)

# Tworzenie klasy bazowej
# Declaratibvve bbase to klasa bazowa dla wszystkich modeli tabe, pozwala na deklaratywne definiowanie struktur
Base = declarative_base()

# Definiowanie modelu tabeli
# Klasa ExampleTable dziedziczy po Base i reprezentuje tabelę w bazie danych
class ExampleTable(Base):
    __tablename__ = 'example_table' # Nazwa tabeli w bazie danych
    id = Column(Integer, primary_key=True) # Definiowanie kolumny 'id'
    name = Column(String) # Definicja kolumny 'name'
    description = Column(String) # Definicja kolumny 'description'


# Tworzenie tabeli
# create_all tworzy tabelę w bazie danbych zgodnie z zadefiniowanym modelem
Base.metadata.create_all(engine)

# Dodawanie rekordu do tabeli
# Session to kontekst sesji bazy danych, pozwala na zarządzenie
# rekordami (dadwanie, modyfikowanie, usuwanie)
with Session(engine) as session:
    new_record = ExampleTable(name="Przykład", description="Opis przykładu") # Tworzenie nowego przykładu
    session.add(new_record) # Dodawnie rrekordu do sesji
    session.commit() # Zatwirzdzanie zmian w bazie danych

# Pobieranie i wyświetlanie rekordów z tabeli
with Session(engine) as session:
    result = session.query(ExampleTable).all() # Pobieranie wszystkich rekordów z tabeli
    for row in result:
        print(f"ID: {row.id}, Name: {row.name}, Description: {row.description}")

