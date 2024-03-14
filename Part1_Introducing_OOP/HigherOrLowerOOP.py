import random

class HigherOrLower:
    def __init__(self, NCARDS):
        self.SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
        self.RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
        self.NCARDS = NCARDS
        self.total_score = 50 
    
    # Pass in a deck and this function returns a random card from the deck
    def retrieveCard(self, storage):
        returnedCard = storage.pop()
        return returnedCard
    
    # Pass in a deck and this function returns a shuffled copy of the deck 
    # In every single time, when a card has been popped out from the storage card, we will create a new storage with a new order organization
    def shuffle(self, storage):
        # make a copy of the starting deck
        copiedStorage = storage.copy()
        
        random.shuffle(copiedStorage)
        return copiedStorage
    
    def prepareStartingDeckList(self):
        startingDeckList = []
        
        for suit in self.SUIT_TUPLE:
            for thisVal, rank in enumerate(self.RANK_TUPLE):
                card = {"rank": rank, "suit": suit, "value": thisVal + 1}
                startingDeckList.append(card)

        print("Starting deck list cards : {}".format(startingDeckList))
        return startingDeckList
    
    def greeting(self):
        print('Welcome to Higher or Lower.')
        print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
        print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
        print('You have 50 points to start.')
        print()
        
    def askForQuit(self):
        restart = input('To play again, press ENTER, or "q" to quit: ')
        
        if restart == "q":
            return True
        else:
            return False
        
    def retrieveCurrentCard(self, available_deck_list):
        current_card = self.retrieveCard(available_deck_list)
        
        return {
            "current_card_rank": current_card["rank"],
            "current_card_value": current_card["value"],
            "current_card_suit": current_card["value"]
        }
        
    def retrieveNextCard(self, available_deck_list):
        next_card = self.retrieveCard(available_deck_list)
        
        return {
            "next_card_rank": next_card["rank"],
            "next_card_value": next_card["value"],
            "next_card_suit": next_card["value"]
        }
    
    def announceScore(self):
        print("Your score : {}".format(self.total_score))
        print()
    
    def play(self):
        self.greeting()
        
        while True:
            print()
            
            availDeckList = self.shuffle(self.prepareStartingDeckList())
            
            current_card = self.retrieveCurrentCard(availDeckList)
            print("Starting card information: \n>> Rank : {}\n>> Value: {}\n>>Suit: {}".format(current_card["current_card_rank"], current_card["current_card_value"], current_card["current_card_suit"]))
            
            for cardNumber in range(0, self.NCARDS):
                # play one this many cards
                answer = input("'Will the next card be higher or lower than the ' + currentCardRank + ' of ' + currentCardSuit + '? (enter h or l): ")
        
                answer = answer.casefold() # force lowercase || lower() instead ?
                
                next_card = self.retrieveNextCard(availDeckList)
                print("Starting card information: \n>> Rank : {}\n>> Value: {}\n>>Suit: {}".format(next_card["next_card_rank"], next_card["next_card_value"], next_card["next_card_suit"]))
                
                if answer == "h":
                    if next_card["next_card_value"] > current_card["current_card_value"]:
                        print("You got it !!! \n--> + 20PTS")
                        self.total_score += 20
                    else:
                        print("Wrong !!!\n--> - 15PTS")
                        self.total_score -= 15
                elif answer == "l":
                    if next_card["next_card_value"] < current_card["current_card_value"]:
                        print("You got it !!! \n--> + 20PTS")
                        self.total_score += 20
                    else:
                        print("Wrong !!!\n--> - 15PTS")
                        self.total_score -= 15
                else:
                    print("Invalid answer !!!!")
                    break
                self.announceScore()
                current_card["current_card_rank"] = next_card["next_card_rank"]
                current_card["current_card_value"] = next_card["next_card_value"]
                
            wantToRestart = self.askForQuit()
            
            if wantToRestart:
                break
        
        print("Bye")

game = HigherOrLower(8)

game.play()
                
                
                
        
        
        