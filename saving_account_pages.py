import streamlit as st
from savings_account import SavingsAccount

def main():
    st.title("Savings Account Page")
    st.session_state.accounts = st.session_state.get('accounts', {})

    account_no = st.text_input("Account No", key="savings_acc_no")
    amount = st.number_input("Amount", min_value=0.0, step=0.01, key="savings_amount")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Deposit"):
            if account_no in st.session_state.accounts:
                success, message = st.session_state.accounts[account_no].deposit(amount)
                if success:
                    st.success(message)
                    st.info("Deposit successful!")
                else:
                    st.error(message)
            else:
                st.error("Account not found.")
    with col2:
        if st.button("Withdraw"):
            if account_no in st.session_state.accounts:
                success, message = st.session_state.accounts[account_no].withdraw(amount)
                if success:
                    st.success(message)
                else:
                    st.error(message)
            else:
                st.error("Account not found.")

if __name__ == "__main__":
    main()