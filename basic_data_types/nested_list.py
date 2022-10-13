student_grades = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_grades.append([name,score])
grades_list = sorted(list(set([student[1] for student in student_grades])))
student2 = [
    student
    for student in student_grades
    if student[1] == grades_list[1]
    ]
student2.sort()
for student in student2:
    print(student[0])
