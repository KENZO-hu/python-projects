import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kenzo Contact App")
        self.root.geometry("400x600")
        
        # Header with logo
        self.header_frame = tk.Frame(self.root, bg="#128C7E", height=80)
        self.header_frame.pack(fill=tk.X)

        # Load and display logo
        try:
            self.logo = Image.open("kenzo_logo.png")  # Ensure 'kenzo_logo.png' is in the same directory
            self.logo = self.logo.resize((50, 50), Image.ANTIALIAS)
            self.logo_img = ImageTk.PhotoImage(self.logo)
            self.logo_label = tk.Label(self.header_frame, image=self.logo_img, bg="#128C7E")
            self.logo_label.pack(side=tk.LEFT, padx=10, pady=10)
        except Exception as e:
            print("Error loading logo:", e)

        self.header_label = tk.Label(self.header_frame, text="Kenzo Contacts", font=("Arial", 18, "bold"), bg="#128C7E", fg="white")
        self.header_label.pack(side=tk.LEFT, pady=10)

        # Contact List Frame
        self.contact_list_frame = tk.Frame(self.root, bg="white")
        self.contact_list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.contact_list_label = tk.Label(self.contact_list_frame, text="Contacts", font=("Arial", 14), bg="white")
        self.contact_list_label.pack()

        self.contact_listbox = tk.Listbox(self.contact_list_frame, width=30, height=20, bg="#ECE5DD", font=("Arial", 12))
        self.contact_listbox.pack(padx=10, pady=10)

        self.contact_listbox.bind('<<ListboxSelect>>', self.on_contact_select)

        # Contact Actions Frame
        self.contact_actions_frame = tk.Frame(self.root, bg="white")
        self.contact_actions_frame.pack(fill=tk.X, padx=10, pady=10)

        self.add_button = tk.Button(self.contact_actions_frame, text="Add Contact", command=self.add_contact, bg="#25D366", fg="white", font=("Arial", 12))
        self.add_button.pack(fill=tk.X, pady=5)

        self.call_button = tk.Button(self.contact_actions_frame, text="Make a Call", command=self.make_call, bg="#128C7E", fg="white", font=("Arial", 12), state=tk.DISABLED)
        self.call_button.pack(fill=tk.X, pady=5)

        self.discuss_button = tk.Button(self.contact_actions_frame, text="Discuss", command=self.discuss_with_contact, bg="#34B7F1", fg="white", font=("Arial", 12), state=tk.DISABLED)
        self.discuss_button.pack(fill=tk.X, pady=5)

        self.block_button = tk.Button(self.contact_actions_frame, text="Block Contact", command=self.block_contact, bg="#FF0000", fg="white", font=("Arial", 12), state=tk.DISABLED)
        self.block_button.pack(fill=tk.X, pady=5)

        self.contacts = {}

    def add_contact(self):
        def save_contact():
            name = name_entry.get()
            phone = phone_entry.get()

            if name and phone:
                self.contacts[name] = {"phone": phone, "blocked": False}
                self.contact_listbox.insert(tk.END, name)
                add_contact_window.destroy()
            else:
                messagebox.showerror("Error", "Both fields are required!")

        add_contact_window = tk.Toplevel(self.root)
        add_contact_window.title("Add Contact")

        tk.Label(add_contact_window, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(add_contact_window)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_contact_window, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
        phone_entry = tk.Entry(add_contact_window)
        phone_entry.grid(row=1, column=1, padx=5, pady=5)

        save_button = tk.Button(add_contact_window, text="Save", command=save_contact)
        save_button.grid(row=2, columnspan=2, pady=10)

    def on_contact_select(self, event):
        try:
            selected_contact = self.contact_listbox.get(self.contact_listbox.curselection())
            if selected_contact:
                self.call_button.config(state=tk.NORMAL)
                self.discuss_button.config(state=tk.NORMAL)
                self.block_button.config(state=tk.NORMAL)
        except tk.TclError:
            pass

    def make_call(self):
        selected_contact = self.contact_listbox.get(self.contact_listbox.curselection())
        contact = self.contacts[selected_contact]

        if contact["blocked"]:
            messagebox.showwarning("Blocked", f"Cannot call {selected_contact}. Contact is blocked.")
        else:
            messagebox.showinfo("Calling", f"Calling {selected_contact} at {contact['phone']}...")

    def discuss_with_contact(self):
        selected_contact = self.contact_listbox.get(self.contact_listbox.curselection())
        contact = self.contacts[selected_contact]

        if contact["blocked"]:
            messagebox.showwarning("Blocked", f"Cannot discuss with {selected_contact}. Contact is blocked.")
        else:
            chat_window = tk.Toplevel(self.root)
            chat_window.title(f"Chat with {selected_contact}")

            chat_area = tk.Text(chat_window, height=15, width=50)
            chat_area.pack(padx=5, pady=5)

            message_entry = tk.Entry(chat_window, width=40)
            message_entry.pack(side=tk.LEFT, padx=5, pady=5)

            send_button = tk.Button(chat_window, text="Send", command=lambda: chat_area.insert(tk.END, f"You: {message_entry.get()}\n"))
            send_button.pack(side=tk.RIGHT, padx=5, pady=5)

    def block_contact(self):
        selected_contact = self.contact_listbox.get(self.contact_listbox.curselection())
        self.contacts[selected_contact]["blocked"] = True
        messagebox.showinfo("Blocked", f"{selected_contact} has been blocked.")

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()
