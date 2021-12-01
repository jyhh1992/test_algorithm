def func():
    pass
    return

if __name__ == '__main__':
    try:
        f = open('./textfile.txt','r')
        length = len(f.read())
        f.close()
        print(length)
    except Exception as e:
        pass

