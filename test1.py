# # 값 교환
# a,  b = 1, 2
# print(a, b)
# a, b = b, a
# print(a, b)

# # 변수 타입
# a = 12345
# print(type(a))
# a = 12.345
# print(type(a))
# a = 'study'
# print(type(a))

# # 출력 방식
# print("number")
# a, b, c = 1, 2, 3
# print(a, b, c)
# print("number : ", a, b, c)
# print(a, b, c, sep='\n')            # 각 변수 사이에 sep 값이 들어감
# print(a)
# print(b)
# print(c)            # print는 자동줄바꿈

# print(a, end=' ')       # 줄바꿈 안함
# print(b)
# print(c)  

# 변수 입력
a = input("숫자를 입력하세요 : ")
print(a)

a, b = input("숫자를 입력하세요 : ").split()        # a와 b 분리
print(a+b)      # string
a, b = int(a), int(b)   # int로 바꾸기
print(a+b)

a, b = map(int, input("숫자를 입력하세요 : ").split())      # map을 통해 int로 바꾸기
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)     # 몫
print(a%b)      # 나머지
print(a**b)     # 제곱

a = 4.3
b = 2
c = a + b
print(type(c))      # 정수형보다 넓은 범위인 실수형