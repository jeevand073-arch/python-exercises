import sqlite3

def create_db():
    conn = sqlite3.connect("Student.IF")
    print("database created successfully")
    c = conn.cursor()
    c.execute("""
       CREATE TABLE  Student_table(
            Roll_no INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50)NOT NULL,
            email VARCHAR(50) UNIQUE,
            age INT)
    """)
    c.execute(""" CREATE TABLE IF NOT EXISTS Subject_table(
            Subject VARCHAR(50)NOT NULL)""")
    c.execute(""" CREATE TABLE IF NOT EXISTS Mark_table(
            marks int)""")
    c.execute("""CREATE TABLE IF NOT EXISTS Grad_table(
            grad VARCHAR(50)NOT NULL)""")

   
    conn.commit()
    conn.close()
    print("successfull")
create_db()