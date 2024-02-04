## Python Terminal Card Game, 
Individual Assignment, completed using pure Python 🐍
Grade: HD

This document contains:
- Introduction
- [Game Rules / Winning Conditions](#game-rules-winning-conditions)
- [App Installation and Launch Instructions](#app-installation-and-launch-instructions)

#### Introduction
- This is a Python program that enables a user (player) to play a Card Game against a computer (robot). The program must have a text interface. 
- The program will be evaluated based on its ease of use and clarity, including the provision of clear information and error messages for the player.
- The objective of the Card Game is to allow a player and a robot to repeatedly draw cards from a deck. Victory is attained when the player's card combination conforms to the rules and surpasses that of the robot's.
- The menu includess the following six options: Start Game, Pick a Card, Shuffle Deck, Show My Cards, Check Win/Lose, and Exit
- Every user can pick a maximum of 6 cards. Once the number of cards reaches 6, the program should display the final result and automatically restart the game.


#### Game Rules / Winning Conditions
To win, the player must meet one of the rules in the following order of priority: Rule 1 > Rule 2 > Rule 3 > Rule 4. The rules are as follows:

1. The player holds the same value card for all the defined suits.
For example, if the suits are ["♥", "♦", "♣", "♠"], the player should hold a set of cards that contains the following cards: ['A of ♥', 'A of ♦', 'A of ♣', 'A of ♠']. If the player's set of cards does not meet this requirement, the comparison proceeds to Rule 2. If the robot meets this requirement but the player does not, then the robot wins.
2. The player has the same values for at least the total defined suits minus one.
For example, if the suits are ["♥", "♦", "♣", "♠"], the player should hold a set of cards that contains at least three suits with the same values, such as ['A of ♥', 'A of ♦', 'A of ♣']. If the player's set of cards does not meet this requirement, then check Rule 3. If the robot meets this requirement but the player does not, then the robot wins.
3. The player holds more cards from the suit in position 2 than the robot. Note: if the suits=["♥", "♦", "♣", "♠"], the second suit is "♦".
For example, if the player holds cards =['A of ♥', '2 of ♦', '3 of ♣', '4 of ♦'] and the robot holds cards = ['2 of ♥', '3 of ♦', '4 of ♣', '5 of ♠'], the player wins as they have two “♦” cards and the robot only has one. If the player's set of cards doesn’t meet the above requirement, then check Rule 4. If the robot meets this requirement but the player does not, then the robot wins.
4. The player holds a higher average of the card’s value than robot.
For example, if the player holds cards =['10 of ♥', '2 of ♦', '3 of ♣', '4 of ♦'] and the robot holds cards = ['2 of ♥', '3 of ♦', '4 of ♣', '5 of ♠'], the player wins as the average number of cards value (i.e., (10+2+3+4) / 4 = 4.75) is higher than the robot’s average number of cards value (i.e., (2+3+4+5)/4 = 3.5). If the robot meets this requirement but the player does not, then the robot wins.

If the player's cards do not meet any of the conditions specified in rules 1 to 4, the player loses. If the robot's cards is empty and player’s card is not empty, the player win.


## App Installation and Launch Instructions

If you don't already have an IDE, download Visual Studio Code or similar
- Mac:  https://code.visualstudio.com/docs/setup/mac
- Windows:  https://code.visualstudio.com/docs/setup/windows
- Linux:  https://code.visualstudio.com/docs/setup/linux

If you don't already have Python installed, download it to your IDE:
- Install to VSCode:  https://code.visualstudio.com/docs/languages/python
- OR
- Download Python:  https://www.python.org/downloads/

Clone repository to your IDE:
- Clone repository instructions:  https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
- clone url:  https://github.com/ejneyland/e-commerce_assignment.git

Launch the app:
- from the main directory
- enter ```python card_game.py``` in the terminal
