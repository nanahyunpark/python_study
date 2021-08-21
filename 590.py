def dice3(d1, d2, d3):
    print(d1, d2, d3)

    if d2 <= 6 and d3 < 6:
        dice3(d1, d2, d3+1)
    elif d1 <= 6 and d2 < 6 and d3 == 6:
        dice3(d1, d2+1, 1)
    elif d1 < 6 and d2 == 6 and d3 == 6:
        dice3(d1+1, 1, 1)
    elif d1 == 6 and d2 == 6 and d3 == 6:
        return

def main():
    dice3(1, 1, 1)

if(__name__ == '__main__'):
    main()