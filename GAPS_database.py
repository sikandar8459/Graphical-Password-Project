import sqlite3
import random as rd

conn = sqlite3.connect("GAPS_DB.db")
cur = conn.cursor()

def create_tb():
    cur.execute("create table if not exists gaps_data (id INTEGER PRIMARY KEY AUTOINCREMENT, username text, email text, password text)")
    conn.commit()

    print("Table created successfully...")

create_tb()

def insert_data():
    un = input("Enter Name : ")
    email = input("Enter Email : ")
    pswd = input("Enter Password : ")

    cur.execute("insert into gaps_data values (?,?,?,?)",(rd.randint(1, 9),un, email, pswd))
    conn.commit()
    print("Data inserted successfully...")

# insert_data()

def delete_data():
    un = input("Enter Name : ")

    cur.execute("delete from gaps_data where username = ?",(un,))
    conn.commit()

    print(f"{un} has been deleted successfully...")

# delete_data()

def show_data():
    cur.execute("select * from gaps_data")
    result = cur.fetchall()

    if len(result) == 0:
        print("Empty")
    else:
        for item in result:
            print(f"ID : {item[0]}")
            print(f"Username : {item[1]}")
            print(f"Email : {item[2]}")
            print(f"Password : {item[3]}\n")

# show_data()

def delete_all():
    cur.execute("delete from gaps_data")
    conn.commit()

    print("Data has been deleted successfully...")

# delete_all()