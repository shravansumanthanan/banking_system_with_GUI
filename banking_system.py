import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime

class Admin:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_account(self, account_details):
        cursor = self.db_connection.cursor()
        query = "INSERT INTO customers (name, balance, gender, city, phone_number, age, country, dob) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, account_details)
        self.db_connection.commit()
        cursor.close()

    def update_account(self, account_id, new_details):
        cursor = self.db_connection.cursor()
        query = "UPDATE customers SET name = %s, balance = %s, gender = %s, city = %s, phone_number = %s, age = %s, country = %s, dob = %s WHERE id = %s"
        cursor.execute(query, new_details + (account_id,))
        self.db_connection.commit()
        cursor.close()

    def delete_account(self, account_id):
        cursor = self.db_connection.cursor()
        query = "DELETE FROM customers WHERE id = %s"
        cursor.execute(query, (account_id,))
        self.db_connection.commit()
        cursor.close()

    def view_all_accounts(self):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM customers"
        cursor.execute(query)
        accounts = cursor.fetchall()
        cursor.close()
        return accounts

    def add_user_record(self, user_details):
        cursor = self.db_connection.cursor()
        query = "INSERT INTO customers (name, balance, gender, city, phone_number, age, country, dob) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, user_details)
        self.db_connection.commit()
        cursor.close()

    def search_user_record(self, search_term):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM customers WHERE name LIKE %s OR city LIKE %s OR phone_number LIKE %s OR country LIKE %s"
        cursor.execute(query, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
        results = cursor.fetchall()
        cursor.close()
        return results

    def is_valid_phone_number(self, phone_number, country_code):
        # Implement phone number validation logic here
        return True

    def is_valid_age_and_city(self, dob, city):
        # Implement age and city validation logic here
        return True

class Customer:
    def __init__(self, db_connection, account_id):
        self.db_connection = db_connection
        self.account_id = account_id

    def deposit(self, amount):
        cursor = self.db_connection.cursor()
        query = "UPDATE customers SET balance = balance + %s WHERE id = %s"
        cursor.execute(query, (amount, self.account_id))
        self.db_connection.commit()
        cursor.close()

    def withdraw(self, amount):
        cursor = self.db_connection.cursor()
        query = "UPDATE customers SET balance = balance - %s WHERE id = %s"
        cursor.execute(query, (amount, self.account_id))
        self.db_connection.commit()
        cursor.close()

    def balance_inquiry(self):
        cursor = self.db_connection.cursor()
        query = "SELECT balance FROM customers WHERE id = %s"
        cursor.execute(query, (self.account_id,))
        balance = cursor.fetchone()[0]
        cursor.close()
        return balance

def visualize_data(db_connection):
    cursor = db_connection.cursor()
    query = "SELECT balance FROM customers"
    cursor.execute(query)
    balances = cursor.fetchall()
    cursor.close()

    balances = [balance[0] for balance in balances]
    plt.hist(balances, bins=10)
    plt.xlabel('Balance')
    plt.ylabel('Number of Customers')
    plt.title('Customer Balance Distribution')
    plt.show()

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def binary_search(arr, x):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            l = mid + 1

        else:
            r = mid - 1

    return -1

def main():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="banking_system"
    )

    root = tk.Tk()
    root.title("Banking Management System")

    def login():
        user_type = user_type_var.get()
        account_id = account_id_entry.get()
        if user_type == "Admin":
            admin = Admin(db_connection)
            admin_window(admin)
        elif user_type == "Customer":
            customer = Customer(db_connection, account_id)
            customer_window(customer)
        else:
            messagebox.showerror("Error", "Invalid user type")

    def admin_window(admin):
        admin_win = tk.Toplevel(root)
        admin_win.title("Admin Dashboard")

        def create_account():
            name = name_entry.get()
            balance = balance_entry.get()
            gender = gender_entry.get()
            city = city_entry.get()
            phone_number = phone_number_entry.get()
            age = age_entry.get()
            country = country_entry.get()
            dob = dob_entry.get()
            admin.create_account((name, balance, gender, city, phone_number, age, country, dob))
            messagebox.showinfo("Success", "Account created successfully")

        def update_account():
            account_id = account_id_entry.get()
            name = name_entry.get()
            balance = balance_entry.get()
            gender = gender_entry.get()
            city = city_entry.get()
            phone_number = phone_number_entry.get()
            age = age_entry.get()
            country = country_entry.get()
            dob = dob_entry.get()
            admin.update_account(account_id, (name, balance, gender, city, phone_number, age, country, dob))
            messagebox.showinfo("Success", "Account updated successfully")

        def delete_account():
            account_id = account_id_entry.get()
            admin.delete_account(account_id)
            messagebox.showinfo("Success", "Account deleted successfully")

        def view_all_accounts():
            accounts = admin.view_all_accounts()
            accounts_text.delete(1.0, tk.END)
            for account in accounts:
                accounts_text.insert(tk.END, f"ID: {account[0]}, Name: {account[1]}, Balance: {account[2]}, Gender: {account[3]}, City: {account[4]}, Phone Number: {account[5]}, Age: {account[6]}, Country: {account[7]}, DOB: {account[8]}\n")

        tk.Label(admin_win, text="Account ID").grid(row=0, column=0)
        account_id_entry = tk.Entry(admin_win)
        account_id_entry.grid(row=0, column=1)

        tk.Label(admin_win, text="Name").grid(row=1, column=0)
        name_entry = tk.Entry(admin_win)
        name_entry.grid(row=1, column=1)

        tk.Label(admin_win, text="Balance").grid(row=2, column=0)
        balance_entry = tk.Entry(admin_win)
        balance_entry.grid(row=2, column=1)

        tk.Label(admin_win, text="Gender").grid(row=3, column=0)
        gender_entry = tk.Entry(admin_win)
        gender_entry.grid(row=3, column=1)

        tk.Label(admin_win, text="City").grid(row=4, column=0)
        city_entry = tk.Entry(admin_win)
        city_entry.grid(row=4, column=1)

        tk.Label(admin_win, text="Phone Number").grid(row=5, column=0)
        phone_number_entry = tk.Entry(admin_win)
        phone_number_entry.grid(row=5, column=1)

        tk.Label(admin_win, text="Age").grid(row=6, column=0)
        age_entry = tk.Entry(admin_win)
        age_entry.grid(row=6, column=1)

        tk.Label(admin_win, text="Country").grid(row=7, column=0)
        country_entry = tk.Entry(admin_win)
        country_entry.grid(row=7, column=1)

        tk.Label(admin_win, text="DOB").grid(row=8, column=0)
        dob_entry = tk.Entry(admin_win)
        dob_entry.grid(row=8, column=1)

        tk.Button(admin_win, text="Create Account", command=create_account).grid(row=9, column=0)
        tk.Button(admin_win, text="Update Account", command=update_account).grid(row=9, column=1)
        tk.Button(admin_win, text="Delete Account", command=delete_account).grid(row=10, column=0)
        tk.Button(admin_win, text="View All Accounts", command=view_all_accounts).grid(row=10, column=1)

        accounts_text = tk.Text(admin_win, height=10, width=50)
        accounts_text.grid(row=11, column=0, columnspan=2)

    def customer_window(customer):
        customer_win = tk.Toplevel(root)
        customer_win.title("Customer Dashboard")

        def deposit():
            amount = amount_entry.get()
            customer.deposit(amount)
            messagebox.showinfo("Success", "Amount deposited successfully")

        def withdraw():
            amount = amount_entry.get()
            customer.withdraw(amount)
            messagebox.showinfo("Success", "Amount withdrawn successfully")

        def balance_inquiry():
            balance = customer.balance_inquiry()
            messagebox.showinfo("Balance", f"Your balance is: {balance}")

        tk.Label(customer_win, text="Amount").grid(row=0, column=0)
        amount_entry = tk.Entry(customer_win)
        amount_entry.grid(row=0, column=1)

        tk.Button(customer_win, text="Deposit", command=deposit).grid(row=1, column=0)
        tk.Button(customer_win, text="Withdraw", command=withdraw).grid(row=1, column=1)
        tk.Button(customer_win, text="Balance Inquiry", command=balance_inquiry).grid(row=2, column=0, columnspan=2)

    tk.Label(root, text="User Type").grid(row=0, column=0)
    user_type_var = tk.StringVar()
    user_type_var.set("Admin")
    tk.OptionMenu(root, user_type_var, "Admin", "Customer").grid(row=0, column=1)

    tk.Label(root, text="Account ID").grid(row=1, column=0)
    account_id_entry = tk.Entry(root)
    account_id_entry.grid(row=1, column=1)

    tk.Button(root, text="Login", command=login).grid(row=2, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
