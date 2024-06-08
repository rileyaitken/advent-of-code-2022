def read_file():
    with open('elf-cleaning-sections.txt', 'r') as file:
        return [line.strip() for line in file.read().split("\n")]
    

def get_lo_and_hi(sections):
    values = sections.split('-')
    return int(values[0]), int(values[1])
    

def get_elf_cleaning_sections(pair):
    sections = pair.split(',')
    elf_1_sections = sections[0]
    elf_2_sections = sections[1]

    elf_1_lo, elf_1_hi = get_lo_and_hi(elf_1_sections)
    elf_2_lo, elf_2_hi = get_lo_and_hi(elf_2_sections)
    
    return elf_1_lo, elf_1_hi, elf_2_lo, elf_2_hi


def check_if_overlapping_sections(pair):
    elf_1_lo, elf_1_hi, elf_2_lo, elf_2_hi = get_elf_cleaning_sections(pair)

    if elf_1_lo > elf_2_hi or elf_2_lo > elf_1_hi:
        return False
    else:
        return True

def check_if_double_up(pair):
    elf_1_lo, elf_1_hi, elf_2_lo, elf_2_hi = get_elf_cleaning_sections(pair)

    if elf_1_lo >= elf_2_lo and elf_1_hi <= elf_2_hi:
        return True
    elif elf_2_lo >= elf_1_lo and elf_2_hi <= elf_1_hi:
        return True
    else:
        return False


def solutions():
    """
    Check for elf pairs where one elf has been assigned sections that have all
    been assigned to other elf.
    Check for elf pairs with any overlap in assigned sections.
    E.g.
        2-4,6-8
        2-3,4-5
        5-7,7-9
        2-8,3-7
        6-6,4-6
        2-6,4-8
    """
    num_double_ups: int = 0
    num_overlaps: int = 0
    elf_pairs = read_file()
    for pair in elf_pairs:
        if check_if_double_up(pair):
            num_double_ups += 1
        if check_if_overlapping_sections(pair):
            num_overlaps += 1
    return num_double_ups, num_overlaps


def main():
    """ """
    part_one_solution, part_two_solution = solutions()
    print(f"Part 1 solution: {part_one_solution}")
    print(f"Part 2 solution: {part_two_solution}")


if __name__ == "__main__":
    main()