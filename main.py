#!/usr/bin/env python3.10
# coding=utf-8
"""
Matching game.
I'm not using many classes because python classes aren't great, and in my opinion, for this use case, functions are
adequate.
I am using a database class though

This code is flexible and robust for its use case, however, doesn't allow for having a larger grid.

I'd like to acknowledge that I only use pandas for the dataframe, but firstly, it's easier to pull data into
matplotlib using pandas instead of having to set up my own logic,
and secondly, it makes the program easier to expand on in future (I could've set up the graph using pandas too using
.plot on the dataframe directly, but this was easier to understand).

For in the future, I could set up a customizable database name and a reset option (with confirmation), but that's just
extra bells and whistles, and if the user really wanted to do either of those things, the code makes enough sense for
simple modification by a person with relatively decent knowledge of Python.

Another thing I could do to expand the game is to allow the user to graph not only by attempt/id, but also by
timestamp.
Timestamps are stored for this reason,
and if I'm not mistaken they're stored in ISO-8601
(if I update the game after submitting it, I may change that to millisecond-precision integer/epoch time)

This is a huge docstring as I'm aware, so lastly, I do want to acknowledge that I have GitHub Copilot and JetBrains'
Full Line Code Completion installed, and if I recall correctly I only used GitHub Copilot once,
for completing two lines in my graph_attempts() function, and for JetBrains' Full Line Code Completion,
I don't think I used what it suggested, but I'm declaring it anyway.
"""

# imports for the project
import sqlite3
import time

from matplotlib import pyplot as plt
import pandas as pd
from random import shuffle
# this may be considered excessive precision, but I don't mind
from timeit import default_timer as timer

# dictionary to translate all possible plot-points to numbers
PLOT_NUMBER_TRANSLATION: dict[str, int] = {
    "a1": 1, "a2": 2, "a3": 3, "a4": 4, "b1": 5, "b2": 6, "b3": 7, "b4": 8,
    "c1": 9, "c2": 10, "c3": 11, "c4": 12, "d1": 13, "d2": 14, "d3": 15,
    "d4": 16
}
# row letters which are valid in input
VALID_ROWS: tuple[str, str, str, str] = ('a', 'b', 'c', 'd')


# Deriving from object (not necessary but looks better, in my opinion)
class Database(object):
    """
    Database class
    """

    def __init__(self, db_name: str):
        """
        Database initialization logic
        :param db_name:
        """
        # Initialize the database (if it doesn't exist, a new file is created)
        self.connection = sqlite3.connect(db_name)
        # Set the cursor variable
        self.cursor = self.connection.cursor()
        # create a db table if it doesn't exist.
        # I'm aware that the autoincrement is redundant, as with having an 'id' column at all as
        # there's a built-in rowid which the id column just aliases to (unless using 'WITHOUT ROWID', which i'm not
        # doing right now as it's not worth the effort), but I've set it up this way on purpose.
        # Switching to no rowid is something I may do if I ever come back to working on this after submitting it.
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS Highscores (
            'ID' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            'attempt_length' REAL DEFAULT 0.0 NOT NULL, 
            'attempt_timestamp' DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL 
            );
        '''
        )

    def insert_row(self, length: float):
        """
        Inserts a new row for an attempt
        :param length:
        """
        self.cursor.execute(f"INSERT INTO Highscores (attempt_length) VALUES ({length})")
        self.connection.commit()


def graph_attempts(attempts: pd.DataFrame):
    """
    Function to graph the attempts
    :param attempts: pd.DataFrame
    """
    # set the plot size
    plt.figure(figsize = (10, 8))
    # set the x-axis to be the attempt length
    plt.plot(attempts["attempt_length"])
    # set the y-axis to be the attempt length
    plt.ylabel("Attempt Length (time taken in seconds)")
    # set the x-axis to be the attempt length
    plt.xlabel("Attempt Number")
    # show the plot
    plt.show()
    print("A window showing you the graph should've appeared. You'll be taken back to the menu in 5 seconds, "
          "but the graph should stay open until you close it yourself!")
    time.sleep(5)


def clear_py_console(sec: float, lines: int):
    """
    Function to clear x number of lines after a specified period of time (in seconds)
    :param sec: float
    :param lines: int
    """
    time.sleep(sec)  # sleeps for a period of time specified when the function is called
    print("\n" * lines)  # sends a newline * specified amount (effectively clearing the console)


def input_int_validator(input_text: str, invalid_message: str = "⚠ Invalid input for column!\n"
                                                                "Valid inputs: '1', '2', '3', '4'") -> int:
    """
    Used to make sure an input is an integer, as well as making sure it's a valid input.
    I'm aware the 1 <= given_input <= 4 makes the code not as reusable, unlike with the string validation,
    but that's because string validation is easier and the functions only are used to validate the row and column
    inputs.
    :rtype: int
    :param invalid_message: str, error message given if check fails
    :param input_text: str, message to ask
    :return:
    """
    # we don't need to use a variable here because once the function returns, no more function code is executed
    while True:
        try:
            given_input: int = int(input(input_text).strip())  # scans for input
        # catches errors for incorrect datatype
        except ValueError:
            print(invalid_message)  # tells the user they didn't type an integer
        else:  # instead of having the return just be in the try statement, I've put it here
            # if the input is valid
            if 1 <= given_input <= 4:  # I know this looks like it ruins re-usability,
                # but the function has a specific use case
                return given_input
            else:
                print(invalid_message)


def input_str_validator(input_text: str, valid_inputs: tuple,
                        invalid_message: str = "⚠ Invalid input for row!\nValid inputs: 'a', 'b', 'c', 'd'") -> str:
    # noinspection SpellCheckingInspection
    """
        Used to make sure an input is valid.
        I know I'm feeding the function a tuple and not a list, and I *could've* used a list + list annotation which'd
        make the code more re-usable, but again, the code is purpose-specific.
        :rtype: str
        :param valid_inputs: tuple, Valid inputs as a tuple to check against
        :param input_text: str, message to ask
        :param invalid_message: str, message to give on check failure
        :return:
        """
    # we don't need to use a variable here because once the function returns, no more function code is executed
    while True:
        given_input: str = input(input_text).strip().lower()  # scans for input
        # if the input is valid return it, otherwise loop !!!
        if given_input in valid_inputs:
            return given_input
        print(invalid_message)  # no point slapping this into an 'else' statement when it won't run if it returns
        # correctly


def string_int_concatenator(string: str, integer: int) -> str:
    """
    A dead simple string and integer concatenator, without the overhead for unnecessary flexibility.
    Doesn't value check because it's done earlier.
    :return:
    :rtype: str
    :type string: str
    :param string: str, string to concatenate the integer onto
    :param integer: int, integer to turn into string and add to the string
    """
    return string + str(integer)


def game_board_print(dictionary: dict):
    """
    Prints the game board for the round; created to reduce duplicated code (I could've done this as an f-string but
    there's no point in it for right now)
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

    Game caveats: You can attempt to rematch an already-matched pair
    """
    # Call an instance of the database class
    db = Database(r"highscores.db")

    # Dictionary which stores all the values to be used in the game
    card_kv_store: dict[int] = {
        1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6,
        15: 7, 16: 8
    }

    # win counter (starting at 0)
    wins: int = 0
    # while loop variables
    playing: bool = True
    choosing_option: bool = True
    while choosing_option:
        # Python 3.10 has nifty new switch-case statements (instead of using switch they call it match though)
        match input("Would you like to play a game of Memory, or view your scores as a graph from when you last "
                    "played (if you've played before)\nType 'memory' to play a round, or 'graph' to "
                    "view a graph: ").lower().strip():
            case "memory":
                print("Sounds good, let's play!")
                choosing_option = False
            case "graph":
                print("Showing you your graph...")
                df: pd.DataFrame = pd.read_sql_query("SELECT * from Highscores", db.connection)
                graph_attempts(df)

            case _:
                print("Invalid or mistyped input, try again.\n")

    # prints board layout to introduce the user to the game (i could've messed around with having all my logic be
    # done before I print this, but there's no benefit to it)
    print("Welcome to a round of Memory Game!\nThis is what the board looks like!\n\n"
          "   ", 1, 2, 3, 4, "\n"
                             "  \u2588 \u2588 \u2588 \u2588 \u2588 \u2588\n"
                             "A \u2588 * * * * \u2588 A\n"
                             "B \u2588 * * * * \u2588 B\n"
                             "C \u2588 * * * * \u2588 C\n"
                             "D \u2588 * * * * \u2588 D\n"
                             "  \u2588 \u2588 \u2588 \u2588 \u2588 \u2588\n   ", 1, 2, 3, 4,
          "\nYou choose a position by its row (line) letter and column number, kinda like in Chess!\nThere are two of "
          "each 'card', and your goal is to find the 8 pairs in the quickest time possible.\nIf you don't find a pair "
          "in your two selections, the game tells you the two cards' values, \nbut memorise quickly as the screen "
          "spams blank lines shortly after displaying those values! I hope you enjoy :)\n\n")

    # loop for the game
    while playing:
        # turns the dict into a list
        card_list_values = list(card_kv_store.values())
        # shuffles said list
        shuffle(card_list_values)  # CWE-338 doesn't apply here
        # turns all keys into asterisks
        card_kv_store = card_kv_store.fromkeys(card_kv_store, "*")
        # boolean variables for use in 'while' loops
        round_in_progress: bool = True

        # code for each round
        start = timer()
        while round_in_progress:
            # keep getting IDE warnings; this just makes sure all the variables are firstly initialized (yes yes,
            # i know python is dynamic), and secondly ensure reset on each iteration
            row1, row2, column1, column2 = "", "", 0, 0
            # prints out the current board from the function i made earlier
            game_board_print(card_kv_store)
            # when the user plots a point (chooses rows and columns)
            # asks the user for a row (this is just part of the loop of asking for a plot, invalid input is
            # caught later on
            row1: str = input_str_validator("Please choose a row: ", VALID_ROWS)
            column1: int = input_int_validator("Please choose a column: ")  # asks the user for input as an int

            # concatenation
            pos1: str = string_int_concatenator(row1, column1)

            numeric_pos1: int = PLOT_NUMBER_TRANSLATION.get(pos1)  # translates the plotted point into a number
            # gets the shuffled number which corresponds with the translated number (adds a 1 to account for the
            # list starting at 0)
            match1: str = card_list_values[numeric_pos1 - 1]

            # asks the user for row2, pretty much duplicated from the plot 1 code
            duplicate_checking: bool = True
            while (row2 == "" and column2 == 0) or duplicate_checking:
                row2: str = input_str_validator("Please choose your second selection's row: ", VALID_ROWS)
                # error-catches again
                column2: int = input_int_validator("Please choose your second selection's column: ")
                # makes sure the input isn't identical to the first plot point, and if it is, notifies the user and
                # makes the user input a new value
                if row1 == row2 and column1 == column2:
                    print("⚠ Identical inputs are not allowed.")
                else:
                    duplicate_checking: bool = False
                # if not identical (aka else), continue along with the code (which is pretty much identical to
                # plot-point 1
            pos2: str = string_int_concatenator(row2, column2)
            numeric_pos2: int = PLOT_NUMBER_TRANSLATION.get(pos2)  # translates the plotted point into a number
            match2: str = card_list_values[numeric_pos2 - 1]

            # if both the inputs match
            if match1 != match2:
                print(
                    f"{pos2.title()} does not match {pos1.title()} unfortunately.\n{pos1.title()} is {match1} and "
                    f"{pos2.title()} "
                    f"is {match2} though!"
                    "\n\nWe'll be hiding these values in 3 seconds, so memorize up❗")
                # this is calling the function i made at the top of the file
                clear_py_console(3, 1000)

            # otherwise, if there's not a match, we tell the user both numbers then clear after 3 seconds
            else:
                # we tell the user it was a match
                print("👏 MATCH!")
                # puts the numbers back in the dictionary so it gets printed
                card_kv_store[numeric_pos1]: str = match1
                card_kv_store[numeric_pos2]: str = match2
            # checks if there are no * chars in the dict (which means the user has completed the game)
            if "*" not in card_kv_store.values():
                # end the timer
                end = timer()
                time_taken: float = end - start
                # round is no longer in progress
                round_in_progress: bool = False
                # adds the win to the user
                wins += 1
                # tells the user they completed the game
                print("✨ Looks like you paired up all the numbers! ✨")

                # Insert a new row for this attempt with the time taken
                db.insert_row(time_taken)

                # prints out completed board
                game_board_print(card_kv_store)
                # asks the user if they would like to keep playing and listens for input
                round_end: str = input(
                    "Well done! Game completed, would you like to play another round?\nType 'y' to play another round, "
                    "or anything else to finish this session.\nInput: ").lower().strip()
                # if yes print next round incoming and go to the top of the code (repeat the while loop), it doesn't
                # scan for valid input,
                # because attempts are stored in the db so progress isn't lost on game end.
                if round_end == "y":
                    print("Alright! Next round incoming. . .")
                # else finish the game
                else:
                    print("Your wins this session:", wins)
                    # turns off while loop and doesn't go back to start of loop as it has ended
                    playing: bool = False
    # end of game
    print("Thanks for playing!")
    # Close the sqlite3 connection
    db.connection.close()
    # raises the exit error, pretty much what sys.exit() does
    raise SystemExit


if __name__ == "__main__":
    main()
