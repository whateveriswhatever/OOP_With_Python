import random

class HigherOrLower_Game:
    def __init__(self):
        self.storage = [random.randrange(1, 8, 2) for _ in range(8)]
        self.total_score = 0
        self.currIdx = 0
        self.outOfUsedIdx = []
        self.previousCard = []
    
    def printInit(self):
        print("**********************************************")
        print("self.storage : {}\nself.total_score : {}\nself.currIdx : {}\nself.outOfUsedIdx : {}".format(self.storage, self.total_score, self.currIdx, self.outOfUsedIdx))
        print("self.previousCard : {}".format(self.previousCard))
        print("********************************************** \n\n\n")
        
        
    def pop_a_Card(self):
        if len(self.storage) > 0:
            randomIdx = random.randrange(0, 8, 2)
            
            # in each time we retrieve a random index for popping out an element that is being stored at the index position
            # we will reserve that index inner the Hash Map <Dictionary>
            # in the next time, if the the random index we received from pop_a_Card() is reminiscent to the previous or any index of the element we
            # have been popped before, we will discard that and keep looking for a new index from the pop_a_Card()
            
            # should we discard the element that being reserved inner the self.storage at randomIdx index ?
            
            if randomIdx in self.outOfUsedIdx:
                return self.pop_a_Card()
            
            # randomIdx = random.randrange(0, 8, 2)
            self.currIdx = randomIdx
            returnedCard = self.storage.pop(randomIdx)
            self.outOfUsedIdx.append(randomIdx)
            print("outofUsedIdx : {}".format(self.outOfUsedIdx))
            return returnedCard
    
    def retrieveTheFirstCard(self):
        primaryCard = self.storage.pop(0)
        self.moveToNextIdx()
        return primaryCard
    
    def retrieveThePrevCard(self):
        return self.previousCard[-1]
    
    def moveToNextIdx(self):
        self.currIdx += 1

    def getTheNextCard(self):
        self.moveToNextIdx()
        return self.storage[self.currIdx]
    
    def guess(self):
        
        # there are 2 cards to be manipulated : Current Card and Next Card
        
        print("Let's guess !\nYour current scores : {}".format(self.trackCurrentScore()))
        currCard = None
        nextCard = None
        
        currTotalScore = self.trackCurrentScore()
        
        if currTotalScore == 0:
            currCard = self.retrieveTheFirstCard()
            nextCard = self.getTheNextCard()
            self.previousCard.append(currCard)
            print(">> The primary card : {}".format(currCard))
        
        currCard = self.pop_a_Card()
        self.previousCard.append(currCard)
        # parsedInScore = int(input("Your inital assignment : "))
        
        print("Chose 'lower' or 'higher' to guess to card we're going to manifest you\nIf the value of the card is correct corresponding to your guess, you will get 20 PTS !")
        print("Enjoy the game !")
        
        
        userGuess = input("'lower' or 'higher' : ")
        print("\n\n")
        # print("Current card : {} >><< Your assignment : {}".format(currCard, parsedInScore))
        
        if self.total_score > 0:
            if (currCard > nextCard) and (userGuess == "higher"):
                return True
            elif (currCard < nextCard) and (userGuess == "lower"):
                return True
            else:
                return False
        else:
            return False
        
    
    def mangeTotalScore(self, answ):
        if answ:
            self.total_score += 20
        else:
            self.total_score -= 15
    
    def trackCurrentScore(self):
        print("Current total scores : {}".format(self.total_score))
        return self.total_score


game = HigherOrLower_Game()

game.printInit()

# print(game.pop_a_Card())

game.guess()

winOrLost = game.guess()

game.mangeTotalScore(winOrLost)

game.trackCurrentScore() 