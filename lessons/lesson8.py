# Что такое База Данных ?
# База данных (БД) — это упорядоченная совокупность данных, которая предназначена для их хранения,
# управления и быстрого доступа. Данные в базе обычно структурированы таким образом,
# чтобы ими было удобно пользоваться. База данных может использоваться для хранения информации
# различного типа: текст, числа, изображения, видео, и другие форматы.


# Что такое  SQL ?
# SQL (Structured Query Language) — это стандартный язык для взаимодействия с базами данных.
# Он используется для выполнения различных операций над данными,
# хранящимися в реляционных базах данных (таких как MySQL, PostgreSQL, SQLite, Oracle, Microsoft SQL Server и другие).


# Что такое СУБД ?
# СУБД (система управления базами данных) — это программное обеспечение,
# которое используется для создания, управления, хранения и извлечения данных в базах данных.
# Она предоставляет инструменты и интерфейсы для работы с данными, обеспечивая их упорядоченное хранение и доступ.


import sqlite3


def connect_or_create_db():
    return sqlite3.connect('user_with_grades.db')


def create_table():
    connect = connect_or_create_db()
    cursor =  connect.cursor()


    # Создание таблиц
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            fio VARCHAR (100) NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    # Таблица оценок по предметам
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades(
        gradeid INTEGER PRIMARY KEY AUTOINCREMENT,
        userid INTEGER,
        subject VARCHAR (100) NOT NULL,
        grade INTEGER NOT NULL,
        FOREIGN KEY (userid) REFERENCES users(userid)
    )
    ''')

    connect.commit()
    connect.close()



def add_user(fio, age):
    connect = connect_or_create_db()
    cursor =  connect.cursor()
    cursor.execute(
        'INSERT INTO users(fio, age) VALUES (?,?)',
        (fio, age))
    connect.commit()
    connect.close()


def add_grade(userid, subject, grade):
    connect = connect_or_create_db()
    cursor =  connect.cursor()
    cursor.execute(
        'INSERT INTO grades(userid, subject, grade) VALUES (?,?,?)',
        (userid, subject, grade))
    connect.commit()
    connect.close()


def get_user_with_grades():
    connect = connect_or_create_db()
    cursor =  connect.cursor()

    cursor.execute('''
        SELECT users.fio, users.age, grades.subject, grades.grade
        FROM users
        LEFT JOIN grades ON users.userid = grades.userid 
    ''')

    rows = cursor.fetchall()
    print(rows)

    for i in rows:
        print(i)


    connect.close()


create_table()

add_user('Ardager', 25)
add_user('Krampoos', 25)

add_grade(1, 'Алгебра', 3)
add_grade(1, 'Русский', 2)
add_grade(2, 'Алгебра', 5)


get_user_with_grades()




