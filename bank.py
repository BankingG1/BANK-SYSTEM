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