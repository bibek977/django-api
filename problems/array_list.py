from typing import Union

def _as_list(value: Union[list,str])->list:
    if isinstance(value,list):
        return value
    
    return [value]

def _parse_list(value: Union[list,str])->str:
    if isinstance(value,str):
        return value
    return ",".join(value)

x = ['banana','apple','orange']
y = "Python is a programming Language"

print(_as_list(x))
print(_as_list(y))
print(_parse_list(x))
print(_parse_list(y))
