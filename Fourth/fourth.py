from collections import Counter


def check_if_duplicates(list_of_elements):
    if len(list_of_elements) == len(set(list_of_elements)):
        return False
    else:
        c = dict(Counter(list_of_elements))
        count = False
        for key in c:
            if c[key] == 2:
                return True



def check_validity(input):
    digits = [int(d) for d in str(input)]
    if digits[-1] >= digits[-2]:
        if digits[-2] >= digits[-3]:
            if digits[-3] >= digits[-4]:
                if digits[-4] >= digits[-5]:
                    if digits[-5] >= digits[-6]:
                        result = check_if_duplicates(digits)
                        if result:
                            return 1
                        else:
                            return 0
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0


def main():
    min_pass = 402328
    max_pass = 864247
    valid_pass = 0
    for i in range(min_pass, max_pass):
        valid_pass += check_validity(i)
    print(valid_pass)


if __name__ == '__main__':
    main()