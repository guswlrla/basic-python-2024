# date : 2024-01-31
# desc : 별찍기 또는 피라미드 만들기
# *
# **
# **
# ****
# *****
for i in range(1, 6):
    # i가 1일때는, range(1, 2) 1번 반복
    # i가 2이면, range(1,3) 2번 반복
    for j in range(1, 6-i+1): # range() 값 바꿔서 디버깅
        print('*', end = '') # 엔터대신 empty로 변환
    print() # 안쪽 for문이 끝나면 엔터