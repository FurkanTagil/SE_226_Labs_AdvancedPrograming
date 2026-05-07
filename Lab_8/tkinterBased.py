import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD"  
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS StudentDatabase")

cursor.execute("USE StudentDatabase")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Score INT
)
""")

conn.commit()


def insert_student():
    name = entry_name.get()
    score = entry_score.get()

    if name == "" or score == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        score = int(score)

        if score < 1 or score > 100:
            messagebox.showerror("Error", "Score must be between 1 and 100")
            return

        sql = "INSERT INTO Students(Name, Score) VALUES(%s, %s)"
        values = (name, score)

        cursor.execute(sql, values)
        conn.commit()

        messagebox.showinfo("Success", "Student added successfully")

        entry_name.delete(0, tk.END)
        entry_score.delete(0, tk.END)

        show_students()

    except:
        messagebox.showerror("Error", "Invalid score")


def show_students():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM Students")

    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)


def filter_students():
    value = filter_entry.get()

    if value == "":
        show_students()
        return

    try:
        value = int(value)

        query = "SELECT * FROM Students WHERE Score > %s"

        cursor.execute(query, (value,))

        rows = cursor.fetchall()

        for row in tree.get_children():
            tree.delete(row)

        for row in rows:
            tree.insert("", tk.END, values=row)

    except:
        messagebox.showerror("Error", "Enter a valid number")

root = tk.Tk()
root.title("Student Database GUI")
root.geometry("700x500")


label_name = tk.Label(root, text="Student Name")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()


label_score = tk.Label(root, text="Student Score")
label_score.pack()

entry_score = tk.Entry(root)
entry_score.pack()


btn_insert = tk.Button(root, text="Add Student", command=insert_student)
btn_insert.pack(pady=10)


tree = ttk.Treeview(root, columns=("ID", "Name", "Score"), show="headings")

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Score", text="Score")

tree.pack(fill=tk.BOTH, expand=True)


filter_label = tk.Label(root, text="Show students with score higher than:")
filter_label.pack(pady=5)

filter_entry = tk.Entry(root)
filter_entry.pack()

filter_button = tk.Button(root, text="Filter", command=filter_students)
filter_button.pack(pady=10)


show_students()


root.mainloop()


cursor.close()
conn.close()