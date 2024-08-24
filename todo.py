# to do list app

import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, padx=(0, 10))

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=10)

        self.edit_button = tk.Button(self.button_frame, text="Edit Task", command=self.edit_task)
        self.edit_button.grid(row=0, column=1, padx=10)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=10)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def edit_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            new_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=self.tasks[selected_task_index])
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.listbox.delete(selected_task_index)
                self.listbox.insert(selected_task_index, new_task)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to edit.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()