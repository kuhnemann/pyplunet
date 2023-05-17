import random

from src.pyplunet import enums

values = [1,2,"1","2"]

def test_all():
    for member in dir(enums):
        if "__" in member:
            continue
        val = values[random.randint(0,3)]
        eenuum = getattr(enums, member)
        try:
            eenuum(val)
        except Exception as e:
            print(eenuum)
            print(eenuum.__name__)
            print(e)
if __name__ == '__main__':
    test_all()