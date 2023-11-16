def read_file():
    with open('elf-calories.txt', 'r') as file:
        return [line.strip() for line in file.read().split("\n")]

def part_one():

    greatest_calories: int = 0
    current_elf_calories: int = 0

    for calorie_count in read_file():

        # end of elf calorie count grouping
        if calorie_count == "":
            if current_elf_calories > greatest_calories:
                greatest_calories = current_elf_calories
            current_elf_calories = 0
            continue
        else:
            current_elf_calories += int(calorie_count)

    return greatest_calories

def part_two():
    """
    Additional space complexity maintaining list of sums
    """
    elf_sums = []
    current_elf_calories: int = 0

    for calorie_count in read_file():
        # end of elf calorie count grouping
        if calorie_count == "":
            elf_sums.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(calorie_count)

    elf_sums = sorted(elf_sums)
    highest = elf_sums[-1]
    top_3 = sum(elf_sums[-3:])
    return highest, top_3

def main():
    """
    E.g.
        1000
        2000
        3000

        4000

        5000
        6000

        7000
        8000
        9000

        10000
    """
    part_one_solution, part_two_solution = part_two()
    return part_one_solution, part_two_solution

if __name__ == "__main__":
    p1, p2 = main()
    print(f'Part 1 solution: {p1}')
    print(f'Part 2 solution: {p2}')
