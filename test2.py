# # 조건문

# x = 5
# if x == 5 : 
#     print("Yes")
#     #   print("error")          # 들여쓰기 에러


# # 중첩

# x = 12
# if x >= 10:
#     if x%2==1:
#         print("10이상의 홀수")
#     print("10이상의 짝수")

# x = 7
# if x > 0 and x < 10:            # 0<x<10 가능
#     print("10보다 작은 자연수")


# # 분기

# x = -10
# if x > 0 :
#     print("양수")
# else:
#     print("음수")

# x = 50
# if x >= 90 :
#     print("A학점")
# elif x >= 80 :
#     print("B학점")
# elif x >= 70 :
#     print("C학점")
# elif x >= 60 :
#     print("D학점")
# else :
#     print("F학점")


# # 반복문

# # for문
# a = range(1, 11)       # 0~9
# print(list(a))          # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(1, 11) :
#     print(i)      # 1~10  줄바꿈

# for i in range(10, 0, -1) :     # 10~1 1씩 작아짐
#     print(i) 


# # while문
# i = 1
# while i <= 10 :
#     print(i)
#     i = i + 1        # 1~10 줄바꿈


# i = 10
# while i >= 1 :
#     print(i)
#     i = i - 1        # 10~1 줄바꿈


# # break
# i = 1
# while True : 
#     print(i)
#     if i == 10 :
#         break
#     i += 1       # 1~10 줄바꿈


# # continue
# for i in range(1, 11) :
#     if i % 2 == 0 :     # i가 짝수일 때
#         continue
#     print(i)        # 홀수만 출력


# # else
# for i in range(1, 11) :
#     print(i)
#     if i > 15 :
#         break
# else :
#     print(11)           # for문이 정상적으로 동작했을 때 출력됨 (break되면 출력 X)


# # 반복문 문제풀이
# # 1) 1부터 N까지 홀수 출력하기

# n = int(input())
# for i in range(1, n+1) :
#     if i % 2 ==1 :
#         print(i)

# # 2) 1부터 N까지의 합 구하기

# n = int(input())
# sum = 0
# for i in range(1, n+1) :
#     sum = sum + i
# print(sum)

# # 3) N의 약수 출력하기

# n = int(input())
# for i in range(1, n+1) :
#     if n % i == 0 :
#         print(i)


# 중첩 반복문 (이중 for문)

# 사각형

for i in range(5) :
    for j in range(5) :
        print("*", end=' ')
    print()

# 직각 삼각형

for i in range(5) :
    for j in range(i + 1) :
        print("*", end=' ')
    print()

# 거꾸로 된 직각 삼각형

for i in range(5) :
    for j in range(5 - i) :
        print("*", end=' ')
    print()

