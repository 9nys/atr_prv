class RenamePrivateAttributes(type):
    def __new__(cls, name, bases, dct):
        for key, value in dct.items():
            if key.startswith("__"):
                new_key = f"__private_{key[2:]}"
                dct[new_key] = dct.pop(key)
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=RenamePrivateAttributes):
    def __init__(self):
        self.__private_var = 10
        self.public_var = 20


obj = MyClass()
print(obj.__dict__)  # {'__private_var': 10, 'public_var': 20}
