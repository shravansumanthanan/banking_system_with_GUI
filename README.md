# Banking Management System

## Project Description

This project is a banking management system implemented in Python. It provides functionalities for creating, updating, and deleting customer accounts, as well as performing basic banking operations such as deposit, withdrawal, and balance inquiry. The system uses MySQL to store customer data and transaction history. It also includes data visualization features using numpy and matplotlib, and a professional GUI for user interaction.

## Features

- Create, update, and delete customer accounts
- Perform basic banking operations: deposit, withdrawal, and balance inquiry
- Store customer data and transaction history in MySQL database
- Data visualization using numpy and matplotlib
- Professional GUI for user interaction
- Secure login and authentication for admin and customer accounts
- Role-based access control to restrict functionalities based on user type (admin or customer)

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/githubnext/workspace-blank.git
   cd workspace-blank
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:
   - Create a new MySQL database.
   - Run the `database_setup.sql` script to create the necessary tables.

4. Update the database connection settings in the `banking_system.py` file.

## Running the Project

1. Start the MySQL server.

2. Run the `banking_system.py` file to start the banking management system:
   ```
   python banking_system.py
   ```

3. Use the GUI to interact with the system.
