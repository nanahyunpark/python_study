def get_scores(n1, n2, n3):
    stu_total = n1+n2+n3
    print(n1, n2, n3, stu_total)
    return stu_total

def main():
    sub1, sub2, sub3 = 0,0,0
    total = 0
    for i in range(0,3):
        n = input().split()
        stu_total = get_scores(int(n[0]), int(n[1]), int(n[2]))
        sub1 += int(n[0])
        sub2 += int(n[1])
        sub3 += int(n[2])
        total += stu_total
    print(sub1, sub2, sub3, total)
    

if(__name__ == '__main__'):
    main()