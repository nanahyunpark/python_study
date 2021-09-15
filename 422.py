class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_msg(self):
        return self.grade + " grade in " + self.name + " School"

def main():
    student = Student(name = "Jejuelementary", grade = "6")
    info = input().split()
    print(student.get_msg())
    student = Student(name=info[0], grade=info[1])
    print(student.get_msg())

if(__name__ == '__main__'):
    main()
