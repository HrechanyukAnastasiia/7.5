#4
def func_4(*args):
    dict1 = {}
    for name, age in args:
        dict1[name] = age
    return dict1
print(func_4(*[('Настя', 16), ('Анастасія', 14), ('Міша', 17), ('Женя', 20)]))