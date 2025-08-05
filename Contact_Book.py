

import tkinter as tk
from tkinter import messagebox, simpledialog

# List to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        contacts.append(contact)
        update_contact_list()
        clear_entries()
        messagebox.showinfo("Success", f"Contact '{name}' added!")
    else:
        messagebox.showwarning("Input Error", "Name and phone are required!")

# Function to display all contacts
def update_contact_list():
    listbox.delete(0, tk.END)
    for i, contact in enumerate(contacts, start=1):
        listbox.insert(tk.END, f"{i}. {contact['name']} - {contact['phone']}")

# Function to clear all entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Function to view selected contact
def view_selected_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        messagebox.showinfo("Contact Details",
            f"Name: {contact['name']}\n"
            f"Phone: {contact['phone']}\n"
            f"Email: {contact['email']}\n"
            f"Address: {contact['address']}"
        )
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to view.")

# Function to delete selected contact
def delete_selected_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        name = contacts[index]["name"]
        contacts.pop(index)
        update_contact_list()
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted.")
    else:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

# Function to search contact by name
def search_contact():
    keyword = simpledialog.askstring("Search", "Enter name or phone to search:")
    if keyword:
        for contact in contacts:
            if keyword.lower() in contact["name"].lower() or keyword in contact["phone"]:
                messagebox.showinfo("Contact Found",
                    f"Name: {contact['name']}\n"
                    f"Phone: {contact['phone']}\n"
                    f"Email: {contact['email']}\n"
                    f"Address: {contact['address']}"
                )
                return
        messagebox.showwarning("Not Found", "No contact found with that keyword.")

# GUI setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x500")

# Labels and Entry fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack()

# Buttons
tk.Button(root, text="Add Contact", width=20, command=add_contact).pack(pady=5)
tk.Button(root, text="View Contact Details", width=20, command=view_selected_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", width=20, command=delete_selected_contact).pack(pady=5)
tk.Button(root, text="Search Contact", width=20, command=search_contact).pack(pady=5)

# Listbox to show contacts
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Start GUI loop
root.mainloop()
