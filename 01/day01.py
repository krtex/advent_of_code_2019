def calculate_fuel(fuel):
    return fuel // 3 - 2

def calculate_total_fuel(fuel_list):
    sum = 0
    for i in fuel_list:
        sum += calculate_fuel(i)
    return sum

def calculate_extra_fuel(fuel_list):
    sum = 0
    for i in fuel_list:
        temp = calculate_fuel(i)
        sum += temp
        while(temp > 8): # magic number! 8 / 3 - 2 = 0, so we need greater numbers
            temp = calculate_fuel(temp)
            sum += temp
    return sum


def main(input_file):
    with open(input_file) as f:
        fuel_list = f.read().splitlines()
    fuel_list = list(map(int, fuel_list))

    print("Part 1: ", calculate_total_fuel(fuel_list))
    print("Part 2: ", calculate_extra_fuel(fuel_list))

if __name__ == "__main__":
    main("input")
