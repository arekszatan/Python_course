from sqlalchemy import create_engine, Column, Integer, String, and_, or_
from sqlalchemy.orm import declarative_base, Session


# Parametry połączenie z bazą danych
DATABASE_URI = 'postgresql+psycopg2://postgres:test123@127.0.0.1/sqlalchemy'

# Nawiązywanie połączenia
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# Definiowanie mod3elu tabeli dla pracowników
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    department = Column(String)
    age = Column(Integer)

# Tworzenie tabeli w bazie dancyh
Base.metadata.create_all(engine)

# Dodawanie pracownika (Create)
def add_employee(name, department, age):
    with Session(engine) as session:
        new_employee = Employee(name=name, department=department, age=age)
        session.add(new_employee)
        session.commit()

# Pobieranie wszystkich pracowników (Read)
def get_all_employees():
    with Session(engine) as session:
        employees = session.query(Employee).all()
        return employees

# Aktual;izowanie danych pracownika (Update)
def update_employee(employee_id, new_name, new_department, new_age):
    with Session(engine) as session:
        employee = session.query(Employee).filter(Employee.id == employee_id).one()
        employee.name = new_name
        employee.department = new_department
        employee.age = new_age
        session.commit()

# Usuwanie pracownika (Delete)
def delete_employee(employee_id):
    with Session(engine) as session:
        employee_to_delete = session.query(Employee).filter(Employee.id == employee_id).one()
        session.delete(employee_to_delete)
        session.commit()

# Zaawansowane zapytania z AND i OR
def find_employees_by_criteria(department, age):
    with Session(engine) as session:
        employees = session.query(Employee).filter(
            and_(Employee.department == department, Employee.age > age)
        ).all()
        return employees

def find_employees_by_name_or_department(name, department):
    with Session(engine) as session:
        employees = session.query(Employee).filter(
            or_(Employee.name == name, Employee.department == department)
        ).all()
        return employees

# Testowanie funkcji
add_employee("Jan Kowalski", "HR", 30)
add_employee("Anna Nowak", "IT", 25)
add_employee("Piotr Zieliński", "HR", 40)
add_employee("Jan Kowalski 1", "HR", 50)
add_employee("Anna Nowak 1", "IT", 55)
add_employee("Piotr Zieliński 1", "HR", 50)

# Wyświetlanie wszystkich pracowników
all_employees = get_all_employees()
for employee in all_employees:
    print(f"{employee.id}: {employee.name}, {employee.department}, {employee.age}")

# Wyświetlanie pracowników spełniających kryteria (AND)
print("\nPracownicy z działu HR powyżej 30 lat:")
employee_hr_over_30 = find_employees_by_criteria("HR", 30)
for employee in employee_hr_over_30:
    print(f"{employee.id}: {employee.name}, {employee.department}, {employee.age}")

# Wyświetlanie pracowników spełniających krytera (OR)
print("\n Pracownicy o imieniu 'Anna' lub z działu IT:")
employee_anna_or_it = find_employees_by_name_or_department("Anna", "IT")
for employee in employee_anna_or_it:
    print(f"{employee.id}: {employee.name}, {employee.department}, {employee.age}")
