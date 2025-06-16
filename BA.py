# Header: Contributed by Member 1 (David Ekoja)
import streamlit as st

class Account:
    def __init__(self, account_no, balance=0, withdrawal_limit=None):
        self.account_no = account_no
        self.balance = balance
        self.withdrawal_limit = withdrawal_limit if withdrawal_limit is not None else float('inf')

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False, "Invalid deposit amount. Please enter a positive number."
        self.balance += amount
        return True, f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False, "Invalid withdrawal amount. Please enter a positive number."
        if amount > self.withdrawal_limit:
            return False, f"Withdrawal amount exceeds limit of ${self.withdrawal_limit:.2f}."
        if amount > self.balance:
            return False, "Insufficient funds."
        self.balance -= amount
        return True, f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"

class BankingApp:
    def __init__(self):
        self.accounts = {}

    def run(self):
        st.title("Banking App")
        st.header("World Bank")
