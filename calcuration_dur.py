# init 거리 시간 속력
# fun1 fun2 출력
class class_name():
    def __init__(self) -> None:
        self.dist = 5.0
        self.time = 1.0
        self.vel = 5
        pass
    def temp01(self):
        result = self.time*self.vel
        return(result)
    def temp02(self):
        result = self.dist / self.vel
        return(result)
    def temp03(self):
        call = class_name()
        dist = call.temp01()
        time = call.temp02()
        print("거리는 %s, 시간은 %s",dist,time)



# fun은 매핑이 되어있어서 호출해도 패러매터로 소통이 안된다
# 그래서 self를 사용해서 소통을 해준다 딕셔너리 방식

if __name__=='__main__':
    call = class_name()
    call.temp03()
    pass