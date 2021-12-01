def fun_callback(input, extend_input):
    print('fun_callback sum :',input)
    print('fun_callback extend_input :', extend_input)
    return

def fun_call(one, two, f_callback,three):
    result = one + two
    f_callback(result, three)
    return

first = 10
second = 20
third = 30
fun_call(first, second, fun_callback, third)