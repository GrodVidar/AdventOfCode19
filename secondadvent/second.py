import csv


def add(list, first, second, output):
    list[output] = list[first] + list[second]
    return list


def multiply(list, first, second, output):
    list[output] = list[first] * list[second]
    return list


def main():
    print('starting')
    opcode = 0
    with open('input.csv') as file:
        reader = csv.reader(file)
        #print(values)
        values = list(reader)
        values = [int(x) for x in values[0]]
        for i in range(100):
            for j in range(100):
                opcode = 0
                new_values = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,13,23,27,1,6,27,31,1,31,10,35,1,35,6,39,1,39,13,43,2,10,43,47,1,47,6,51,2,6,51,55,1,5,55,59,2,13,59,63,2,63,9,67,1,5,67,71,2,13,71,75,1,75,5,79,1,10,79,83,2,6,83,87,2,13,87,91,1,9,91,95,1,9,95,99,2,99,9,103,1,5,103,107,2,9,107,111,1,5,111,115,1,115,2,119,1,9,119,0,99,2,0,14,0]
                new_values[1] = i
                new_values[2] = j
                running = True
                while running:
                    if new_values[0] == 19690720:
                        print(f'noun: {new_values[1]}, verb: {new_values[2]}\n answer= ')
                        print((100 * new_values[1])+ new_values[2])
                        running = False
                    if new_values[opcode] == 1:
                        print('adding')
                        new_values = add(new_values, new_values[opcode+1], new_values[opcode+2], new_values[opcode+3])
                        opcode = opcode+4
                    elif new_values[opcode] == 2:
                        print('multiplying')
                        new_values = multiply(new_values, new_values[opcode+1], new_values[opcode+2], new_values[opcode+3])
                        opcode = opcode+4
                    elif new_values[opcode] == 99:
                        # print('position 0 = %s' %(new_values[0]))
                        print('code')
                        running = False
                    else:
                        print('exiting opcode = %s' %(opcode))
                        running = False


if __name__ == '__main__':
    main()
    quit()
