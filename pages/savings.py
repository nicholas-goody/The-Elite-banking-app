import streamlit as st
from savings_account import SavingsAccount

st.set_page_config(
    page_title="Bank App - Savings",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

savings = SavingsAccount(200000)


with st.form("savings_form"):
    st.title("Savings Account Management")
    amount = st.number_input("Enter amount")
    operations = st.selectbox(('Deposit or Withdraw'), ("deposit","withdraw","transfer"))
    submit = st.form_submit_button('submit')

    if submit:
        if operations == "deposit":
            savings.deposit(amount)
            st.success(f"Deposited {amount} successfully! New balance is {savings.balance}")

        elif operations == "withdraw":
            with st.spinner("Processing withdrawal... Please wait."):

                if amount<= 10000 :
                    savings.withdraw(amount)
                    st.write(f"your balance is {savings.balance}")

                elif amount > savings.balance:
                    st.write("Insufficient balance for withdrawal.")

                else:
                    st.write("Withdrawal limit exceeded. Maximum withdrawal amount is 10,000.")
    

    if submit and operations == 'deposit' :
        with st.spinner("Processing deposit... Please wait."):
            savings.deposit(amount)
            st.write(f"your balance is {savings.balance}")

            

