import calendar , datetime 
calendar.setfirstweekday(calendar.SATURDAY)
dt = datetime.datetime.now()
day_name = dt.strftime("%A")
import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry.get()
    task_description = entry_description.get()
    if task:
        if completed_var.get() == 1:
            completed_listbox.insert(tk.END, task + " - " + task_description)
        else:
            not_completed_listbox.insert(tk.END, task + " - " + task_description)
        entry.delete(0, tk.END)
        entry_description.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task(listbox):
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")
    
def edit_task():
    try:
        index = not_completed_listbox.curselection()[0]
        task = not_completed_listbox.get(index)
        task_name, task_description = task.split(" - ")
        entry.delete(0, tk.END)
        entry.insert(0, task_name)
        entry_description.delete(0, tk.END)
        entry_description.insert(0, task_description)
        not_completed_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

root = tk.Tk()
root.minsize(height=800 , width=1000)
root.title("To-Do App")
root.geometry("400x400")
root.configure(bg="#f0f0f0")



# Frame for welcome text
welcome_frame = tk.Frame(root, bg="#FFF8DC", padx=10, pady=10)
welcome_frame.pack(pady=10)

# Welcome text
welcome_label = tk.Label(root, text=f"Welcome to the To-Do App .\nNow, you can manage your {day_name}'s tasks.", font=("Arial", 16), bg="#FFFFFF")
welcome_label.pack(pady=10)

# Entry for task name
entry_label = tk.Label(root, text="Task Name:", font=("Arial", 12), bg="#f0f0f0")
entry_label.pack()


# Entry for adding/editing tasks
entry = tk.Entry(root, width=60, font=("Arial", 12), bg="white", bd=1, relief=tk.SOLID)
entry.pack(pady=10)

# Entry for task description
entry_description_label = tk.Label(root, text="Task Description:", font=("Arial", 12), bg="#f0f0f0")
entry_description_label.pack()

entry_description = tk.Entry(root, width=60, font=("Arial", 12), bg="white", bd=1, relief=tk.SOLID)
entry_description.pack(pady=5)

# Checkbox for marking task as completed
completed_var = tk.IntVar()
completed_checkbox = tk.Checkbutton(root, text="Mark as Completed", variable=completed_var, bg="#f0f0f0")
completed_checkbox.pack()


# Add Task, Edit Task, and Delete Task buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, width=10, font=("Arial", 10), bg="#D3D3D3", fg="black")
add_button.pack(side=tk.LEFT, padx=5)

edit_button = tk.Button(button_frame, text="Edit Task", command=edit_task, width=10, font=("Arial", 10), bg="#D3D3D3", fg="black")
edit_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=lambda: delete_task(not_completed_listbox), width=10, font=("Arial", 10), bg="#FF0000", fg="white")
delete_button.pack(side=tk.LEFT, padx=5)

delete_completed_button = tk.Button(button_frame, text="Delete Completed Task", command=lambda: delete_task(completed_listbox), width=20, font=("Arial", 10), bg="#FF0000", fg="white")
delete_completed_button.pack(side=tk.LEFT, padx=5)

#delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, width=10, font=("Arial", 10), bg="#F44336", fg="black")
#delete_button.pack(side=tk.LEFT, padx=5)

# Frame for tasks
tasks_frame = tk.Frame(root, bg="#f0f0f0")
tasks_frame.pack(pady=10)

# Labels for task categories
completed_label = tk.Label(tasks_frame, text="Completed Tasks", font=("Arial", 12), bg="#f0f0f0")
completed_label.grid(row=0, column=1, padx=10)


not_completed_label = tk.Label(tasks_frame, text="Not Completed Tasks", font=("Arial", 12), bg="#f0f0f0")
not_completed_label.grid(row=0, column=0, padx=10)

# Listbox for not completed tasks
not_completed_listbox = tk.Listbox(tasks_frame, width=39, height=10, font=("Arial", 12), bg="white", bd=2, relief=tk.SOLID)
not_completed_listbox.grid(row=1, column=0, padx=10)

# Listbox for completed tasks
completed_listbox = tk.Listbox(tasks_frame, width=39, height=10, font=("Arial", 12), bg="white", bd=2, relief=tk.SOLID)
completed_listbox.grid(row=1, column=1, padx=10)


root.mainloop()
