class Student:
    def __init__(self, name, school, grade):
        self.name = name
        self.school = school
        self.grade = grade

    def get_msg(self):
        return "Name : " + self.name + "\n" + "School : " + self.school + "\n" + "Grade : " + self.grade

def main():
    info = input().split()
    student = Student(name=info[0], school=info[1], grade=info[2])
    print(student.get_msg())

if(__name__ == '__main__'):
    main()
