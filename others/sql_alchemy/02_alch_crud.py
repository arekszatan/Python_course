from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import declarative_base, Session

# Parametry połączenie z bazą danych
DATABASE_URI = 'postgresql+psycopg2://postgres:test123@127.0.0.1/sqlalchemy'

# Nawiązywanie połączenia
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# Definiowanie modelu tabeli
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True)
    email = Column(String)

# Tworzenie tabeli w bazie danych
Base.metadata.create_all(engine)

# Dodawnie użytkowników
def add_user(user_name, email):
    with Session(engine) as session:
        new_user = User(user_name=user_name, email=email)
        session.add(new_user)
        session.commit()

# Pobieranie wszystki9ch użytkowników (Read)
def get_all_users():
    with Session(engine) as session:
        users = session.query(User).all()
        return users

# Aktualizowanie użytko0wnika (Update)
def update_user(user_id, new_user_name, new_email):
    with Session(engine) as session:
        user_to_update = session.query(User).filter(User.id == user_id).one()
        user_to_update.user_name = new_user_name
        user_to_update.email = new_email
        session.commit()

# Usuwanie użytkownika (Delete)
def delete_user(user_id):
    with Session(engine) as session:
        user_to_delete = session.query(User).filter(User.id == user_id).one()
        session.delete(user_to_delete)
        session.commit()

# Testownie funkcji
add_user('Janek', 'Janek@example.com')
add_user('Anna', 'Anna@example.com')

print("Users after adding:")
all_users = get_all_users()
for user in all_users:
    print(f"{user.id}: {user.user_name}, {user.email}")

update_user(1, 'Janek_update', 'updated_janek@example.com')

print("Users after update:")
all_users = get_all_users()
for user in all_users:
    print(f"{user.id}: {user.user_name}, {user.email}")

delete_user(2)

print("Users after delete:")
all_users = get_all_users()
for user in all_users:
    print(f"{user.id}: {user.user_name}, {user.email}")