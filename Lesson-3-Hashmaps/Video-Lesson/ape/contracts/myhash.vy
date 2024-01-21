#@version ^0.3.9

week: public(HashMap[String[100], uint256])
user_balances: public(HashMap[address, uint256])
user_address: public(address)

@external
def add_days(_day:String[100], _value: uint256):
    self.week[_day] = _value

@external
def add_balance(_amount:uint256):
    self.user_address = msg.sender
    self.user_balances[self.user_address] = _amount

@external
def add_balance_custom(_wallet: address, _amount:uint256):
    self.user_balances[_wallet] = _amount

