import random, requests, os
from colored import bg, attr, fg
from bs4 import BeautifulSoup


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class Wordle:
    def __init__(self):
        clear()
        os.system("title Wordle")
        self.guesses = 6
        self.guessed = []
        self.word = self.assign_word()
        self.start_game()

    def assign_word(self):
        r = requests.get("https://www.thefreedictionary.com/5-letter-words.htm")
        soup = BeautifulSoup(r.text, "html.parser")
        wordsl = soup.find("div", "TCont")
        for words in wordsl:
            words = [word.text.upper() for word in words.children]
            return random.choice(words)

    def grey(self, text):
        return f"{fg(0)}{bg(241)} {text} {attr(0)} "

    def yellow(self, text):
        return f"{fg(0)}{bg(3)} {text} {attr(0)} "

    def green(self, text):
        return f"{fg(0)}{bg(10)} {text} {attr(0)} "

    def display_board(self):
        if self.guessed[-1] == self.word:
            print("".join(self.green(letter) for letter in self.word))
            print("Congrats! You Won!")
            self.guesses = 0
            return
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        for guessed in self.guessed:

            for index, letter in enumerate(guessed):
                letter = letter.upper()

                if letter in list(self.word) and list(self.word)[index] == letter:
                    print(
                        self.green(letter.upper()),
                        end="┃ " if letter != guessed[-1] else "",
                    )
                elif letter in list(self.word) and list(self.word)[index] != letter:
                    print(
                        self.yellow(letter.upper()),
                        end="┃ " if letter != guessed[-1] else "",
                    )
                else:
                    print(
                        self.grey(letter.upper()),
                        end="┃ " if letter != guessed[-1] else "",
                    )
            print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    def start_game(self):
        print(
            f"""
██╗    ██╗  ██████╗  ██████╗  ██████╗  ██╗      ███████╗
██║    ██║ ██╔═══██╗ ██╔══██╗ ██╔══██╗ ██║      ██╔════╝
██║ █╗ ██║ ██║   ██║ ██████╔╝ ██║  ██║ ██║      █████╗
██║███╗██║ ██║   ██║ ██╔══██╗ ██║  ██║ ██║      ██╔══╝
╚███╔███╔╝ ╚██████╔╝ ██║  ██║ ██████╔╝ ███████╗ ███████╗
 ╚══╝╚══╝   ╚═════╝  ╚═╝  ╚═╝ ╚═════╝  ╚══════╝ ╚══════╝"""
        )
        print(f"Welcome to Wordle!")
        print(f"Guess a 5 letter word!")
        print(f"You have 6 guesses!")
        print(f"Good Luck!\n")
        while self.guesses != 0:
            os.system(f"title Wordle - {self.guesses} guesses left")

            if self.guesses != 6:
                clear()
                print(
                    f"""
██╗    ██╗  ██████╗  ██████╗  ██████╗  ██╗      ███████╗
██║    ██║ ██╔═══██╗ ██╔══██╗ ██╔══██╗ ██║      ██╔════╝
██║ █╗ ██║ ██║   ██║ ██████╔╝ ██║  ██║ ██║      █████╗
██║███╗██║ ██║   ██║ ██╔══██╗ ██║  ██║ ██║      ██╔══╝
╚███╔███╔╝ ╚██████╔╝ ██║  ██║ ██████╔╝ ███████╗ ███████╗
 ╚══╝╚══╝   ╚═════╝  ╚═╝  ╚═╝ ╚═════╝  ╚══════╝ ╚══════╝"""
                )
                self.display_board()
            os.system(f"title Wordle - {self.guesses} guesses left")
            if self.guesses == 0:
                print("You lost!")
                print(f"The word was {self.word}")
                break
            while True:
                guess = input(">> ")
                if len(guess) == 5 and guess.isalpha():
                    break
                else:
                    print("Please enter a 5 letter word with only letters!")
            self.guessed.append(guess)
            self.guesses -= 1
        if self.guesses == 0 and self.guessed[-1] != self.word:
            print("\nYou lost!")
            print(f"The word was {self.word}")
        while True:
            play_again = input("Would you like to play again? (Y/N): ")
            if play_again.upper() == "Y":
                self.__init__()
                break
            elif play_again.upper() == "N":
                print("Thanks for playing!")
                break
            else:
                print("Please enter Y or N!")


Wordle()
