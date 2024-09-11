# FinTracker - Personal Finance Tracker
FinTracker is a simple personal finance tracking application built using Python and the tkinter library for a graphical user interface (GUI). It allows users to add, view, and manage basic financial transactions such as income and expenses. The data is stored in a CSV file for easy access and management.

## Features
- **Add Transactions**: Users can add new income and expenses.
- **View Data**: Easily view the transaction history in CSV format.
- **Refresh Balance**: Quickly calculate and display the total income, expenses, and balance.
- **Simple GUI**: Provides an intuitive interface to interact with the application.

## Requirements
- Python 3.x
- Tkinter (usually included with Python)
- csv and os modules (included with Python)

## How to Use
1. Download the ZIP File:
    - Go to the [Releases](https://github.com/NaldCapuno/FinTracker/releases) page on GitHub and download the latest release ZIP file.

2. Extract the ZIP File:
    - Extract the contents of the ZIP file to a directory of your choice.

3. Run the Application:
    - Open the **FinTracker.pyw** file directly in your file explorer. Double-click the file to run it using the default Python interpreter installed on your system.

## How it Works
Once the app is launched, you'll see the following options:
- **Add Data**: Opens a new window where you can input income (Amount In) and expenses (Amount Out). The data will be saved to transactions.csv.
- **Refresh**: Recalculates the total income, expenses, and current balance and displays the updated values.
- **View Data**: Opens the transactions.csv file for a detailed look at your transactions in your default spreadsheet editor.

![FinTracker](https://github.com/user-attachments/assets/c67d31d0-14e4-44c8-bc8a-75392e6b64e4)

## File Structure
- **FinTracker.pyw**: Main application script.
- **data/transactions.csv**: CSV file where transactions are stored.
