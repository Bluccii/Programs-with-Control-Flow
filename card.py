# Import all necessary modules for the code
import stdio
import stdrandom

# Setting variable to a random number to simulate card ranks
rank = stdrandom.uniformInt(2, 15)
# Creating a string variable for the random rank
rankStr = str(rank)

# if statements used to determine specific card rank names
if rank == 11:
    rankStr = "Jack"
elif rank == 12:
    rankStr = "Queen"
elif rank == 13:
    rankStr = "King"
elif rank == 14:
    rankStr = "Ace"

# Setting the card's suit to a random suit
suit = stdrandom.uniformInt(1, 5)
# Creating a string variable for the random suit
suitStr = None

# Using if statements to determine what rank the card is based on the random integer
if suit == 1:
    suitStr = "Diamonds"
elif suit == 2:
    suitStr = "Clubs"
elif suit == 3:
    suitStr = "Hearts"
elif suit == 4:
    suitStr = "Spades"

# Displaying a statement describing what random card was generated to output
stdio.writeln(f"{rankStr} of {suitStr}")