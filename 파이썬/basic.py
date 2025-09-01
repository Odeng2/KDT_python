# =============== 변수 ===============


# # 1: 'global' (함수 안에서 전역 변수값 수정)
# count = 0

# def increment():
#     global count
#     count += 1

# print(count)
# increment()
# print(count)


# # Quiz : 아래 코드의 출력 결과는?
# x = 10
# y = 20
# x, y = y, x
# print(x, y)



# =============== 데이터 타입 ===============


# # 1: 정밀도 제한(float type 사용시 정확한 계산이 어려움.)
# print(0.1 + 0.2 == 0.3)

# # 해결 1. 반올림('round') 사용하기
# print(round(0.1 + 0.2, 1) == 0.3)
# # 해결 2. decimal 모듈 사용하기
# from decimal import Decimal
# a = Decimal('0.1')
# b = Decimal('0.2')
# print(a + b)
# # 해결 3. math 모듈의 'isclose' 함수 사용하기
# import math
# print(math.isclose(0.1 + 0.2, 0.3))


# # 2: 문자열 - 삼중따옴표(여러 줄 문자열)
# str1 = """안녕하세요.
# str1입니다. """
# str2 = '''이건
# str2입니다.'''
# print(str1)
# print(str2)


# # 3: 불리언 - 단축 평가(and의 첫 값이 False이거나 or의 첫 값이 True면 두 번재 값은 무시됨.
# print(False and print("확인"))
# print(True or print("확인"))

# # 실제 값 반환
# print(0 and 5)
# print(2 and 5)
# print(0 or 5)
# print(2 or 5)


# # 4: 객체 비교 (==은 내용이 같으면 True, is는 객체까지 같아야 True)
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# list3 = list1

# print(list1 == list2)
# print(list1 is list2)
# print(list1 is list3)


# # Quiz 1 : 다음 코드의 출력 결과는?
# a = 0.1 + 0.1 + 0.1
# b = 0.3 
# print(a == b)

# # Quiz 2 : 다음 중 False로 평가되지 않는 것은?
# print(0)
# print("")
# print([0])
# print(None)
# print(False)

# # Quiz 3 : 다음 코드의 실행 결과와 그 이유는?
# text = "Python"
# text[0] = "J"
# print(text)
# # 에러. str type은 수정 불가능. (불변성. immutability)



# # =============== 컬렉션 타입 - 리스트 ===============


# # Quiz 1 : 다음 코드의 실행 결과는?
# numbers = [1, 2, 3, 4, 5]
# numbers[1:4] = [10, 20]
# print(numbers)


# # Quiz 2 : 다음 코드의 실행 결과는?
# def modify_list(lst):
#     lst.append(4)
#     lst = [7, 8, 9]
#     return lst

# original = [1, 2, 3]
# result = modify_list(original)
# print(original)
# print(result)


# # Quiz 3 : 다음 코드를 실행했을 때의 오류는?
# matrix = [[0] * 3] * 3
# matrix[0][0] = 1
# matrix[1][1] = 2
# print(matrix)



# # =============== 컬렉션 타입 - 튜플 ===============

# # Quiz 1 : 다음 코드의 실행 결과는?
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# result = t1 + t2
# print(result[2:5])


# # Quiz 2 : 다음 코드에서 오류가 발생하는 라인은?
# person = ('홍길동', 30, '서울')
# name, age, city = person
# age = age + 1
# person[1] = age
# print(f"{name}은 {age}세이고 {city}에 살고 있습니다.")

# # Quiz 3 : 다음 코드의 실행 결과는?
# def get_values():
#     return 1, 2, 3

# x, *y = get_values()
# print(x)
# print(y)



# =============== 컬렉션 타입 - 집합 ===============

# # Quiz 1 : 다음 코드의 결과는?
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# set3 = {1, 2}

# print(set3.issubset(set1))
# print(set3 < set1)
# print(set1.isdisjoint(set2))
# print(set1 ^ set2)


# # Quiz 2 : 다음 코드의 결과는?
# def process_data(data):
#     unique = set()
#     result = []
#     for item in data:
#         if isinstance(item, list):
#             item = tuple(item)
#         if item not in unique:
#             unique.add(item)
#             result.append(item)
#     return result

# data = [1, 2, 2, [3, 4], [3, 4], 5]
# print(process_data(data))


# # =============== 연산자 ===============


# # Quiz 1 : 다음 코드의 출력 결과는?
# x = 10
# y = 5
# z = x // y * 2 + x % y
# print(z)


# # Quiz 2 : 다음 논리 연산의 결과값은?
# a = True
# b = False
# c = True
# result = a or b and not c
# print(result)


# # Quiz 3 : 다음 코드를 실행한 후 변수 x의 최종값은?
# x = 5
# x += 3
# x *= 2
# x //= 3
# print(x)



# # =============== 조건문 ===============


# # Quiz 1 : 다음 코드의 출력 결과는?
# age = 15
# if age < 13:
#     ticket_price = 5000
#     category = "어린이"
# elif age < 19:
#     ticket_price = 8000
#     category = "청소년"
# else:
#     ticket_price = 10000
#     category = "성인"
# print(f"{category} 티켓 가격: {ticket_price}원")


# # Quiz 2 : 다음 코드에서 발생하는 문제는 무엇이며, 어떻게 수정해야 하는지?
# score = 85
# if score >= 90:
#     grade = "A"
# if score >= 80:
#     grade = "B"
# if score >= 70:
#     grade = "C"
# if score >= 60:
#     grade = "D"
# else:
#     grade = "F"
# print(f"학점: {grade}")


# # Quiz 3 : 중첩 조건문을 3항 연산자를 사용해 한 줄로 작성하기
# temperature = 25
# if temperature > 30:
#     message = "더운 날씨입니다."
# else:
#     if temperature > 20:
#         message = "적당한 날씨입니다."
#     else:
#         message = "추운 날씨입니다."
# print(message)



# # =============== 반복문 ===============


# # Quiz 1 : 다음 반복문의 출력 결과는?
# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()


# # Quiz 2 : 다음 반복문의 출력 결과는?
# sum_value = 0
# for i in range(1, 10):
#     if i % 2 == 0:
#         continue
#     sum_value += i
#     if sum_value > 10:
#         break
# print(sum_value)


# # Quiz 3 : 다음 반복문의 출력 결과는?
# numbers = [4, 2, 7, 1, 8, 3, 6]
# result = 0
# for num in numbers:
#     if num % 2 == 0:
#         result += num
#     else:
#         result -= num
# print(result)


# # =============== 반복문 ===============
