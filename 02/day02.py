def execute_programme(prog):
    idx = 0
    while(prog[idx] is not 99):
        try:
            if prog[idx] == 1:
                prog[prog[idx + 3]] = prog[prog[idx + 1]] + prog[prog[idx + 2]]
            elif prog[idx] == 2:
                prog[prog[idx + 3]] = prog[prog[idx + 1]] * prog[prog[idx + 2]]
        except:
            pass#print("Out of scope")
        idx += 4

def find_input(exp, prog):
    for n in range(0, 100):
        for v in range(0, 100):
            temp = prog[:]
            temp[1] = n
            temp[2] = v
            execute_programme(temp)
            if temp[0] == exp:
                return n, v
    return -1, -1


def main(input_file):
    with open(input_file) as f:
        programme = f.read().split(',')
    programme = list(map(int, programme))
    original = programme[:]

    execute_programme(programme)
    print("Position [0]:", programme[0])

    expected_value = 19690720
    noun, verb = find_input(expected_value, original)
    print("Noun and verb give", 100 * noun + verb)


if __name__ == "__main__":
    main("input")
