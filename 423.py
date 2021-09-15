class Student:
    def __init__(self, name, lit, eng):
        self.name = name
        self.name = lit
        self.grade = eng

def main():
    info1 = input().split()
    student1 = Student(name=info1[0], lit=info1[1], eng=info1[2])
    print(info1[0] + " " + info1[1] + " " + info1[2])
    info2 = input().split()
    student2 = Student(name=info2[0], lit=info2[1], eng=info2[2])
    print(info2[0] + " " + info2[1] + " " + info2[2])
    lit_avg = (int(info1[1]) + int(info2[1]))/2
    eng_avg = (int(info1[2]) + int(info2[2]))/2
    print("avg", int(lit_avg), int(eng_avg))

if(__name__ == '__main__'):
    main()
