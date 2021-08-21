from typing import Sequence


ans_seq = []

def make_sequence():
    ans_seq.append(1)
    foo(1,2)

def foo(n1, n2):
    value = (n1 * n2)%100
    if(len(ans_seq) == 100):
        return
    ans_seq.append(value)
    n2 = n1
    n1 = value
    foo(n1, n2)

def main():
    ans = int(input())
    make_sequence()
    print(ans_seq[ans-1])

if(__name__ == '__main__'):
    main()
