global weight
def add(num1,num2):
    global weight
    result = num1+num2+weight
    return result

if __name__=='__main__':
    weight = 5
    result = add(1,2)
    print(result)
    pass