import streamlit as st
from web3_script import *

st.title('Web3 Contract Interaction')

st.header('Function: add_message')
_message = st.text_input('Enter _message', key='add_message__message')
if st.button('Execute add_message', key='add_message_button'):
    result = add_message(_message)
    st.write(f'Result: {result}')

st.header('Function: get_message')
_index = st.number_input('Enter _index', step=1, key='get_message__index')
if st.button('Execute get_message', key='get_message_button'):
    result = get_message(_index)
    st.write(f'Result: {result}')

st.header('Function: get_length_messages')
if st.button('Execute get_length_messages', key='get_length_messages_button'):
    result = get_length_messages()
    st.write(f'Result: {result}')

st.header('Function: delete_message')
if st.button('Execute delete_message', key='delete_message_button'):
    result = delete_message()
    st.write(f'Result: {result}')

st.header('Function: add_fixed_number')
_number = st.number_input('Enter _number', step=1, key='add_fixed_number__number')
_index = st.number_input('Enter _index', step=1, key='add_fixed_number__index')
if st.button('Execute add_fixed_number', key='add_fixed_number_button'):
    result = add_fixed_number(_number, _index)
    st.write(f'Result: {result}')

st.header('Function: get_fixed_number')
_index = st.number_input('Enter _index', step=1, key='get_fixed_number__index')
if st.button('Execute get_fixed_number', key='get_fixed_number_button'):
    result = get_fixed_number(_index)
    st.write(f'Result: {result}')

st.header('Function: add_real_dynamic_number')
_number = st.number_input('Enter _number', step=1, key='add_real_dynamic_number__number')
if st.button('Execute add_real_dynamic_number', key='add_real_dynamic_number_button'):
    result = add_real_dynamic_number(_number)
    st.write(f'Result: {result}')

st.header('Function: remove_dynamic_number')
if st.button('Execute remove_dynamic_number', key='remove_dynamic_number_button'):
    result = remove_dynamic_number()
    st.write(f'Result: {result}')

st.header('Function: get_dynamic_number')
_index = st.number_input('Enter _index', step=1, key='get_dynamic_number__index')
if st.button('Execute get_dynamic_number', key='get_dynamic_number_button'):
    result = get_dynamic_number(_index)
    st.write(f'Result: {result}')

st.header('Function: get_length_dynamic_array')
if st.button('Execute get_length_dynamic_array', key='get_length_dynamic_array_button'):
    result = get_length_dynamic_array()
    st.write(f'Result: {result}')

