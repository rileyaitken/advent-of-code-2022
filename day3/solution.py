from string import ascii_lowercase, ascii_uppercase

LOWERCASE_LETTERS = list(ascii_lowercase)
UPPERCASE_LETTERS = list(ascii_uppercase)


def read_file():
    with open('rucksack-items.txt', 'r') as file:
        return [line.strip() for line in file.read().split("\n")]
    

def split_list(list: list):
    half = len(list) // 2
    return list[:half], list[half:]


def get_item_priority(item):
    try:
        return LOWERCASE_LETTERS.index(item) + 1
    except ValueError:
        try:
            return UPPERCASE_LETTERS.index(item) + 27
        except ValueError:
            print(f"Error finding {item}")
            return 0


def find_duplicate_rucksack_item_priority(rucksack: str):
    rucksack_items = list(rucksack)
    compartment_one_items, compartment_two_items = split_list(rucksack_items)

    for item in compartment_one_items:
        if item in compartment_two_items:
            return get_item_priority(item)
        

def sum_duplicate_rucksack_item_priorities():
    """
    Find matching item in each compartment of rucksack, where each compartment holds
    exactly half of all items. Item priority is equivalent to the letter's position
    in the alphabet; 1-26 for lowercase, and 27-52 for uppercase.
    Find the sum of duplicate item priorities in each rucksack.
    E.g.
        vJrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw
    """
    priority_sum: int = 0
    rucksacks = read_file()
    for rucksack in rucksacks:
        if rucksack != "":
            priority = find_duplicate_rucksack_item_priority(rucksack)
            priority_sum += priority
    return priority_sum


def find_elf_group_badge_priority(rucksack_one, rucksack_two, rucksack_three):
    for item in rucksack_one:
        if item in rucksack_two and item in rucksack_three:
            return get_item_priority(item)


def sum_elf_group_badge_priorities():
    priority_sum: int = 0
    rucksacks = read_file()
    idx: int = 0

    while idx < len(rucksacks) - 1:
        priority_sum += find_elf_group_badge_priority(list(rucksacks[idx]), list(rucksacks[idx + 1]), list(rucksacks[idx + 2]))
        idx += 3

    return priority_sum
                                                                                                    
                                                                                
def main():
    """ """
    part_one_solution = sum_duplicate_rucksack_item_priorities()
    print(f"Part 1 solution: {part_one_solution}")

    part_two_solution = sum_elf_group_badge_priorities()
    print(f"Part 2 solution: {part_two_solution}")

if __name__ == "__main__":
    main()