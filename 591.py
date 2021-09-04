seq = []
N = 0

def sequence(idx):
    # global seq
    if seq[idx] != 0:
        return seq[idx]
    else:
        seq[idx] = sequence(idx-1) + sequence(idx//2)
        return seq[idx]

def main():
    global N, seq
    N = int(input())
    seq = [0] * (N+2)
    seq[0] = 0
    seq[1] = 1

    value = sequence(N)
    print(value)
    
if(__name__ == '__main__'):
    main()
