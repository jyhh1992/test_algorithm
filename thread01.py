import threading

def firstfun(age):
    while True:
        print("Child",age)
    return

def secondfun(age):
    while True:
        print("SecondChild",age)
    return

if __name__ == "__main__":
    first = threading.Thread(target=firstfun,args=(5,))
    second = threading.Thread(target = secondfun,args=(3,))
    first.start()
    second.start()
    first.join()
    second.join()

    while True:
        print("I am parent")    
    pass