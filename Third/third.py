class Lines:
    def __init__(self, x, y):
        self.x = 0
        self.new_x = x
        self.y = 0
        self.new_y = y
        self.horizontal = False
        self.vertical = False
        self.steps = 0

    def print_values(self):
        print(f'x: {self.x}, new_x: {self.new_x}\ny: {self.y}, new_y: {self.new_y}')

    def reset(self):
        self.x = 0
        self.new_x = 0
        self.y = 0
        self.new_y = 0
        self.steps = 0

    def move(self, direction, distance):
        if direction == 'R':
            # print("going Right")
            self.new_x += int(distance)
            self.steps += int(distance)
            # print(self.new_x)
            self.horizontal = True
            self.vertical = False
        elif direction == 'L':
            # print("going Left")
            self.new_x -= int(distance)
            self.steps += int(distance)
            self.horizontal = True
            self.vertical = False
        elif direction == 'U':
            # print("going Up")
            self.new_y += int(distance)
            self.steps += int(distance)
            self.vertical = True
            self.horizontal = False
        elif direction == 'D':
            # print("going Down")
            self.new_y -= int(distance)
            self.steps += int(distance)
            self.vertical = True
            self.horizontal = False
        else:
            print(f'got unknown direction: {direction}')

    def set_values(self):
        self.x = self.new_x
        self.y = self.new_y


def find_manhattan(x, y):
    return abs(x) + abs(y)


def check_values(horizontal, vertical, my_list, minimal_steps):
    if vertical.y < vertical.new_y:
        if vertical.y <= horizontal.y <= vertical.new_y:
            if horizontal.x < horizontal.new_x:
                if horizontal.x <= vertical.x <= horizontal.new_x:
                    my_list.append(find_manhattan(vertical.x, horizontal.y))
                    minimal_steps.append(vertical.steps-(abs(vertical.new_y-horizontal.y)) + horizontal.steps-(abs(horizontal.new_x-vertical.x)))
                    # print(f'hit on({vertical.x}, {horizontal.y})')
                    return
                else:
                    return
            else:
                if horizontal.new_x <= vertical.x <= horizontal.x:
                    my_list.append(find_manhattan(vertical.x, horizontal.y))
                    minimal_steps.append(vertical.steps-(abs(vertical.new_y-horizontal.y)) + horizontal.steps-(abs(horizontal.new_x-vertical.x)))
                    # print(f'hit on({vertical.x}, {horizontal.y})')
                    return
                else:
                    return
        else:
            return
    else:
        if vertical.new_y <= horizontal.y <= vertical.y:
            if horizontal.x < horizontal.new_x:
                if horizontal.x <= vertical.x <= horizontal.new_x:
                    my_list.append(find_manhattan(vertical.x, horizontal.y))
                    minimal_steps.append(vertical.steps-(abs(vertical.y-horizontal.y)) + horizontal.steps-(abs(horizontal.new_x-vertical.x)))
                    # print(f'hit on({vertical.x}, {horizontal.y}')
                    return
                else:
                    return
            else:
                if horizontal.new_x <= vertical.x <= horizontal.x:
                    my_list.append(find_manhattan(vertical.x, horizontal.y))
                    minimal_steps.append(vertical.steps-(abs(vertical.y-horizontal.y)) + horizontal.steps-(abs(horizontal.x-vertical.x)))
                    # print(f'hit on({vertical.x}, {horizontal.y}')
                    return
                else:
                    return
        else:
            return


def main():
    print('starting')
    myfile = open('input.txt', 'r')
    first = myfile.readline()
    first_list = first.split(',')
    first_list[-1] = first_list[-1].replace('\n', '')
    second = myfile.readline()
    second_list = second.split(',')
    line1 = Lines(0, 0)
    line2 = Lines(0, 0)
    minimal_steps = []
    my_list = []
    for i in first_list:
        line1.move(i[0], i[1:])
        for j in second_list:
            # line2.print_values()
            line2.move(j[0], j[1:])
            if line1.horizontal and line2.vertical:
                check_values(line1, line2, my_list, minimal_steps)
            elif line2.horizontal and line1.vertical:
                check_values(line2, line1, my_list, minimal_steps)
            line2.set_values()
        line2.reset()
        line1.set_values()
    print(f'minimal manhattan-distance: {min(my_list)}')
    print(f'minimal amount of steps before collision: {min(minimal_steps)}')

    # print(first_list[0][1:])
    # print(f'{first_list} hej hej {second_list}')


if __name__ == '__main__':
    main()