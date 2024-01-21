from web3 import Web3, HTTPProvider
from dotenv import load_dotenv
import os

load_dotenv()

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

assert w3.is_connected(), 'Failed to connect to the Ethereum client.'

contract_address = '0x998abeb3E57409262aE5b751f60747921B33613E'
abi = [
    {
        "inputs": [
            {
                "name": "_message",
                "type": "string"
            }
        ],
        "name": "add_message",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "_index",
                "type": "uint256"
            }
        ],
        "name": "get_message",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "get_length_messages",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "delete_message",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "_number",
                "type": "uint256"
            },
            {
                "name": "_index",
                "type": "uint256"
            }
        ],
        "name": "add_fixed_number",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "_index",
                "type": "uint256"
            }
        ],
        "name": "get_fixed_number",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "_number",
                "type": "uint256"
            }
        ],
        "name": "add_real_dynamic_number",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "remove_dynamic_number",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "_index",
                "type": "uint256"
            }
        ],
        "name": "get_dynamic_number",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "get_length_dynamic_array",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = w3.eth.contract(address=contract_address, abi=abi)

account_address = '0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266'
private_key = os.getenv('PRIVATE_KEY')
assert private_key, 'Private key not found in .env file'

def add_message(_message):
    # Update nonce before building transaction
    updated_nonce = w3.eth.get_transaction_count(account_address)

    # Build transaction with updated nonce
    txn = contract.functions.add_message(_message).build_transaction({
        'chainId': 31337,
        'gas': 2000000,
        'nonce': updated_nonce,
    })

    # Sign transaction
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    # Send transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    # Wait for transaction to be mined
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt

def get_message(_index):
    return contract.functions.get_message(_index).call()

def get_length_messages():
    return contract.functions.get_length_messages().call()

def delete_message():
    # Update nonce before building transaction
    updated_nonce = w3.eth.get_transaction_count(account_address)

    # Build transaction with updated nonce
    txn = contract.functions.delete_message().build_transaction({
        'chainId': 31337,
        'gas': 2000000,
        'nonce': updated_nonce,
    })

    # Sign transaction
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    # Send transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    # Wait for transaction to be mined
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt

def add_fixed_number(_number, _index):
    # Update nonce before building transaction
    updated_nonce = w3.eth.get_transaction_count(account_address)

    # Build transaction with updated nonce
    txn = contract.functions.add_fixed_number(_number, _index).build_transaction({
        'chainId': 31337,
        'gas': 2000000,
        'nonce': updated_nonce,
    })

    # Sign transaction
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    # Send transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    # Wait for transaction to be mined
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt

def get_fixed_number(_index):
    return contract.functions.get_fixed_number(_index).call()

def add_real_dynamic_number(_number):
    # Update nonce before building transaction
    updated_nonce = w3.eth.get_transaction_count(account_address)

    # Build transaction with updated nonce
    txn = contract.functions.add_real_dynamic_number(_number).build_transaction({
        'chainId': 31337,
        'gas': 2000000,
        'nonce': updated_nonce,
    })

    # Sign transaction
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    # Send transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    # Wait for transaction to be mined
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt

def remove_dynamic_number():
    # Update nonce before building transaction
    updated_nonce = w3.eth.get_transaction_count(account_address)

    # Build transaction with updated nonce
    txn = contract.functions.remove_dynamic_number().build_transaction({
        'chainId': 31337,
        'gas': 2000000,
        'nonce': updated_nonce,
    })

    # Sign transaction
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    # Send transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    # Wait for transaction to be mined
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt

def get_dynamic_number(_index):
    return contract.functions.get_dynamic_number(_index).call()

def get_length_dynamic_array():
    return contract.functions.get_length_dynamic_array().call()

