import tkinter as tk
from tkinter import messagebox
import json


class Contact:
    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["first_name"], data["last_name"], data["email"], data["phone"])

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Email: {self.email}, Phone: {self.phone}"


class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Contact List")
        self.contacts = []

        self.load_contacts()

        # Frames
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(pady=10)

        # Input Fields
        tk.Label(self.input_frame, text="First Name:").grid(row=0, column=0, padx=5, pady=5)
        self.first_name_entry = tk.Entry(self.input_frame)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Last Name:").grid(row=1, column=0, padx=5, pady=5)
        self.last_name_entry = tk.Entry(self.input_frame)
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.input_frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Phone:").grid(row=3, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.input_frame)
        self.phone_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        self.add_button = tk.Button(self.input_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Selected", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Search Contacts", command=self.search_contacts)
        self.search_button.pack(pady=5)

        self.save_button = tk.Button(self.root, text="Save Contacts", command=self.save_contacts)
        self.save_button.pack(pady=5)

        # Contact List Display
        self.contact_listbox = tk.Listbox(self.list_frame, width=60, height=15)
        self.contact_listbox.pack(padx=10, pady=10)

    def add_contact(self):
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if first_name and last_name and email and phone:
            new_contact = Contact(first_name, last_name, email, phone)
            self.contacts.append(new_contact)
            self.clear_entries()
            self.view_contacts()
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
            contact_index = selected[0]
            del self.contacts[contact_index]
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
        with open("contacts.json", "w") as file:
            json_contacts = [contact.to_dict() for contact in self.contacts]
            json.dump(json_contacts, file)
        messagebox.showinfo("Success", "Contacts saved successfully!")

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                json_contacts = json.load(file)
                self.contacts = [Contact.from_dict(data) for data in json_contacts]
        except FileNotFoundError:
            self.contacts = []


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
