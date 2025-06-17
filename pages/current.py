import streamlit as st 
from current_account import CurrentAccount
st.set_page_config(
    page_title="Bank App - Current",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)
current = CurrentAccount(100000)
with st.form("current_form"):
    st.title("Current Account Management")
    amount = st.number_input("Enter amount")
    operations = st.selectbox(('Deposit or Withdraw'), ("deposit", "withdraw", "transfer"))
    submit = st.form_submit_button('submit')

    if submit:
        if operations == "deposit":
            current.deposit(amount)
            st.success(f"Deposited {amount} successfully! New balance is {current.balance}")

        elif operations == "withdraw":
            with st.spinner("Processing withdrawal... Please wait."):
                if amount <= current.balance:
                    current.withdraw(amount)
                    st.write(f"Your balance is {current.balance}")
                else:
                    st.write("Insufficient balance for withdrawal.")
        elif operations == "transfer":
            st.write("Transfer functionality is not implemented yet.")
        else:
            st.write("Invalid operation selected.")
    if submit and operations == 'deposit':
        with st.spinner("Processing deposit... Please wait."):
            current.deposit(amount)
            st.write(f"Your balance is {current.balance}")  
