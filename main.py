# coding=utf-8
"""Matching game"""

# imports for the project
import random
import time

# dictionary to translate all possible plot-points to numbers
PLOT_NUMBER_TRANSLATION: dict[str, int] = {
    "a1": 1, "a2": 2, "a3": 3, "a4": 4, "b1": 5, "b2": 6, "b3": 7, "b4": 8,
    "c1": 9, "c2": 10, "c3": 11, "c4": 12, "d1": 13, "d2": 14, "d3": 15,
    "d4": 16
}
# row letters which are valid in input
VALID_ROWS: tuple[str, str, str, str] = ('a', 'b', 'c', 'd')


def clear_py_console(sec: float, lines: int):
    """
    Function to clear x amount of lines after a specified period of time (in seconds)
    :param sec: float
    :param lines: int
    """
    time.sleep(sec)  # sleeps for a period of time specified when the function is called
    print("\n" * lines)  # sends a newline * specified amount (effectively clearing the console)


def input_int_validator(input_text: str, invalid_message: str = "⚠ Invalid input! Please use a round number.") -> int:
    """
    Used to make sure an input is an integer
    :rtype: int
    :param invalid_message:
    :param input_text:
    :return:
    """
    while True:
        try:
            given_input: int = int(input(input_text).strip())
        # catches errors for incorrect datatype
        except ValueError:
            print(invalid_message)  # tells the user they didn't type an integer
        else:  # instead of having the return just be in the try statement, I've put it here
            return given_input


def game_board_print(dictionary: dict):
    """
    Prints the game board for the round; created to reduce duplicated code
    :param dictionary: dict
    """
    print("   ", 1, 2, 3, 4, "\n"
                             "  \u2588 \u2588 \u2588 \u2588 \u2588 \u2588\n"
                             "A \u2588 {} {} {} {} \u2588 A\n"
                             "B \u2588 {} {} {} {} \u2588 B\n"
                             "C \u2588 {} {} {} {} \u2588 C\n"
                             "D \u2588 {} {} {} {} \u2588 D\n"
                             "  \u2588 \u2588 \u2588 \u2588 \u2588 \u2588\n   ".format(dictionary.get(1),
                                                                                       dictionary.get(2),
                                                                                       dictionary.get(3),
                                                                                       dictionary.get(4),
                                                                                       dictionary.get(5),
                                                                                       dictionary.get(6),
                                                                                       dictionary.get(7),
                                                                                       dictionary.get(8),
                                                                                       dictionary.get(9),
                                                                                       dictionary.get(10),
                                                                                       dictionary.get(11),
                                                                                       dictionary.get(12),
                                                                                       dictionary.get(13),
                                                                                       dictionary.get(14),
                                                                                       dictionary.get(15),
                                                                                       dictionary.get(16)),
          1, 2, 3, 4)


def main():
    """
    Main function
    TODO: Change error checking to be in function
    """

    # Dictionary which stores all the values to be used in the game
    card_kv_store: dict[int] = {
        1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6,
        15: 7, 16: 8
    }

    # win counter (starting at 0)
    wins: int = 0
    # main while loop variable
    playing: bool = True

    # prints board layout to introduce the user to the game
    print("Welcome to a game of Memory Game!\nThis is what the board looks like!\n\n"
          "   ", 1, 2, 3, 4, "\n"
                             "  \u2588 \u2588 \u2588 \u2588 \u2588 \u2588\n"
                             "A \u2588 * * * * \u2588 A\n"
                             "B \u2588 * * * * \u2588 B\n"
                             "C \u2588 * * * * \u2588 C\n"
                             "D \u2588 * * * * \u2588 D\n"
                             "  \u2588 \u2588 \u2588 \u2588 \u2588 \u2588\n   ", 1, 2, 3, 4,
          "\nYou choose a position by its line (row) number and column letter, kinda like in Chess! I hope you "
          "enjoy!\n\n")

    # loop for the game
    while playing:
        # turns the dict into a list
        card_list_values = list(card_kv_store.values())
        # shuffles said list
        random.shuffle(card_list_values)  # CWE-338 doesn't apply here
        # turns all keys into asterisks
        card_kv_store = card_kv_store.fromkeys(card_kv_store, "*")

        # boolean variables for use in 'while' loops
        round_in_progress: bool = True
        error_catching: bool = True
        plotting: bool = True

        # code for each round
        while round_in_progress:
            # prints out the current board from the function i made earlier
            game_board_print(card_kv_store)
            # when the user plots a point (chooses rows and columns)
            while plotting:
                # catches errors (specifically catching integer ValueError)
                while error_catching:
                    # asks the user for a row (this is just part of the loop of asking for a plot, invalid input is
                    # caught later on
                    row1: str = input("Please choose a row: ").strip().lower()
                    column1: int = input_int_validator("Please choose a column: ")  # asks the user for input as an int
                error_catching: bool = True  # changes the variable to True because the code is recycled later on

                # TODO: clean this whole area up; I can get rid of a lot of unnecessary code

                # if the inputted rows and columns are valid
                if row1 in VALID_ROWS and 1 <= column1 <= 4:
                    # adds the variables into one "word" (the colon after the var-name is for annotation, which was a
                    # suggestion from my IDE)
                    pos1: str = row1 + str(column1)
                    numeric_pos1: int = PLOT_NUMBER_TRANSLATION.get(pos1)  # translates the plotted point into a number
                    # gets the shuffled number which corresponds with the translated number (adds a 1 to account for the
                    # list starting at 0)
                    match1: str = card_list_values[numeric_pos1 - 1]
                    plotting: bool = False  # plotted position was in correct bounds so we escape the loop
                else:
                    print("⚠ Invalid input, try again.")  # the user's input was out of bounds
            plotting: bool = True  # beep boop, recycled variable

            while plotting:
                while error_catching:
                    # asks the user for row2, pretty much duplicated from the plot 1 code
                    row2: str = input("Please choose your second selection's row: ").strip().lower()
                    # error-catches again
                    try:
                        column2: int = int(input("Please choose your second selection's column: ").strip())
                        error_catching: bool = False
                    except ValueError:
                        print("")
                error_catching: bool = True
                # same as before
                if row2 in VALID_ROWS and 1 <= column2 <= 4:
                    # makes sure the input isn't identical to the first plot point, and if it is, notifies the user and
                    # makes the user input a new value
                    if row1 == row2 and column1 == column2:
                        print("⚠ Identical inputs are not allowed.")
                    # if not identical (aka else), continue along with the code (which is pretty much identical to
                    # plot-point 1
                    else:
                        pos2: str = row2 + str(column2)
                        numeric_pos2: int = PLOT_NUMBER_TRANSLATION.get(
                            pos2)  # translates the plotted point into a number
                        match2: str = card_list_values[numeric_pos2 - 1]
                        plotting: bool = False  # plotted position was in correct bounds so we escape the loop
                else:
                    print("⚠ Invalid input, try again.")
            plotting: bool = True  # beep boop, recycled variable

            # if both of the inputs match
            if match1 == match2:
                # we tell the user it was a match
                print("👏 MATCH!")
                # puts the numbers back in the dictionary so it gets printed
                card_kv_store[numeric_pos1]: str = match1
                card_kv_store[numeric_pos2]: str = match2
            # otherwise if there's not a match, we tell the user both numbers then clear after 3 seconds
            else:
                print(
                    f"{pos2.title()} does not match {pos1.title()} unfortunately.\n{pos1.title()} is {match1} and "
                    f"{pos2.title()} "
                    f"is {match2} though!"
                    "\n\nWe'll be hiding these values in 3 seconds, so memorize up❗")
                # this is calling the function i made at the top of the file
                clear_py_console(3, 1000)
            # checks if there are no * chars in the dict (which means the user has completed the game)
            if "*" not in card_kv_store.values():
                # round is no longer in progress
                round_in_progress: bool = False
                # adds the win to the user
                wins += 1
                # tells the user they completed the game
                print("✨ Looks like you paired up all the numbers! ✨")

                # TODO: add sqlite code here

                # prints out completed board
                game_board_print(card_kv_store)
                # asks the user if they would like to keep playing
                round_end: str = input(
                    "Well done! Game completed, would you like to play another round?\nType 'y' to play another round, "
                    "or anything else to finish this session.\nInput: ").lower().strip()
                # if yes print next round incoming and go to the top of the code (repeat the while loop
                if round_end == "y":
                    print("Alright! Next round incoming. . .")
                # else finish the game
                else:
                    print("Your wins this session:", wins)
                    # turns off while loop and doesn't go back to start of loop as it has ended
                    playing: bool = False
    # end of game
    print("Thanks for playing!")
    # raises the exit error, pretty much what sys.exit() does
    raise SystemExit


if __name__ == "__main__":
    main()
