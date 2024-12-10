class Phrase:


    def __init__(self, phrase):
        self.phrase = phrase.lower()


    def display(self, guesses):  # Displays letters or underscores that represent the phrase
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter }", end=" ")
            else:
                print(f"_ ", end=" ")
        print("\n")


    def check_letter(self, guess):  # Checks the guessed letter to see if it is in the phrase
        return guess in self.phrase


    def check_complete(self, guesses):  # Checks the letters in the phrase against the letters guessed
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
