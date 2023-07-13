# Higher or Lower game 
# card number range 1 to 40 

import random 

NUMBERS_TUPLE = (range(1, 41))
NCARDS = 10

print("Welcome to higher or lower game. You have to choose whether the next number card is higher or lower than the current.")
print("Getting it right earns you 15 points, get it wrong and 10 points will be deducted.")
print("You have 50 points to start with.")
print("Get to 100 and above and you win. Drop to 0 and below and you lose.")
print("You have a maximum of 10 tries.")

score = 50

# returns a card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

# returns shuffled copy of deck 
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

startingDeckList = []
# get list of dict {'value':value}, so when u pop, u pop one of the {'value':value}
for value in NUMBERS_TUPLE:
    cardDict = {'value':value}
    startingDeckList.append(cardDict)

while True:
    # ----------- get starting card ----------------
    # shuffled copy of the deck
    gameDeckList = shuffle(startingDeckList)
    # return a card 
    currentCardDict = getCard(gameDeckList)
    # get the value of the card
    currentCardValue = currentCardDict['value']
    print("Starting card is:", currentCardValue)
    print("")
    # ------------------------------------------------
    for card in range(0, NCARDS):
        ans = input("Will the next card be higher or lower? (enter h or l):")
        ans = ans.casefold()
        nextCardDict = getCard(gameDeckList)
        nextCardValue = nextCardDict['value']
        print("Next card is:", nextCardValue)

        if ans == 'h':
            if nextCardValue > currentCardValue:
                print("You got it right!")
                score += 15
            else:
                print("Wrong")
                score -= 10
        elif ans == 'l':
            if nextCardValue < currentCardValue:
                print("You got it right!")
                score += 15
            else:
                print("Wrong")
                score -= 10
        else:
            print("Invalid")

        print("Your score is:", score)
        print("")

        currentCardValue = nextCardValue
        
        # win or lost or no more tries left 
        if score >= 100:
            print("You won")
            break
        if score <= 0:
            print("You lost")
            break

    # if press q, the while loop breaks and game ends
    # if press ENTER, the while loop will go for a second loop
    print("No more tries\n")
    again = input("Press ENTER to play again, press 'q' to quit")
    if again == 'q':
        break
    else:
        print("Your score is restarted to 50")
        score = 50

print("Ok end of game")