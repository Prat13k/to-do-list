import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("To-do-list")
app.geometry("400x400")

tasks = []

def update_task():
    task_list.delete(0,tk.END)
    for task in tasks:
        task_list.insert(tk.END,task)

def add_task():
    task = task_entry.get()
    if task.strip():
        tasks.append(task)
        update_task()
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("No task selected !!")

def clear_task():
    if messagebox.askyesno("Confirm ?"):
        tasks.clear()
        update_task()

def remove_task():
    try:
        selected_task  = task_list.curselection()[0]
        tasks.pop(selected_task)
        update_task()
    except IndexError:
        messagebox.showwarning("No task selected")

title_label = tk.Label(app, text = "To-do-list", font = ("Arial",16))
title_label.pack(pady = 10)

frame =tk.Frame(app)
frame.pack(pady = 10)

task_entry = tk.Entry(frame,width = 30, font = ("Arial",14))
task_entry.pack(side = tk.LEFT, padx = 5)

task_list = tk.Listbox(app, width = 40, height = 15, font=("Arial",12),
                       selectmode = tk.SINGLE)
task_list.pack(pady=10)

add_button = tk.Button(frame,text = "add task", command = add_task,
                       font=("Arial",12))
add_button.pack(side = tk.LEFT,padx=5)

remove_button = tk.Button(frame,text = "remove task", command = remove_task,
                       font=("Arial",12))
remove_button.pack(pady=10)

clear_button = tk.Button(frame,text = "clear task", command = clear_task,
                       font=("Arial",12))
clear_button.pack(pady=10)

app.mainloop()
