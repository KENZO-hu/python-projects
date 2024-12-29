import tkinter as tk
from tkinter import ttk, messagebox

class StudentBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Board")
        
        # Input labels and entry boxes
        self.labels = ["First Name", "Last Name", "Student Code", "Graduation Year"]
        self.entries = {}

        for i, label in enumerate(self.labels):
            tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(root, width=25)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label] = entry

        # Add button
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.grid(row=len(self.labels), column=0, columnspan=2, pady=10)

        # Table for displaying student records
        self.table = ttk.Treeview(root, columns=self.labels, show="headings", height=8)
        for label in self.labels:
            self.table.heading(label, text=label)
            self.table.column(label, width=100)
        self.table.grid(row=len(self.labels) + 1, column=0, columnspan=2, pady=10)

    def add_student(self):
        """Add a new student to the table."""
        values = [self.entries[label].get().strip() for label in self.labels]

        if any(not value for value in values):
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        self.table.insert("", tk.END, values=values)

        # Clear the input fields
        for entry in self.entries.values():
            entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Student added successfully!")

# Create and run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentBoard(root)
    root.mainloop()
