import streamlit as st
from savings_account import SavingsAccount
from current_account import CurrentAccount

class BankingApp:
    def __init__(self):
        self.accounts = {}

    def run(self):
        st.title("Banking App")
        st.header("World Bank")

        # Account Creation
        st.subheader("Create Account")
        with st.form(key="create_account"):
            name = st.text_input("Name")
            account_no = st.text_input("Account No")
            initial_balance = st.number_input("Initial Balance", min_value=0.0, step=0.01)
            account_type = st.radio("Account Type", ["Savings", "Current"])
            if st.form_submit_button("Create Account"):
                if not account_no or not name:
                    st.error("Name and Account No are required.")
                else:
                    account = SavingsAccount(account_no, initial_balance) if account_type == "Savings" else CurrentAccount(account_no, initial_balance)
                    self.accounts[account_no] = account
                    st.success(f"Account {account_no} created for {name} with ${initial_balance:.2f} as {account_type}.")

        # Balance Overview
        st.subheader("Balance Overview")
        account_no = st.text_input("Account No to View", key="view_acc_no")
        if st.button("View Balance"):
            if account_no in self.accounts:
                st.success(f"Balance for {account_no}: ${self.accounts[account_no].get_balance():.2f}")
            else:
                st.error("Account not found.")

if __name__ == "__main__":
    app = BankingApp()
    app.run()