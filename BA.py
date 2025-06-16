# banking_app.py
import tkinter as tk
from tkinter import messagebox
from account import Account
from savings_account import SavingsAccount
from current_account import CurrentAccount

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking App")
        self.root.configure(bg="#2E2E2E")  # Dark background
        self.accounts = {}
        self.create_widgets()

    def create_widgets(self):
        # Account Creation Frame
        create_frame = tk.Frame(self.root, bg="#D3D3D3", padx=10, pady=10)
        create_frame.pack(pady=10, padx=10, fill="x")

        tk.Label(create_frame, text="World Bank", font=("Arial", 14, "bold"), bg="#D3D3D3").pack()
        tk.Label(create_frame, text="Create Account", font=("Arial", 12), bg="#D3D3D3").pack()

        tk.Label(create_frame, text="Name:", bg="#D3D3D3").pack()
        self.name_entry = tk.Entry(create_frame)
        self.name_entry.pack()

        tk.Label(create_frame, text="Account No:", bg="#D3D3D3").pack()
        self.acc_no_entry = tk.Entry(create_frame)
        self.acc_no_entry.pack()

        tk.Label(create_frame, text="Initial Balance:", bg="#D3D3D3").pack()
        self.balance_entry = tk.Entry(create_frame)
        self.balance_entry.pack()

        self.acc_type = tk.StringVar(value="Savings")
        tk.Radiobutton(create_frame, text="Savings", variable=self.acc_type, value="Savings", bg="#D3D3D3").pack()
        tk.Radiobutton(create_frame, text="Current", variable=self.acc_type, value="Current", bg="#D3D3D3").pack()

        tk.Button(create_frame, text="Create Account", command=self.create_account, bg="#4CAF50", fg="white").pack(pady=5)

        # Actions Frame
        action_frame = tk.Frame(self.root, bg="#D3D3D3", padx=10, pady=10)
        action_frame.pack(pady=10, padx=10, fill="x")

        tk.Label(action_frame, text="Actions", font=("Arial", 12), bg="#D3D3D3").pack()
        tk.Label(action_frame, text="Amount:", bg="#D3D3D3").pack()
        self.amount_entry = tk.Entry(action_frame)
        self.amount_entry.pack()

        tk.Button(action_frame, text="Deposit", command=self.deposit, bg="#2196F3", fg="white").pack(side="left", padx=5)
        tk.Button(action_frame, text="Withdraw", command=self.withdraw, bg="#F44336", fg="white").pack(side="left", padx=5)
        tk.Button(action_frame, text="View Balance", command=self.view_balance, bg="#9C27B0", fg="white").pack(side="left", padx=5)

        # Output
        self.output = tk.Label(self.root, text="Results will appear here.", fg="#FFFFFF", bg="#2E2E2E", wraplength=300)
        self.output.pack(pady=10)

    def create_account(self):
        name = self.name_entry.get().strip()
        acc_no = self.acc_no_entry.get().strip()
        if not name or not acc_no:
            self.output.config(text="Name and Account No cannot be empty.")
            return
        try:
            balance = float(self.balance_entry.get())
            if balance < 0:
                self.output.config(text="Initial balance cannot be negative.")
                return
        except ValueError:
            self.output.config(text="Please enter a valid balance.")
            return

        is_savings = self.acc_type.get() == "Savings"
        if acc_no in self.accounts:
            self.output.config(text="Account number already exists.")
            return
        self.accounts[acc_no] = SavingsAccount(acc_no, balance) if is_savings else CurrentAccount(acc_no, balance)
        self.output.config(text=f"Account {acc_no} created for {name} with ${balance:.2f} as {'Savings' if is_savings else 'Current'}.")

    def deposit(self):
        acc_no = self.acc_no_entry.get().strip()
        if acc_no not in self.accounts:
            self.output.config(text="Account not found.")
            return
        try:
            amount = float(self.amount_entry.get())
            account = self.accounts[acc_no]
            success, message = account.deposit(amount)
            if success:
                messagebox.showinfo("Success", "Deposit successful!")
            self.output.config(text=message)
        except ValueError:
            self.output.config(text="Please enter a valid amount.")

    def withdraw(self):
        acc_no = self.acc_no_entry.get().strip()
        if acc_no not in self.accounts:
            self.output.config(text="Account not found.")
            return
        try:
            amount = float(self.amount_entry.get())
            account = self.accounts[acc_no]
            success, message = account.withdraw(amount)
            if success:
                messagebox.showinfo("Success", "Withdrawal successful!")
            self.output.config(text=message)
        except ValueError:
            self.output.config(text="Please enter a valid amount.")

    def view_balance(self):
        acc_no = self.acc_no_entry.get().strip()
        if acc_no not in self.accounts:
            self.output.config(text="Account not found.")
            return
        account = self.accounts[acc_no]
        self.output.config(text=f"Balance for account {acc_no}: ${account.balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
  # ui_enhancements.py
import tkinter as tk
from tkinter import messagebox

def enhance_ui(app):
    # Add a clear button to reset input fields
    clear_button = tk.Button(app.root, text="Clear Fields", command=lambda: clear_fields(app), bg="#FF9800", fg="white")
    clear_button.pack(pady=5)

    # Add a status bar
    status_bar = tk.Label(app.root, text="Ready", bd=1, relief="sunken", anchor="w", bg="#D3D3D3")
    status_bar.pack(side="bottom", fill="x")

def clear_fields(app):
    app.name_entry.delete(0, tk.END)
    app.acc_no_entry.delete(0, tk.END)
    app.balance_entry.delete(0, tk.END)
    app.amount_entry.delete(0, tk.END)
    app.output.config(text="Fields cleared.")
