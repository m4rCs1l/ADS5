from typing import List

def prepare_data(text:str):
    data = []

    side_size = -1
    for line in text.splitlines():
        if side_size == -1:
            side_size = len(line)

        if len(line) != side_size:
            raise RuntimeError("Данный лабиринт не прямоугольник")

        data.append([])

        for char in line:
            if char not in ["0", "1"]:
                raise RuntimeError("Данный лабиринт имеет неизвестные символы")

            if char == "0":
                data[-1].append([0, 0])
            else:
                data[-1].append([1, 0])

    return data

text = "101111\n" \
       "100001\n" \
       "111101\n" \
       "100001\n" \
       "101111\n" \
       "100001\n" \
       "111101"

def print_data(data):
    for line in data:
        for item in line:
            print(item[0], end="")
        print("")
    print("")

def find_entrances(data:List[List[List]]):
    num_entrances = 0
    entrances = []
    for y in range(len(data)):
        if data[y][0][0] == 0:
                num_entrances+=1
                entrances.append([0, y])
        if data[y][len(data[0])-1][0] == 0:
                num_entrances+=1
                entrances.append([len(data[0])-1, y])
    for x in range(len(data[0])):
        if data[0][x][0] == 0:
                num_entrances+=1
                entrances.append([x, 0])
        if data[len(data)-1][x][0] == 0:
                num_entrances+=1
                entrances.append([len(data)-1, x])
    if num_entrances > 2:
        raise Exception("Больше 2-x входов")
    elif num_entrances < 2:
        raise Exception("Меньше 2-x входов")
    return entrances


labyrinth = prepare_data(text)
print_data(labyrinth)
entrances = find_entrances(labyrinth)
print(entrances)

def get_4_sides(x, y, side_len):
    ret_data = []
    if x-1 >= 0:
        ret_data.append([x-1, y])
    if x+1 < side_len:
        ret_data.append([x+1, y])
    if y - 1 >= 0:
        ret_data.append([x, y-1])
    if y + 1 < side_len:
        ret_data.append([x, y+1])
    return ret_data

path = []

def solve(labyrinth, x, y):
    # Если дошли до выхода и не начало
    global path
    if labyrinth[x][y][1] == 0 and labyrinth[x][y][0] == 0 and (x == 0 or y == 0 or x == len(labyrinth) - 1 or y == len(labyrinth) - 1):
        path.append([x, y])
        return True

    sides = get_4_sides(x, y, len(labyrinth))

    labyrinth[x][y][1] += 1

    for side in sides:
        lx = side[0]
        ly = side[1]
        # Если не стена
        if labyrinth[lx][ly][0] != 1:
            # Если не было посещено
            if labyrinth[lx][ly][1] == 0:
                answer = solve(labyrinth, lx, ly)
                if answer:
                    path.append([x, y])
                    return True

    return False

labyrinth[entrances[0][1]][entrances[0][0]][1] = 1
if solve(labyrinth, entrances[0][1], entrances[0][0]):
    for pair in path:
        labyrinth[pair[0]][pair[1]][0] = "*"
    print_data(labyrinth)