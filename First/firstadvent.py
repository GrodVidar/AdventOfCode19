def calculate(num):
    summa = 0
    i_num = int(num)
    while (int(i_num/3))-2 > 0:
        i_num = int(i_num/3)
        i_num -= 2
        summa += i_num
    return summa


def main():
    sumofcardemum = 0
    with open('modules.txt') as file:
        lines = file.readlines()
        for line in lines:
            print(line)
            sumofcardemum += calculate(line)
        print(sumofcardemum)
        quit()


main()
