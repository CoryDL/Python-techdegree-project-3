import random
from phrasehunter.phrase import Phrase

class Game:

    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def welcome(self):
        print("\n\n     ==================================\n"
              "          Welcome to Phrase Hunter\n"
              "     ==================================\n\n"
              "             Hunt the phrase!\n" 
              "       Correct guesses earns a letter,\n"
              "  guess wrong 5 times and the game is over!\n"
              "     __________________________________\n\n")


    def create_phrases(self):  # Creates a list of Phrase class objects, from the phrases in the list
        self.phrase_list = ['Tongue in cheek',
               'Thick as thieves',
               'Loose lips sink ships',
               'Last but not least',
               'Time is money']

        self.phrase_objects = []

        for item in self.phrase_list:
            self.phrase_objects.append(Phrase(item))
        return self.phrase_objects
    

    def get_random_phrase(self):  # Randomly gets a phrase from the list
        self.random_index = random.randint(0, len(self.phrases) -1)

        return self.phrases[self.random_index]


    def start(self):  # Starts the game, utilizes other methods to keep track of the phrase and guesses
        self.welcome()   
        
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(f"           Incorrect guesses: {self.missed}\n\n")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            if not self.active_phrase.check_letter(user_guess):
                self.missed += 1

        self.game_over()    
    

    def get_guess(self):  # Handles the user input for the guess
        while True:
            try:
                user_guess = input("Guess a letter: ")
                if len(user_guess) > 1 or not user_guess.isalpha():
                    raise Exception("That is an invalid guess. Please enter one letter.")
            except Exception as e:
                print(e)
            else:
                return user_guess
                break


    def game_over(self):
        if self.missed == 5:
            print("You missed too many times.\n     GAME OVER\n")
        else:
            print(f"\n The correct phrase was {self.active_phrase.phrase}!!!\n\n Congratulations, you won!!\n\n")
        self.replay()


    def replay(self):  # handles the user input for replaying the game, calls the __init__ method and restarts
        answer_list = ['y','yes','n','no']

        while True:
            try:
                play_again = input("Would you like to play again? [Y]es/[N]o: ")
                if play_again.lower() not in answer_list:
                    raise Exception("Please enter [Y]es/[N]o")                  
            except ValueError:
                print('Please enter a [Y]es or [N]o.')
            except Exception as e:
                print(e)    
            if play_again.lower() == 'y' or play_again.lower() == 'yes':
                self.__init__()
                self.start()            
            elif play_again.lower() == 'n' or play_again.lower() == 'no':
                print("\nThe game is ending, see you next time!")
                exit()
                                   