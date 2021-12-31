# global weight
# global은 항상 메모리를 차지한다

class add_class():
    def __init__(self) -> None:
        pass
    def add(self,num1,num2):
        result = num1+num2
        return result
    def temp01(self):
        pass

class minus_class():
    def __init__(self) -> None:
        pass
    def minus(self,num1,num2):
        result = num1-num2
        return result
    def temp01(self):
        pass

# fun은 매핑이 되어있어서 호출해도 패러매터로 소통이 안된다
# 그래서 self를 사용해서 소통을 해준다 딕셔너리 방식

if __name__=='__main__':
  
    pass