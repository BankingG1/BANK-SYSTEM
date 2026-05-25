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

def withdraw():
    global balance

    try:
        amount = float(entry.get())

        if amount <= 0 or amount > balance:
            raise ValueError

        balance -= amount

        transactions.append(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Withdrew ₱{amount}"
        )

        save()
        update()

        messagebox.showinfo("Success", "Withdrawal Successful")

        entry.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Invalid or insufficient balance")

window = tk.Tk()

window.title("Banking System")
window.geometry("600x500")
window.config(bg="lightblue")

tk.Label(
    window,
    text="GUI Banking System",
    font=("Arial", 20, "bold"),
    bg="lightblue"
).pack(pady=10)

balance_label = tk.Label(
    window,
    text="Balance: ₱0",
    font=("Arial", 15),
    bg="lightblue",
    fg="green"
)

balance_label.pack(pady=5)

entry = tk.Entry(window, font=("Arial", 12), width=25)

entry.pack(pady=10)

tk.Button(
    window,
    text="Deposit",
    width=15,
    bg="green",
    fg="white",
    command=deposit
).pack(pady=5)

tk.Button(
    window,
    text="Withdraw",
    width=15,
    bg="red",
    fg="white",
    command=withdraw
).pack(pady=5)

tk.Button(
    window,
    text="Check Balance",
    width=15,
    bg="blue",
    fg="white",
    command=lambda:
    messagebox.showinfo(
        "Balance",
        f"Current Balance: ₱{balance}"
    )
).pack(pady=5)


