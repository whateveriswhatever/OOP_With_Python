import random

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8 

total_score = 50

# Pass in a deck and this function returns a random card from the deck

def getCard(storage):
    returnedCard = storage.pop()
    return returnedCard

# Pass in a deck and this function returns a shuffled copy of the deck 
# In every single time, when a card has been popped out from the storage card, we will create a new storage with a new order organization
def shuffle(storage):
    copiedStorage = storage.copy() # make a copy of the starting deck
    random.shuffle(copiedStorage)
    
    return copiedStorage

# Main code
print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {"rank": rank, "suit": suit, "value": thisValue + 1}
        startingDeckList.append(cardDict)

print("staringDectList : {}".format(startingDeckList))

while True:
    print()
    availDeckList = shuffle(startingDeckList)
    
    currentCardDict = getCard(availDeckList)
    currentCardRank = currentCardDict["rank"]
    currentCardVal = currentCardDict["value"]
    currentCardSuit = currentCardDict["suit"]
    
    print("Starting card information: \n>> Rank : {}\n>> Value: {}\n>>Suit: {}".format(currentCardRank, currentCardVal, currentCardSuit))
    print()

    for cardNumber in range(0, NCARDS):
        # play one this many cards
        answer = input("'Will the next card be higher or lower than the ' + currentCardRank + ' of ' + currentCardSuit + '? (enter h or l): ")
        
        answer = answer.casefold() # force lowercase || lower() instead ?
        
        nextCardDict = getCard(availDeckList)
        
        nextCardRank = nextCardDict["rank"]
        nextCardVal = nextCardDict["value"]
        nextCardSuit = nextCardDict["suit"]
        
        print("Next card information: \n>> Rank : {}\n>> Value: {}\n>>Suit: {}".format(nextCardRank, nextCardVal, nextCardSuit))

        if answer == "h":
            if nextCardVal > currentCardVal:
                print("You got it !!! \n--> + 20PTS")
                total_score += 20
            else:
                print("Wrong !!!\n--> - 15PTS")
                total_score -= 15
        elif answer == "l":
            if nextCardVal < currentCardVal:
                print("You got it !!! \n--> + 20PTS")
                total_score += 20
            else:
                print("Wrong !!!\n--> - 15PTS")
                total_score -= 15
        else:
            print("Invalid answer !!!")
            break
    
        print("Your score : {}".format(total_score))
        print()
        currentCardRank = nextCardRank
        currentCardVal = nextCardVal
        # no need to move to the next card's suit
    
    restart = input('To play again, press ENTER, or "q" to quit: ')
    if restart == "q":
        break

print("Bye")
    