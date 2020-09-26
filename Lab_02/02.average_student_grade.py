number_of_students = int(input())

student_record = {}

for _ in range(number_of_students):
    token = input().split()
    name = token[0]
    grade = float(token[1])
    if name not in student_record:
        student_record[name] = [grade]
    else:
        student_record[name].append(grade)

for name, marks in student_record.items():
    grades  = [''.join(f'{mark:.2f}') for mark in marks]
    print(f'{name} -> {" ".join(grades)} (avg: {sum(marks)/ len(marks):.2f})')