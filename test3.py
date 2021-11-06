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



# # 리스트와 내장함수

# import random as r

# a = []      # 빈 리스트
# b = list()      # 빈 리스트

# a = [1, 2, 3, 4, 5]
# print(a)
# print(a[0])     # 1

# b = list(range(1, 11))      # 1~10 까지 초기화
# print(b)

# c = a + b       # 리스트끼리 합치기
# print(c)

# a.append(6)     # 마지막에 6 추가
# print(a)

# a.insert(3, 7)      # 인덱스 3에 7 추가
# print(a)

# a.pop()
# print(a)        # 마지막 삭제

# a.pop(3)
# print(a)        # 인덱스 3 값 삭제

# a.remove(4)     # 값이 4인 것 삭제
# print(a)

# print(a.index(5))       # 값이 5인 인덱스 번호 출력

# a = list(range(1, 11)) 
# print(sum(a))       # a라는 리스트의 모든 값 합치기
# print(max(a))       # a라는 리스트의 최댓값 출력 (인자값 중에서)
# print(min(a))       # a라는 리스트의 최솟값 출력 (인자값 중에서)
# print(min(7, 4, 10))        # 인자값 중에서 최솟값 출력

# # a를 랜덤으로 섞기
# r.shuffle(a)        
# print(a)

# # 오름차순 정렬
# a.sort()       
# print(a)

# # 내림차순 정렬
# a.sort(reverse=True)   
# print(a)

# # 리스트 비우기
# a.clear()
# print(a)



# 리스트와 내장함수 2

a = [23, 12, 36, 53, 19]
print(a[:3])        # 인덱스 0~2 값 출력
print(a[1:4])       # 인덱스 1~3 값 출력
print(len(a))        # 리스트 길이(개수)

for i in range(len(a)) :
    print(a[i], end=" ")
print()

for x in a :
    print(x, end=" ")
print()

# 홀수 출력
for x in a :
    if x % 2 == 1 :
        print(x, end=" ")
print()


# 튜플

b = (1, 2, 3, 4, 5)
print(b[0])

# b[0] = 7          # 에러 발생

# 튜플은 값 변경 불가 (리스트는 가능)

# enumerate - 인덱스와 해당하는 값 튜플 형태로 출력
for x in enumerate(a) :
    print(x)

for x in enumerate(a) :
    print(x[0], x[1])       # 하나하나 원소 값 출력
print()

for index, value in enumerate(a) :
    print(index, value)
print()

# all - 60 > x라는 조건을 모두 만족하면 참
if all(50 >x for x in a) :
    print("Yes!")
else :
    print("No!")

# any - 60 > x라는 조건을 한 번이라도 만족하면 참 (모두 만족하지 않아야 거짓)
if any(20 >x for x in a) :
    print("Yes!")
else :
    print("No!")