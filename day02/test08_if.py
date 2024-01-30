# date : 2024-01-30
# desc : 홀수/짝수 또는 배수
number = int(input('정수입력 > ')) # 입력 받은 후 정수로 변경

if number % 2 == 0: # 짝수 또는 배수
    print('짝수')
else: # 홀수 또는 나머지
    print('홀수')