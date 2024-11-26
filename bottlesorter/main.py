import sys

from bottle import Bottle
import levels


def print_board(list_bottles):
    """Prints to screen the contents of each bottle"""
    for b in list_bottles:
        print(b.show_contents())
    print("\n")

    if is_game_complete(list_bottles):
        print("Game Complete")
        again = input('Play again? [Y/N] ')
        if again and again.upper() in ('Y', 'YES'):
            play_game()
    else:
        print("Next move?\n")


def pour_bottle_to_bottle(bottle_from: Bottle, bottle_to: Bottle):
    """Pours the top contents from one bottle to another and check to see
    pour is valid"""
    if len(bottle_from.contents) > 0 and bottle_to.valid_pour(bottle_from.contents[-1]):
        bottle_to.add_contents(bottle_from.remove_contents())
        if (
            len(bottle_from.contents) != 0
            and bottle_from.contents[-1] == bottle_to.contents[-1]
        ):
            pour_bottle_to_bottle(bottle_from, bottle_to)
    else:
        print("*** Invalid Pour ***")


def is_game_complete(list_bottles):
    """Check to see if all bottles are sorted"""
    return sum(not b.is_bottle_complete() for b in list_bottles) == 0


def play_game():
    """Recode of Water Sort Puzzle game developed by IEC GLOBAL PTY LTD for learning purpose only"""

    min_level = list(levels.level_dict.keys())[0]
    max_level = list(levels.level_dict.keys())[-1]

    level = input(f"Choose a level from {min_level} - {max_level}: ")
    list_of_bottles = levels.get_games(**levels.level_dict[int(level)])

    print_board(list_of_bottles.values())

    b_from_str = ""
    b_to_str = ""

    while (
            not is_game_complete(list_of_bottles.values())
            and b_from_str != "q"
            and b_to_str != "q"
    ):
        b_from_str = input(
            f"Choose a bottle to pour from ({', '.join(list(list_of_bottles.keys()))}) or q to quit: "
        )
        if b_from_str == "q":
            sys.exit()
        if b_from_str not in list_of_bottles.keys():
            print("Selection not in list")
            continue
        b_to_str = input("Select bottle to pour to: ")
        if b_to_str not in list_of_bottles.keys():
            print("Selection not in list")
            continue
        if b_to_str == b_from_str:
            print("You can not select the same bottle")
            continue

        b_from = list_of_bottles[b_from_str]
        b_to = list_of_bottles[b_to_str]

        pour_bottle_to_bottle(b_from, b_to)
        print_board(list_of_bottles.values())


if __name__ == "__main__":
    play_game()

