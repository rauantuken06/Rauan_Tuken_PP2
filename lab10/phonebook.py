import psycopg2
import csv
from tabulate import tabulate

conn=psycopg2.connect(
    host="localhost",
    dbname="lab10",
    user="postgres",
    password="Barcelona better than RM",
    port=5432,
)
cur=conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        user_id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        surname VARCHAR(255) NOT NULL,
        phone VARCHAR(255) UNIQUE NOT NULL    
    )
""")
conn.commit()

def print_menu():
    print("""
    List of commands:
    1.[I] Insert data (CSV or Console)
    2.[U] Update data
    3.[Q] Query data
    4.[D] Delete data
    5.[S] Show all
    6.[F] Finish
    """)

def is_valid_phone(phone):
    return phone.isdigit()

while True:
    print_menu()
    command=input("Enter command: ").strip().lower()

    if command=="i":
        source=input("Type 'csv' to upload from file or 'con' to enter manually:").strip().lower()

        if source=='csv':
            path=input("Enter CSV file path: ").strip()
            try:
                with open(path, 'r') as f:
                    reader=csv.reader(f)
                    next(reader)
                    for row in reader:
                        if len(row)==3 and is_valid_phone(row[2]):
                            try:
                                cur.execute(
                                    "INSERT INTO phonebook (name, surname, phone) VALUES(%s, %s, %s)",
                                    (row[0], row[1], row[2])
                                )
                            except Exception as e:
                                print(f"Error inserting {row}: {e}")
                                conn.rollback()
                    conn.commit()
                    print("Data inserted from CSV.")
            except FileNotFoundError:
                print("File not found.")
        elif source=='con':
            name=input("Name: ")
            surname=input("Surname: ")
            phone=input("Phone: ")
            if is_valid_phone(phone):
                try:
                    cur.execute(
                        "INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)",
                        (name, surname, phone)
                    )
                    conn.commit()
                    print("Inserted successfully.")
                except Exception as e:
                    print("Error:", e)
                    conn.rollback()
            else:
                print("Inavalid phone number.")
    elif command=='u':
        field=input("Which field do you want to update ? (name/surname/phone): ").strip().lower()
        if field in ["name", "surname", "phone"]:
            old_value=input(f"Current {field}: ")
            new_value=input(f"New {field}: ")

            if field=="phone" and not is_valid_phone(new_value):
                print("Phone must contain only digits.")
                continue
            try:
                cur.execute(
                    f"UPDATE phonebook SET {field}=%s WHERE {field}=%s",
                    (new_value, old_value)
                )
                conn.commit()
                print("Updated successfully.")
            except Exception as e:
                print("Error updating:", e)
                conn.rollback()
        else:
            print("Invalid field.")
    elif command=='q':
        filter_by=input("Search by (id/name/surname/phone): ").strip().lower()
        if filter_by in ['id', 'name', 'surname', 'phone']:
            value=input("Enter value to search: ")
            try:
                query=f"SELECT * FROM phonebook WHERE {filter_by}=%s"
                cur.execute(query, (value,))
                rows=cur.fetchall()
                if rows:
                    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
                else:
                    print("No result found.")
            except Exception as e:
                print("Query error:", e)
        else:
            print("Invalid field.")
    elif command=='d':
        value=input("Enter phone or name to delete: ")
        try:
            cur.execute("DELETE FROM phonebook WHERE phone=%s OR name=%s", (value, value))
            conn.commit()
            print("Deleted successfully.")
        except Exception as e:
            print("Error deleting:", e)
            conn.rollback()
    elif command=='s':
        cur.execute("SELECT * FROM phonebook")
        rows=cur.fetchall()
        print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
    elif command=='f':
        print("Program finished.")
        break
    else:
        print("Unknown command. Try again.")

cur.close()
conn.close()