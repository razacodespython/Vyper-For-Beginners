import streamlit as st
from web3_script import *

st.title('Web3 Contract Interaction')

st.header('Function: changeNumber')
_num = st.number_input('Enter _num', step=1, key='changeNumber__num')
if st.button('Execute changeNumber', key='changeNumber_button'):
    result = changeNumber(_num)
    st.write(f'Result: {result}')

st.header('Function: changeGreet')
_greet = st.text_input('Enter _greet', key='changeGreet__greet')
if st.button('Execute changeGreet', key='changeGreet_button'):
    result = changeGreet(_greet)
    st.write(f'Result: {result}')

st.header('Function: my_number')
if st.button('Execute my_number', key='my_number_button'):
    result = my_number()
    st.write(f'Result: {result}')

st.header('Function: greet')
if st.button('Execute greet', key='greet_button'):
    result = greet()
    st.write(f'Result: {result}')

