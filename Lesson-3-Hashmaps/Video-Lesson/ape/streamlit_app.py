import streamlit as st
from web3_script import *

st.title('Web3 Contract Interaction')

st.header('Function: add_days')
_day = st.text_input('Enter _day', key='add_days__day')
_value = st.number_input('Enter _value', step=1, key='add_days__value')
if st.button('Execute add_days', key='add_days_button'):
    result = add_days(_day, _value)
    st.write(f'Result: {result}')

st.header('Function: add_balance')
_amount = st.number_input('Enter _amount', step=1, key='add_balance__amount')
if st.button('Execute add_balance', key='add_balance_button'):
    result = add_balance(_amount)
    st.write(f'Result: {result}')

st.header('Function: add_balance_custom')
_wallet = st.text_input('Enter _wallet', key='add_balance_custom__wallet')
_amount = st.number_input('Enter _amount', step=1, key='add_balance_custom__amount')
if st.button('Execute add_balance_custom', key='add_balance_custom_button'):
    result = add_balance_custom(_wallet, _amount)
    st.write(f'Result: {result}')

st.header('Function: week')
arg0 = st.text_input('Enter arg0', key='week_arg0')
if st.button('Execute week', key='week_button'):
    result = week(arg0)
    st.write(f'Result: {result}')

st.header('Function: user_balances')
arg0 = st.text_input('Enter arg0', key='user_balances_arg0')
if st.button('Execute user_balances', key='user_balances_button'):
    result = user_balances(arg0)
    st.write(f'Result: {result}')

st.header('Function: user_address')
if st.button('Execute user_address', key='user_address_button'):
    result = user_address()
    st.write(f'Result: {result}')

