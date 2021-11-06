# # 2차원 리스트 생성과 접근

# a = [0] * 10    # 0으로 초기화된 값 10개 생성 (인덱스 0~9)
# print(a)        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# # 2차원 리스트
# a = [[0]*3 for _ in range(3)]       # 반복문이 3번 돌면서 [0]*3 실행
# print(a)        # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# a[0][1] = 1     # a[행][열] = 값
# print(a)        # [[0, 1, 0], [0, 0, 0], [0, 0, 0]]    

# for x in a :        # a라는 리스트의 행
#     print(x)        
# # [0, 1, 0]
# # [0, 0, 0]
# # [0, 0, 0]

# for x in a :        # 원소 하나하나의 값
#     for y in x :
#         print(y, end=" ")       # 0 1 0 0 0 0 0 0 0



# # 함수 만들기

# def add(a, b) :     # 함수 정의
#     c = a + b
#     print(c)

# add(4, 3)       # 4 + 3 = 7 출력


# def add(a, b) :
#     c = a + b
#     return c        # 결과값을 호출한 곳에 반환하고 함수 종료

# print(add(5, 3))    # 값을 받아서 출력


# def add(a, b) :
#     c = a + b
#     d = a - b
#     return c, d     # 여러 개 return 가능

# print(add(3, 2))    # 튜플로 반환 (5, 1)


# a = [11, 5, 6, 33, 27]

# # 소수 찾기 함수
# def isPrime(x) :
#     for i in range(2, x) :
#         if x % i == 0 :
#             return False
#     return True

# a = [11, 5, 6, 33, 27]

# for y in a :
#     if isPrime(y) :
#         print(y, end=" ")



# 람다함수 (익명함수)

def plus_one(x) :
    return x + 1
print(plus_one(1))      # 2


plus_two = lambda x : x + 2     # 람다함수를 사용하려면 변수에 할당해야 함
print(plus_two(1))      # 3


# 내장함수의 인자로 사용될 때 유용

a = [1, 2, 3]
print(list(map(plus_one, a)))       # map(함수명, 자료)     plus_one이라는 함수에 a값
# [2, 3, 4]

# 함수를 따로 만들지 않고 문장 내에 바로 함수 만들기

print(list(map(lambda x : x + 1, a))) 
# [2, 3, 4]     위의 print문과 같음


