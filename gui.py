import tkinter as tk
from tkinter import messagebox
from banking_system import Admin, Customer, visualize_data
from banking_system import Admin

class BankingGUI:
    def __init__(self, root, db_connection):
        self.root = root
        self.db_connection = db_connection
        self.root.title("Banking Management System")

        self.user_type_var = tk.StringVar()
        self.user_type_var.set("Admin")
        self.account_id_entry = tk.Entry(self.root)

        self.create_login_screen()

    def create_login_screen(self):
        tk.Label(self.root, text="User Type").grid(row=0, column=0)
        tk.OptionMenu(self.root, self.user_type_var, "Admin", "Customer").grid(row=0, column=1)

        tk.Label(self.root, text="Account ID").grid(row=1, column=0)
        self.account_id_entry.grid(row=1, column=1)

        tk.Button(self.root, text="Login", command=self.login).grid(row=2, column=0, columnspan=2)

    def login(self):
        user_type = self.user_type_var.get()
        account_id = self.account_id_entry.get()
        if user_type == "Admin":
            admin = Admin(self.db_connection)
            self.create_admin_window(admin)
        elif user_type == "Customer":
            customer = Customer(self.db_connection, account_id)
            self.create_customer_window(customer)
        else:
            messagebox.showerror("Error", "Invalid user type")

    def create_admin_window(self, admin):
        admin_win = tk.Toplevel(self.root)
        admin_win.title("Admin Dashboard")

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

        tk.Button(admin_win, text="Create Account", command=lambda: self.create_account(admin, name_entry, balance_entry, gender_entry, city_entry, phone_number_entry, age_entry, country_entry, dob_entry)).grid(row=9, column=0)
        tk.Button(admin_win, text="Update Account", command=lambda: self.update_account(admin, account_id_entry, name_entry, balance_entry, gender_entry, city_entry, phone_number_entry, age_entry, country_entry, dob_entry)).grid(row=9, column=1)
        tk.Button(admin_win, text="Delete Account", command=lambda: self.delete_account(admin, account_id_entry)).grid(row=10, column=0)
        tk.Button(admin_win, text="View All Accounts", command=lambda: self.view_all_accounts(admin)).grid(row=10, column=1)
        tk.Button(admin_win, text="Data Analysis", command=lambda: self.data_analysis(admin)).grid(row=11, column=0, columnspan=2)

        self.accounts_text = tk.Text(admin_win, height=10, width=50)
        self.accounts_text.grid(row=12, column=0, columnspan=2)

    def create_account(self, admin, name_entry, balance_entry, gender_entry, city_entry, phone_number_entry, age_entry, country_entry, dob_entry):
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

    def update_account(self, admin, account_id_entry, name_entry, balance_entry, gender_entry, city_entry, phone_number_entry, age_entry, country_entry, dob_entry):
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

    def delete_account(self, admin, account_id_entry):
        account_id = account_id_entry.get()
        admin.delete_account(account_id)
        messagebox.showinfo("Success", "Account deleted successfully")

    def view_all_accounts(self, admin):
        accounts = admin.view_all_accounts()
        self.accounts_text.delete(1.0, tk.END)
        for account in accounts:
            self.accounts_text.insert(tk.END, f"ID: {account[0]}, Name: {account[1]}, Balance: {account[2]}, Gender: {account[3]}, City: {account[4]}, Phone Number: {account[5]}, Age: {account[6]}, Country: {account[7]}, DOB: {account[8]}\n")

    def data_analysis(self, admin):
        results = admin.data_analysis()
        result_win = tk.Toplevel(self.root)
        result_win.title("Data Analysis Results")
        result_text = tk.Text(result_win, height=10, width=50)
        result_text.grid(row=0, column=0, columnspan=2)
        result_text.insert(tk.END, results)

    def create_customer_window(self, customer):
        customer_win = tk.Toplevel(self.root)
        customer_win.title("Customer Dashboard")

        tk.Label(customer_win, text="Amount").grid(row=0, column=0)
        amount_entry = tk.Entry(customer_win)
        amount_entry.grid(row=0, column=1)

        tk.Button(customer_win, text="Deposit", command=lambda: self.deposit(customer, amount_entry)).grid(row=1, column=0)
        tk.Button(customer_win, text="Withdraw", command=lambda: self.withdraw(customer, amount_entry)).grid(row=1, column=1)
        tk.Button(customer_win, text="Balance Inquiry", command=lambda: self.balance_inquiry(customer)).grid(row=2, column=0, columnspan=2)

    def deposit(self, customer, amount_entry):
        amount = amount_entry.get()
        customer.deposit(amount)
        messagebox.showinfo("Success", "Amount deposited successfully")

    def withdraw(self, customer, amount_entry):
        amount = amount_entry.get()
        customer.withdraw(amount)
        messagebox.showinfo("Success", "Amount withdrawn successfully")

    def balance_inquiry(self, customer):
        balance = customer.balance_inquiry()
        messagebox.showinfo("Balance", f"Your balance is: {balance}")

def main():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="banking_system"
    )

    root = tk.Tk()
    app = BankingGUI(root, db_connection)
    root.mainloop()

if __name__ == "__main__":
    main()
