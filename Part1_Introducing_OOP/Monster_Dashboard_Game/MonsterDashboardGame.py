import random 

class Monster:
    def __init__(self, nRows, nCols, maxSpeed):
        self._nRows = nRows
        self._nCols = nCols 
        self._maxSpeed = maxSpeed
        
        self._currRow = random.randrange(self._nRows) # choose to stand on a random row on the dashboard
        self._currCol = random.randrange(self._nCols) # choose to stand on a random column on the dashboard
        
        self._currSpeedX = random.randrange(-self._maxSpeed, self._maxSpeed + 1) # pick randomly a speed value to move between columns
        self._currSpeedY = random.randrange(-self._maxSpeed, self._maxSpeed + 1) # pick randomly a speed value to move between rows
        
    def move(self):
        # self._currRow = random.randrange(self._currSpeedX, self._currRow) % self._nRows
        # self._currCol = random.randrange(self._currSpeedY, self._currCol) % self._nCols
        # if self._currRow and self._currCol:
        #     self._currRow = random.randrange(self._currSpeedX, self._currRow) % self._nRows
        #     self._currCol = random.randrange(self._currSpeedY, self._currCol) % self._nCols
        # else:
        #     while not self._currRow and self._currCol:
        #         self._currRow = random.randrange(self._currSpeedX, self._currRow) % self._nRows
        #         self._currCol = random.randrange(self._currSpeedY, self._currCol) % self._nCols
        new_row = (self._currRow + self._currSpeedX) % self._nRows
        new_col = (self._currCol + self._currSpeedY) % self._nCols
        
        if 0 <= new_row < self._nRows and 0 <= new_col < self._nCols:
            self._currRow = new_row
            self._currCol = new_col
        else:
            # Adjust positions to stay within grid boundaries
            self._currRow = random.randrange(self._nRows)
            self._currCol = random.randrange(self._nCols)
    
    def info(self):
        print("*** Info ***")
        print(">> Speed X: {}\n>> Speed Y : {}\n>> On current row : {}\n>> On current column : {}".format(self._currSpeedX, self._currSpeedY, self._currRow, self._currCol))        

    def getLocation(self):
        return [self._currRow, self._currCol]
    
    def receive_info(self):
        info = {
            "Speed-X": self._currSpeedX,
            "Speed-Y": self._currSpeedY,
            "Coordinate-X": self._currRow,
            "Coordinate-Y": self._currCol 
        }
        
        return info
    
# bench = []

# for i in range(4):
#     monster = Monster(100, 200, 4)
#     bench.append(monster)

# print("bench : {}".format(bench))
        
        