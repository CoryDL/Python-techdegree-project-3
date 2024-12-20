"Phrase Hunter" is a console-based word guessing game. 
It uses Python and OOP (Object-Oriented Programming) approaches to select a phrase at random, hidden from the player. 
A player tries to guess the phrase by inputting individual characters.

There is a Game class for managing the game, and a Phrase class to help with storing attributes of a phrase with specific methods to help determine how to display the phrase in the game.

The code chooses a random phrase and uses some logic to display each letter of the phrase as underscore character placeholders, _.

Each time the player guesses a letter, the program compares the letter the player has chosen with the random phrase. If the letter is in the phrase, the phrase object is updated so that it displays the chosen letters on the screen.

A player continues to select letters until they guess the phrase (and win), or make five incorrect guesses (and lose).

If the player completes the phrase before they run out of guesses, a winning screen appears. If the player guesses incorrectly five times, a losing screen appears.
