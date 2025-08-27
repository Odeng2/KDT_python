'''
#1. 리스트

** 과제 요구사항:
    1)학생 추가: 이름과 점수 입력 -> 목록에 추가
    2) 학생 삭제: 이름 입력 -> 해당 학생의 정보 삭제
    3) 성적 수정: 이름 입력 -> 해당 학생의 점수 수정
    4) 전체 목록 출력: 모든 학생의 이름 및 점수 출력
    5) 통계 출력: 최고, 최저, 평균 점수 계산 및 출력
'''

students = []

def add_student(name, score):
    students.append([name, score])
    print(f"{name} 학생, {score}점 추가됨")
    return students


def delete_student(name):
    for i in range(len(students)):
        if students[i][0] == name:
            students.pop(i)
            break

    print(f"{name} 학생 정보 삭제됨")
    return students

        
def modify_score(name, score):
    for i in range(len(students)):
        if students[i][0] == name:
            students[i][1] = score
            break
    
    print(f"{name} 학생의 점수가 {score}점으로 수정됨")
    return students

def show_students():
    print(students)

def statistics():
    best_score = 0
    worst_score = 100
    avg_score = 0

    for i in range(len(students)):
        avg_score += students[i][1]

        if best_score < students[i][1]:
            best_score = students[i][1]
    
        if worst_score > students[i][1]:
            worst_score = students[i][1]

    print(f"best score : {best_score}")
    print(f"worst score : {worst_score}")
    print(f"average score : {avg_score / len(students)}")



add_student("정규민", 90)
add_student("박치원", 80)
add_student("서동현", 92)
add_student("안지민", 74)
add_student("노재윤", 88)
show_students()
statistics()

delete_student("서동현")
show_students()
statistics()

modify_score("정규민", 60)
show_students()
statistics()
