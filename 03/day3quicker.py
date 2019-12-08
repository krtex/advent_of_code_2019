def parse_command(list, command):
    head = command[0]
    tail = int(command[1:])
    last = list[-1]

    if head == 'U':
        temp = [(last[0], i) for i in range(last[1] + 1, last[1] + tail + 1)]
    elif head == 'D':
        temp = [(last[0], i) for i in range(last[1] - 1, last[1] - tail - 1, -1)]
    elif head == 'R':
        temp = [(i, last[1]) for i in range(last[0] + 1, last[0] + tail + 1)]
    elif head == 'L':
        temp = [(i, last[1]) for i in range(last[0] - 1, last[0] - tail - 1, -1)]
    list.extend(temp)

def parse_input(input_file):
    with open(input_file) as f:
        wire_positions = f.read().splitlines()
    wire1 = wire_positions[0].split(',')
    wire2 = wire_positions[1].split(',')
    return wire1, wire2

def main(input_file):
    path1, path2 = parse_input(input_file)

    wire1 = [(0,0)]
    wire2 = [(0,0)]
    for e in path1:
        parse_command(wire1, e)

    for e in path2:
        parse_command(wire2, e)

    inter = set(wire1).intersection(wire2)

    distances = []
    metric = lambda a, b : abs(a) + abs(b)
    for e in inter:
        distances.append(metric(e[0], e[1]))

    distances.sort()
    print(distances)

if __name__ == "__main__":
    main("input")
