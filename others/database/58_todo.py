import psycopg2
from tkinter import *
from tkinter import messagebox
from datetime import datetime

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

    connection.autocommit = True
    cursor = connection.cursor()

    cursor.execute("DROP DATABASE IF EXISTS py_todo;")
    cursor.execute("CREATE DATABASE py_todo;")
    cursor.close()
    connection.close()

    # Ponowne połączenie z nowo utworzoną bazą danych
    dbname = "py_todo"
    conn = psycopg2.connect(host=host, user=user, password=password, dbname=dbname)
    cursor = conn.cursor()

    def create_table():
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                content TEXT NOT NULL,
                due_date DATE NOT NULL
            );
        """)
        conn.commit()

    # Funkcja do obsługi bazy danych
    def add_task(title, content, due_date):
        """Dodaje nowe zadanie do bazy danych."""
        if not due_date:
            due_date = datetime.now().strftime("%Y-%m-%d")

        cursor.execute("""
            INSERT INTO tasks (title, content, due_date)
            VALUES (%s, %s, %s)
        """, (title, content, due_date))

        conn.commit()
        load_tasks()

    def update_task(task_id, title, content, due_date):
        """Aktualizuje zadanie w bazie danych."""
        if not due_date:
            due_date = datetime.now().strftime("%Y-%m-%d")

        cursor.execute("""
            UPDATE tasks SET title = %s, content = %s, due_date = %s
            WHERE id = %s
        """, (title, content, due_date, task_id))

        conn.commit()
        load_tasks()

    # Kasowanie zadania
    def delete_task(task_id):
        """Usuwanie zadania z bazy danych"""
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        conn.commit()
        load_tasks()

    # Odczyt zadań
    def load_tasks():
        """Ładuje zadania z bazy danych i wyświetla je w interfejsie użytkonika."""
        cursor.execute("SELECT * FROM tasks;")
        tasks = cursor.fetchall()

        # Czyszczenie listy zadań w GUI
        for widget in frame_tasks.winfo_children():
            widget.destroy()

        # Dodawanie zadań do GUI
        for task in tasks:
            task_frame = Frame(frame_tasks, bg="white", pady=10)
            task_frame.pack(fill="x")

            Label(task_frame, text=f"{task[1]} (do wykonania: {task[3]})",
                  bg="white").pack(side="left")
            Button(task_frame, text="Edytuj", command=lambda task=task: edit_task(task)).pack(side="right")
            Button(task_frame, text="Usuń", command=lambda task_id=task[0]: delete_task(task_id)).pack(side="right")

    # Edycja zadania
    def edit_task(task):
        """Wypełnia formularz danymi wybranego zadania do edycji"""
        entry_title.delete(0, END)
        entry_title.insert(0, task[1])
        entry_content.delete(0, END)
        entry_content.insert(0, task[2])
        entry_due_date.delete(0, END)
        entry_due_date.insert(0, task[3])
        button_add_task.config(text="Zapisz", width=25,
                               command= lambda: update_task(task[0], entry_title.get(),
                                                            entry_content.get(), entry_due_date.get()))

    # Konfiguracja GUI
    root = Tk()
    root.title("Zarządzanie zadaniami")
    root.geometry("600x400")

    frame_add_task = Frame(root, padx=10, pady=10)
    frame_add_task.pack(fill="x")

    Label(frame_add_task, text="Tytuł:").pack(side="left")
    entry_title = Entry(frame_add_task)
    entry_title.pack(side="left", expand=True, fill="x")

    Label(frame_add_task, text="Treść:").pack(side="left")
    entry_content = Entry(frame_add_task)
    entry_content.pack(side="left", expand=True, fill="x")

    Label(frame_add_task, text="Data wykonania").pack(side="left")
    entry_due_date = Entry(frame_add_task)
    entry_due_date.pack(side="left", expand=True, fill="x")

    # Przycisk do dodawania nowego zadania
    button_add_task = Button(frame_add_task, text="Dodaj", width=20,
                             command=lambda: add_task(entry_title.get(), entry_content.get(),
                                                      entry_due_date.get()))
    button_add_task.pack(side="right")

    frame_tasks = Frame(root, bg="white")
    frame_tasks.pack(fill="both", expand=True)

    # Tworzenie tabeli i ładownie danych
    create_table()
    load_tasks()

    # Funkcja zamykająca połączenie z bazą danych przy zamykaniu okna aplikacji
    def on_closing():
        if messagebox.askokcancel("Quit", "Czy na pewno chcesz wyjść?"):
            cursor.close()
            conn.close()
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()



except (Exception, psycopg2.DatabaseError) as error:
    print("Błąd podczas połączenia z bazą danych PostgresSQL", error)
finally:
    if connection:
        print("Połączenie z bazą działa.")
        cursor.close()
        connection.close()
        print("Połączenie z bazą zostało zamknięte.")
