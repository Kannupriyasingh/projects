from prettytable import PrettyTable
mytable = PrettyTable(["student name", "course", "semester", "percentage"])
count = int(input("how many students?: "))
for i in range(1, count+1):
    name = input("name of the student: ")
    course = input("course of the student: ")
    semester = input("semester of the student: ")
    per = input("percentage of the student: ")
    mytable.add_row([name, course, semester, per])
print(mytable)
