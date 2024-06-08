class Choice:
    choice: str
    player_1_char: str
    player_2_char: str
    selection_score: int
    beats: str
    loses_to_char: str
    beats_char: str

    def __init__(
        self,
        choice: str,
        player_1_char: str,
        player_2_char: str,
        selection_score: int,
        beats: str,
        loses_to_char: str,
        beats_char: str
    ):
        self.choice = choice
        self.player_1_char = player_1_char
        self.player_2_char = player_2_char
        self.selection_score = selection_score
        self.beats = beats
        self.loses_to_char = loses_to_char
        self.beats_char = beats_char


ROCK = Choice("Rock", "A", "X", 1, "Scissors", "Y", "Z")
PAPER = Choice("Paper", "B", "Y", 2, "Rock", "Z", "X")
SCISSORS = Choice("Scissors", "C", "Z", 3, "Paper", "X", "Y")


def read_file():
    with open('rps-strategy-guide.txt', 'r') as file:
        return [line.strip() for line in file.read().split("\n")]


def get_choice_for_player_1(choice: str) -> Choice:
    match choice:
        case ROCK.player_1_char:
            return ROCK
        case PAPER.player_1_char:
            return PAPER
        case SCISSORS.player_1_char:
            return SCISSORS


def get_choice_for_player_2(choice: str) -> Choice:
    match choice:
        case ROCK.player_2_char:
            return ROCK
        case PAPER.player_2_char:
            return PAPER
        case SCISSORS.player_2_char:
            return SCISSORS
        

def get_player_2_choice_and_score_for_outcome(choice_one: Choice, outcome: str) -> str:
    """
    X = loss
    Y = draw
    Z = win
    """
    match outcome:
        case 'X':
            return get_choice_for_player_2(choice_one.beats_char), 0
        case 'Y':
            return choice_one, 3
        case 'Z':
            return get_choice_for_player_2(choice_one.loses_to_char), 6
        

def rock_paper_scissors_p1(choice_one: str, choice_two: str):
    """
    Given two selections of Rock (A for player  1 / X for player 2), Paper (B for player 1 / Y for
    player 2) or Scissors (C for player 1 / Z for player 2), determine a score for each player.
    Scoring is as follows:
     - 1, 2 and 3 points for selecting Rock, Paper, Scissors, respectively
     - 0 for a round loss, 3 for a draw and 6 for a win
    """
    player_1_round_score: int = 0
    player_2_round_score: int = 0

    player_1_choice = get_choice_for_player_1(choice_one)
    player_2_choice = get_choice_for_player_2(choice_two)

    player_1_round_score += player_1_choice.selection_score
    player_2_round_score += player_2_choice.selection_score

    if player_1_choice.beats == player_2_choice.choice:
        player_1_round_score += 6
    elif player_2_choice.beats == player_1_choice.choice:
        player_2_round_score += 6
    else:
        player_1_round_score += 3
        player_2_round_score += 3
    return [player_1_round_score, player_2_round_score]


def rock_paper_scissors_p2(choice_one: str, round_outcome: str):
    """
    Given two selections of Rock (A for player  1 / X for player 2), Paper (B for player 1 / Y for
    player 2) or Scissors (C for player 1 / Z for player 2), determine a score for each player.
    Scoring is as follows:
     - 1, 2 and 3 points for selecting Rock, Paper, Scissors, respectively
     - 0 for a round loss, 3 for a draw and 6 for a win
    """
    player_2_round_score: int = 0

    player_1_choice = get_choice_for_player_1(choice_one)
    player_2_choice, score = get_player_2_choice_and_score_for_outcome(player_1_choice, round_outcome)

    player_2_round_score += player_2_choice.selection_score
    player_2_round_score += score

    return player_2_round_score


def process_strategy_guide_p1():
    """
    Given file of suggested moves, calculate player two's total score if each round is
    played as per strategy guide.
    E.g.
        A Y
        B X
        C Z
    """
    opponents_total_score: int = 0
    my_total_score: int = 0

    for game in read_file():
        choices = game.split(" ")
        if len(choices) < 2:
            continue
        player_1_score, player_2_score = rock_paper_scissors_p1(choices[0], choices[1])
        opponents_total_score += player_1_score
        my_total_score += player_2_score

    return my_total_score

def process_strategy_guide_p2():
    """
    Given file of moves for player 1 and desired outcome for player 2, calculate player two's total score if 
    each round is played as per strategy guide.
    E.g.
        A Y
        B X
        C Z
    """
    my_total_score: int = 0

    for game in read_file():
        values = game.split(" ")
        if len(values) < 2:
            continue
        player_1_choice = values[0]
        player_2_round_outcome = values[1]
        my_score = rock_paper_scissors_p2(player_1_choice, player_2_round_outcome)
        my_total_score += my_score

    return my_total_score


def main():
    """ """
    part_one_solution = process_strategy_guide_p1()
    part_two_solution = process_strategy_guide_p2()
    print(f"Part 1 solution: {part_one_solution}")
    print(f"Part 2 solution: {part_two_solution}")

if __name__ == "__main__":
    main()
    
