#@version ^0.3.0

my_number: public(uint256)
greet: public(String[100])

@external
def __init__():
    self.greet = "Hello World"

@external
def changeNumber(_num: uint256):
    self.my_number = _num

@external
def changeGreet(_greet: String[100]):
    self.greet = _greet
