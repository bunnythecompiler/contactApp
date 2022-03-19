import sqlite3
from datetime import datetime

def create_table():
    conn = sqlite3.connect("ContactDb.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE contacts(
            first_name text,
            last_name text,
            nickname text,
            phone_no text,
            email_address text,
            time text
    )""")
    conn.commit()
    conn.close()

def insert_data(first_name, last_name,nickname, phone_no,email_address,time):
    conn = sqlite3.connect("ContactDb.db")
    c = conn.cursor()
    c.execute("INSERT INTO contacts VALUES (?,?,?,?,?,?)",(first_name,last_name,nickname,phone_no,email_address,time))
    conn.commit()
    conn.close()

def showAllContacts():
    conn = sqlite3.connect("ContactDb.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM contacts ")
    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()

def delete_contact(id):
    conn = sqlite3.connect("ContactDb.db")
    c = conn.cursor()
    statement = "DELETE FROM contacts WHERE rowid=(?)"
    try:
        d = c.execute(statement,(id,))
        print("deleted successfully",d.rowcount)
        conn.commit()
    except sqlite3.Error as my_error:
        print("error",my_error)
        
    conn.commit()
    conn.close()

def search_contacts(first_name):
    conn = sqlite3.connect("ContactDb.db")
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE first_name =?",(first_name,))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()


