import csv
import os
import tkinter as tk
from tkinter import messagebox
from datetime import date

filepath = os.path.join(os.path.expanduser("~"), "FinTracker", "data", "transactions.csv")

def initialize_transactions_file():
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(filepath):
        with open(filepath, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Income", "Expense"])

def add_data():
    initialize_transactions_file()
    global in_text, ex_text, add_window

    add_window = tk.Tk()
    add_window.title("Add Data")
    add_window.geometry("218x108+100+300")
    add_window.resizable(False,False)
    
    in_label = tk.Label(add_window, text="Income:")
    in_label.grid(column=0, row=0, padx=10, pady=10, sticky="w")

    ex_label = tk.Label(add_window, text="Expense:")
    ex_label.grid(column=0, row=1, padx=10, pady=[0,10], sticky="w")

    in_text = tk.Entry(add_window, width=22)
    in_text.grid(column=1, row=0, padx=[0,10], pady=10)

    ex_text = tk.Entry(add_window, width=22)
    ex_text.grid(column=1, row=1, padx=[0,10], pady=[0,10])

    submit_button = tk.Button(add_window, text="Submit", width=10, command=submit)
    submit_button.grid(column=0, row=2, padx=10, pady=[0,10], columnspan=2)

    add_window.mainloop()

def refresh():
    initialize_transactions_file()
    total_in = 0.0
    total_ex = 0.0

    try:
        with open(filepath, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                total_in += float(row[1]) if row[1] else 0
                total_ex += float(row[2]) if row[2] else 0
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while reading the file: {e}")

    total = total_in - total_ex
    text_box.config(state="normal")
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, f"Balance: {total}\n")
    text_box.insert(tk.END, f"\nTotal Income:  {total_in}")
    text_box.insert(tk.END, f"\nTotal Expense: {total_ex}")
    text_box.config(state="disabled")

def view_data():
    try:
        if os.name == "nt":
            os.startfile(filepath)
        elif os.name == "posix":
            if os.system(f"open {filepath}") != 0:
                os.system(f"xdg-open {filepath}")
        else:
            messagebox.showerror("Error", "Unsupported operating system.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def submit():
    amount_in = in_text.get()
    amount_ex = ex_text.get()
    
    try:
        amount_in = float(amount_in) if amount_in else 0
        amount_ex = float(amount_ex) if amount_ex else 0
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")
        return

    try:
        with open(filepath, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date.today(), amount_in, amount_ex])
            messagebox.showinfo("Success", "Data added successfully!")
            add_window.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while writing to the file: {e}")

    refresh()

if __name__ == "__main__":
    initialize_transactions_file()
    
    main = tk.Tk()
    main.title("FinTracker")
    main.geometry("354x118+100+100")
    main.resizable(False,False)

    add_button = tk.Button(main, text="Add", width=10, command=add_data)
    add_button.grid(column=0, row= 0, padx=10, pady=10)

    refresh_button = tk.Button(main, text="Refresh", width=10, command=refresh)
    refresh_button.grid(column=0, row=1, padx=10, pady=[0,10])

    view_data_button = tk.Button(main, text="View Data", width=10, command=view_data)
    view_data_button.grid(row=2, columnspan=2, pady=[0,10])

    text_box = tk.Text(main, height=4, width=30, state="disabled")
    text_box.grid(column=1, row=0, rowspan=2, padx=[0,10])
    refresh()

    main.mainloop()