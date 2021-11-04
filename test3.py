# # 문자열과 내장함수

# msg = "It is Time"
# print(msg.upper())
# print(msg.lower())      # msg 값이 변하는 건 아님
# print(msg)

# tmp = msg.upper()
# print(tmp)
# print(tmp.find("T"))    # 처음 찾은 인덱스 번호 
# print(tmp.count("T"))   # 찾으려는 문자 개수
# print(tmp[:2])      # 인덱스 2 미만 값 출력
# print(tmp[3:5])     # 인덱스 3, 4 값 출력

# print(len(msg))     # 문자열 길이

# for i in range(len(msg)) :
#     print(msg[i], end=' ')
# print()

# for x in msg :
#     print(x, end=' ')
# print()

# # 문자열에서 대문자만 출력
# for x in msg :
#     if x.isupper() :
#         print(x, end=' ')       
# print()

# # 문자열에서 소문자만 출력
# for x in msg :
#     if x.islower() :
#         print(x, end=' ')       
# print()

# # x가 알파벳일 때만 참
# for x in msg :
#     if x.isalpha() :
#         print(x, end='')       
# print()

# # 대문자 아스키 넘버 (A(65) ~ Z(90))
# tmp = 'AZ'
# for x in tmp :
#     print(ord(x))

# # 소문자 아스키 넘버 (A(97) ~ Z(122))
# tmp = 'az'
# for x in tmp :
#     print(ord(x))

# # 아스키 넘버에 해당하는 문자 출력
# tmp = 65        # A
# print(chr(tmp))



# 리스트와 내장함수

import random as r

a = []      # 빈 리스트
b = list()      # 빈 리스트

a = [1, 2, 3, 4, 5]
print(a)
print(a[0])     # 1

b = list(range(1, 11))      # 1~10 까지 초기화
print(b)

c = a + b       # 리스트끼리 합치기
print(c)

a.append(6)
print(a)