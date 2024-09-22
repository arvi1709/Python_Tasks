import tkinter as tk
from tkinter import messagebox
import requests

def get_exchange_rate(from_currency, to_currency, amount):
    try:
        url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
        response = requests.get(url)
        data = response.json()
        rate = data['rates'].get(to_currency)
        if rate is None:
            raise ValueError("Currency conversion rate not available")
        return amount * rate
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def convert():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_entry.get().upper()
        to_currency = to_currency_entry.get().upper()

        converted_amount = get_exchange_rate(from_currency, to_currency, amount)
        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid inputs.")

root = tk.Tk()
root.title("Currency Converter")

tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="From Currency:").grid(row=1, column=0, padx=10, pady=10)
from_currency_entry = tk.Entry(root)
from_currency_entry.grid(row=1, column=1)

tk.Label(root, text="To Currency:").grid(row=2, column=0, padx=10, pady=10)
to_currency_entry = tk.Entry(root)
to_currency_entry.grid(row=2, column=1)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result will be displayed here")
result_label.grid(row=4, column=0, columnspan=2, pady=10)


root.mainloop()
