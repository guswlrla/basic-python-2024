# date : 2024-01-31
# desc : 객체지향 클래스 만들기

# 클래스(사람이라는 객체를 만들기 위한 청사진) 만들기
class Person: # 사람 클래스 선언
    name = '' # 멤버변수
    age = 0
    gender = ''

    # 생성자 함수(스페셜 함수) 클래스의 객체를 생성할 때 동작.
    # init == initialization(초기화)
    def __init__(self) -> None:
        self.name = '홍길동'
        self.age = 29
        self.gender = '남자'

    # 클래스를 호출할 때 원하는 형태로 변환해서 보여주고 싶을 경우 사용
    def __str__(self) -> str:
        strs = f'커스텀 출력, 이름 {self.name} 객체 생성!'
        return strs

    # 멤버함수
    def walk(self):
        print(f'{self.name}이(가) 걷습니다.')
    
    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')


# 사람 객체 생성, Instance(사례, 예제)
ew = Person() # 함수 호출처럼 작성하면 됨
kj = Person()
# print(type(EW))
# print(id(EW)) # 다른 객체인지 확인
# print(id(KJ))
ew.name = '차은우' #객체명.멤버변수 = ...
ew.age = '28'
ew.gender = '남자'

kj.name = '서강준'
kj.age = '32'
kj.gender = '남자'

print(f'ew => 이름: {ew.name} / 나이: {ew.age}세 / 성별: {ew.gender}')
print(f'kj => 이름: {kj.name} / 나이: {kj.age}세 / 성별: {kj.gender}')

kj.walk()
print('1분동안 걷는다.')
kj.stop()

ew.walk()
print('걷기 싫어함.')
ew.stop()

print('-----------------생성자 함수 추가------------------')
gd = Person()
print(f'gd => 이름: {gd.name} / 나이: {gd.age}세 / 성별: {gd.gender}')
print(gd) 
