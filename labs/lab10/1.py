import psycopg2
import csv

conn = psycopg2.connect( # creating a connection
    database="PhoneBook",
    user="postgres",
    host="localhost",
    password="12345678",
    port=5432,
)

# Создание таблицы
def create_table():
    command = """CREATE TABLE phonebook (
                id SERIAL PRIMARY KEY,
                user_name VARCHAR(255),
                phone VARCHAR(12)
            )"""
    try:
        with conn.cursor() as cur:
            # execute the command
            cur.execute(command)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

    c = input("Table created successfully. Press Enter to continue...")
    return c

# Удаление таблицы
def drop_table():

    command = "DROP TABLE IF EXISTS phonebook"

    with conn.cursor() as cur:
        cur.execute(command) # Выполнение команды
        conn.commit()

# Запись юзера
def insert(user_name, phone):

    command = "INSERT INTO phonebook(user_name, phone) VALUES(%s, %s)"

    with conn.cursor() as cur:
        cur.execute(command, (user_name, phone)) # Выполнение команды
        conn.commit()

# Вставка из CSV-файла
def insert_from_csv(csv_file_name):

    command = "INSERT INTO phonebook(user_name, phone) VALUES(%s, %s)"

    with conn.cursor() as cur:
        with open(csv_file_name, "r") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')
            _ = next(csvreader) # избавление от заголовков
            for row in csvreader:
                user_name, phone = row
                cur.execute(command, (user_name, phone))
        conn.commit()

# Получение фильтра имен по первой букве
def get_names_filter_by_letter(letter):
    command = "SELECT * FROM phonebook WHERE user_name LIKE %s"
    with conn.cursor() as cur:
        cur.execute(command, (letter,)) # (,) is to show that we have a tuple
        results = cur.fetchall()
        if not results:
            print("No users found starting with that letter.")
        else:
            for row in results:
                print(row)
        
# Изменение имени
def update_user_name():
    current_phone = input("Enter current phone number: ")
    new_name = input("Enter new user name: ")

    command = "UPDATE phonebook SET user_name = %s WHERE phone = %s"
    with conn.cursor() as cur:
        cur.execute(command, (new_name, current_phone))
        if cur.rowcount == 0:
            print("No matching user found.")
        else:
            print("User name updated successfully.")
        conn.commit()

# Удаление пользователя
def delete_user(phone):
   
    command = "DELETE FROM phonebook WHERE phone = %s"

    with conn.cursor() as cur:
        cur.execute(command, (phone,))
        conn.commit()

# Вывод всех таблиц
def select_all():
    command = """SELECT EXISTS (
    SELECT 1 
    FROM pg_catalog.pg_tables 
    WHERE tablename = 'phonebook' 
    AND schemaname = 'public'
    );"""
    with conn.cursor() as cur:
        cur.execute(command)
        exists = cur.fetchone()[0]
    if exists:
        command = "SELECT * FROM phonebook"
    else:
        print("Table does not exist.")
        return

    with conn.cursor() as cur:
        cur.execute(command)
        return cur.fetchall()

date = select_all()


