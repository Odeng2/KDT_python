'''
#2. 딕셔너리

** 과제 요구사항:
    1) 키: 연락처 이름, 값: 전화번호, 이메일, 주소 등의 정보
    2) 중첩 딕셔너리 구조 사용 -> 각 연락처마다 여러 정보 저장
    3) 기능 구현: 연락처 추가, 삭제, 검색, 수정, 모든 연락처 보기
'''


contacts = {}


def insert_contacts(input_name, input_phone, input_email, input_address):
    contacts[input_name] = {"phone": input_phone, "email": input_email, "address": input_address}
    print(f"{input_name}의 정보가 연락처에 추가되었습니다.")
    return contacts


def delete_contacts(input_name):
    del contacts[input_name]
    print(f"{input_name}의 정보가 연락처에서 삭제되었습니다.")
    return contacts


def search_contacts(input_name):
    print(f"{input_name}의 연락처 정보 ===================")
    print(f"전화번호 : " + contacts[input_name]["phone"])
    print(f"이메일 : " + contacts[input_name]["email"])
    print(f"주소 : " + contacts[input_name]["address"])


def modify_contact_info(input_name, input_field, input_value):
    new_info = { input_field: input_value }
    contacts[input_name].update(new_info)
    print(f"{input_name}님의 {input_field} 정보가 수정되었습니다.")
    


def show_contacts():
    print(contacts)



# 결과 테스트
insert_contacts("홍길동", "01012345678", "gildong@example.com", "마곡역 1번출구")
insert_contacts("박성진", "01023456789", "seongjin@example.com", "부산광역시")
insert_contacts("강영현", "01034567890", "youngk@example.com", "서울특별시")
insert_contacts("김원필", "01045678901", "wonpil@example.com", "인천광역시")
insert_contacts("윤도운", "01056789012", "dowoon@example.com", "부산광역시")
show_contacts()

delete_contacts("홍길동")
show_contacts()

search_contacts("강영현")

modify_contact_info("윤도운", "phone", "01099995555")
show_contacts()