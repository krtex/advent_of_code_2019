import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
            self.x = x
            self.y = y

    def __repr__(self):
        return "(%s, %s)" % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.x == other.y

    def __hash__(self):
        return hash(repr(self))

def draw_up(start, steps):
    line = set()
    for i in range(start.y + 1, start.y + steps):
        line.add(Point(start.x, i))
    last = Point(start.x, start.y + steps)
    line.add(last)
    return line, last

def draw_down(start, steps):
    line = set()
    for i in range(start.y - 1, start.y - steps, -1):
        line.add(Point(start.x, i))
    last = Point(start.x, start.y - steps)
    line.add(last)
    return line, last

def draw_right(start, steps):
    line = set()
    for i in range(start.x + 1, start.x + steps):
        line.add(Point(i, start.y))
    last = Point(start.x + steps, start.y)
    line.add(last)
    return line, last

def draw_left(start, steps):
    line = set()
    for i in range(start.x - 1, start.x - steps, -1):
        line.add(Point(i, start.y))
    last = Point(start.x - steps, start.y)
    line.add(last)
    return line, last

class Wire:
    def __init__(self, centre):
            self.line = set()
            self.line.add(centre)
            self.last = centre

    def __repr__(self):
        return "%s" % (self.line)

    def wire_up(self, steps):
        line, self.last = draw_up(self.last, steps)
        self.line.update(line)

    def wire_down(self, steps):
        line, self.last = draw_down(self.last, steps)
        self.line.update(line)

    def wire_right(self, steps):
        line, self.last = draw_right(self.last, steps)
        self.line.update(line)

    def wire_left(self, steps):
        line, self.last = draw_left(self.last, steps)
        self.line.update(line)

    def parse_input(self, command):
        head = command[0]
        tail = int(command[1:])

        if head == 'U':
            self.wire_up(tail)
        elif head == 'D':
            self.wire_down(tail)
        elif head == 'R':
            self.wire_right(tail)
        elif head == 'L':
            self.wire_left(tail)

    def update_cable(self, commands):
        for e in commands:
            self.parse_input(e)

def parse_input(input_file):
    with open(input_file) as f:
        wire_positions = f.read().splitlines()
    wire1 = wire_positions[0].split(',')
    wire2 = wire_positions[1].split(',')
    return wire1, wire2

def main(input_file):
    wire1, wire2 = parse_input(input_file)

    cable1 = Wire(Point(0, 0))
    cable1.update_cable(wire1)
    #print(cable1.line)

    cable2 = Wire(Point(0, 0))
    cable2.update_cable(wire2)

    intersections = cable1.line.intersection(cable2.line)
    #print(intersections)
    distances = []
    for e in intersections:
        distances.append(abs(e.x) + abs(e.y))
    print(distances)

    for e in cable1.line:
        plt.scatter(e.x, e.y, color='red')
    for e in cable2.line:
        plt.scatter(e.x, e.y, color='blue')
    plt.show()

if __name__ == "__main__":
    main("test0")
