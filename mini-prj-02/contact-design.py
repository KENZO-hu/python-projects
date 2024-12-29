import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Contact:
    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Email: {self.email}, Phone: {self.phone}"


class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f8ff")

        self.contacts = []

        # Input Frame
        self.input_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.input_frame.pack(pady=10)

        # Input Fields
        self.create_label_and_entry("First Name", 0)
        self.create_label_and_entry("Last Name", 1)
        self.create_label_and_entry("Email", 2)
        self.create_label_and_entry("Phone", 3)

        # Buttons
        self.buttons_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.buttons_frame.pack(pady=10)

        self.create_button("Add Contact", self.add_contact)
        self.create_button("View Contacts", self.view_contacts)
        self.create_button("Delete Selected", self.delete_contact)
        self.create_button("Search Contacts", self.search_contacts)
        self.create_button("Save Contacts", self.save_contacts)

        # Contact List Display
        self.listbox_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.listbox_frame.pack(pady=20)

        self.contact_listbox = tk.Listbox(self.listbox_frame, width=50, height=15, font=("Arial", 12))
        self.contact_listbox.pack(side="left", padx=5)
        self.scrollbar = ttk.Scrollbar(self.listbox_frame, orient="vertical", command=self.contact_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.contact_listbox.config(yscrollcommand=self.scrollbar.set)

    def create_label_and_entry(self, label_text, row):
        tk.Label(self.input_frame, text=label_text + ":", bg="#f0f8ff", font=("Arial", 10)).grid(row=row, column=0, padx=5, pady=5, sticky="w")
        entry = tk.Entry(self.input_frame, width=30, font=("Arial", 10))
        entry.grid(row=row, column=1, padx=5, pady=5)
        setattr(self, f"{label_text.lower().replace(' ', '_')}_entry", entry)

    def create_button(self, text, command):
        tk.Button(self.buttons_frame, text=text, command=command, bg="#4682b4", fg="white", font=("Arial", 10), padx=10, pady=5).pack(side="left", padx=5)

    def add_contact(self):
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if first_name and last_name and email and phone:
            new_contact = Contact(first_name, last_name, email, phone)
            self.contacts.append(new_contact)
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def view_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        if not self.contacts:
            self.contact_listbox.insert(tk.END, "No contacts available.")
        else:
            for contact in self.contacts:
                self.contact_listbox.insert(tk.END, str(contact))

    def delete_contact(self):
        selected = self.contact_listbox.curselection()
        if selected:
            del self.contacts[selected[0]]
            self.view_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")

    def search_contacts(self):
        query = self.first_name_entry.get().strip().lower()
        self.contact_listbox.delete(0, tk.END)
        if not query:
            self.view_contacts()
            return
        results = [contact for contact in self.contacts if query in contact.first_name.lower()]
        if results:
            for contact in results:
                self.contact_listbox.insert(tk.END, str(contact))
        else:
            self.contact_listbox.insert(tk.END, "No matching contacts found.")

    def clear_entries(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def save_contacts(self):
        # Placeholder for saving functionality
        messagebox.showinfo("Save", "Save functionality is not implemented yet!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
