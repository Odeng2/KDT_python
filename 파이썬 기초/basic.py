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



# =============== 컬렉션 타입 - 리스트 ===============
