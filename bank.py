import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

file = "bank_data.json"

try:
    with open(file, "r") as f:
        data = json.load(f)
        balance = data["balance"]
        transactions = data["transactions"]
except:
    balance = 0
    transactions = []

def save():
    with open(file, "w") as f:
        json.dump({
            "balance": balance,
            "transactions": transactions
        }, f, indent=4)
def update():
    balance_label.config(text=f"Balance: ₱{balance}")

    history.delete(0, tk.END)

    for item in transactions:
        history.insert(tk.END, item)

def deposit():
    global balance

    try:
        amount = float(entry.get())

        if amount <= 0:
            raise ValueError

        balance += amount

        transactions.append(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Deposited ₱{amount}"
        )

        save()
        update()

        messagebox.showinfo("Success", "Deposit Successful")

        entry.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Enter valid amount")
