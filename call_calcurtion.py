from calcuration_class import add_class
from calcuration_class import minus_class

if __name__ == '__main__':
    instance = add_class()
    result = instance.add(3,5)
    print(result)
    instance2 = minus_class()
    result2 = instance2.minus(5,3)
    print(result2)
    pass