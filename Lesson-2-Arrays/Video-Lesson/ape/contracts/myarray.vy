#@version ^ 0.3.9

fixed_size_array: uint256[5]
dynamic_size_array: DynArray[uint256, 10]
dynamic_string_array: DynArray[String[100], 10]

@external
def add_message(_message:String[100]):
    self.dynamic_string_array.append(_message)

@view
@external
def get_message(_index:uint256) -> String[100]:
    return self.dynamic_string_array[_index]

@view
@external
def get_length_messages() -> uint256:
    return len(self.dynamic_string_array)

@external
def delete_message():
    self.dynamic_string_array.pop()

@external
def add_fixed_number(_number: uint256, _index: uint256):
    self.fixed_size_array[_index] = _number

@view
@external
def get_fixed_number(_index:uint256) -> uint256:
    return self.fixed_size_array[_index]


@external
def add_real_dynamic_number(_number: uint256):
    self.dynamic_size_array.append(_number)

@external
def remove_dynamic_number():
    self.dynamic_size_array.pop()

@view
@external
def get_dynamic_number(_index:uint256) -> uint256:
    return self.dynamic_size_array[_index]


@view
@external
def get_length_dynamic_array() -> uint256:
    return len(self.dynamic_size_array)

