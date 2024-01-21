### Balance Tracker Template

Below you can find a template, you can copy and paste to either Remix or your local dev environment.

Each line of comments, provides instructions on how to write up the contract.

Check out the video, if you need help on writing the contract up!

```python
# Simplified User Registration and Balance Tracker Contract in Vyper

# Declare a dynamic array to store addresses of registered users, with a maximum of 100 addresses

# Declare a public HashMap to map user addresses (address type) to their balances (unsigned 256-bit integer)

# Define a public function that allows users to register themselves
    # Inside the function:
    # - Create a variable to store the address of the sender (msg.sender)
    # - Append the sender's address to the dynamic array of registered users
    # - Initialize the sender's balance to 0 in the HashMap

# Define a public function that allows a user to set their balance
    # The function takes an unsigned 256-bit integer as an input parameter (the new balance)
    # Inside the function:
    # - Store the sender's address in a variable
    # - Update the sender's balance in the HashMap to the new balance

# Define a public view function to get the balance of a specific user
    # The function takes an address as an input parameter
    # Inside the function:
    # - Return the balance associated with the input address from the HashMap
```