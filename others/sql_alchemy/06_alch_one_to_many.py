from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship, joinedload
from sqlalchemy.exc import NoResultFound


# Parametry połączenie z bazą danych
DATABASE_URI = 'postgresql+psycopg2://postgres:test123@127.0.0.1/sqlalchemy'

# Nawiązywanie połączenia
engine = create_engine(DATABASE_URI)
Base = declarative_base()

class School(Base):
    __tablename__ = "schools"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship("Student", back_populates="school")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    school_id = Column(Integer, ForeignKey("schools.id"), nullable=False)
    school = relationship("School", back_populates="students")

Base.metadata.create_all(engine)

def add_school(name):
    with Session(engine) as session:
        school = School(name=name)
        session.add(school)
        session.commit()

def add_student(name, school_id):
    with Session(engine) as session:
        student = Student(name=name, school_id=school_id)
        session.add(student)
        session.commit()

def get_all_schools():
    with Session(engine) as session:
        schools = session.query(School).options(joinedload(School.students)).all()
        return schools

def update_student(student_id, new_name):
    with Session(engine) as session:
        try:
            student = session.query(Student).filter(Student.id == student_id).one()
            student.name = new_name
            session.commit()
        except NoResultFound:
            print(f"Student o ID {student_id} nie istnieje.")

def delete_student(student_id):
    with Session(engine) as session:
        try:
            student = session.query(Student).filter(Student.id == student_id).one()
            session.delete(student)
            session.commit()
        except NoResultFound:
            print(f"Student o ID {student_id} nie istnieje.")

# Dodawnaie danych do testów
add_school("Liceum Ogólnokształcące nr 1")
add_school("Technikum Informatyczne")

add_student("Jan Kowalski", 1)
add_student("Anna Nowak", 2)
add_student("Jan Kowalski 1", 1)
add_student("Anna Nowak 1", 2)

# Testowanie funkcji
schools = get_all_schools()
for school in schools:
    print(f"Szkoła: {school.name}")
    for student in school.students:
        print(f"    Uczeń: {student.name}")

# Update i delete
update_student(1, "Jan Nowkaowski")
delete_student(2)

schools = get_all_schools()
for school in schools:
    print(f"Szkoła: {school.name}")
    for student in school.students:
        print(f"    Uczeń: {student.name}")