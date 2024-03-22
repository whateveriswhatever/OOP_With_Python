class DashBoard:
    def __init__(self):
        self._nRows = 100
        self._nCols = 200
        self._dashboard = []
        
    def initialize(self):
        # grid 
        for i in range(self._nRows):
            row = []
            
            for j in range(self._nCols):
                row.append(0)
            
            self._dashboard.append(row)
    
    def manifest(self):
        # print("Dashboard : {}".format(self._dashboard))
        print("** Dashboard **")
        for row in self._dashboard:
            print(row)
        
    def occupy(self, botLocationX, botLocationY):
        
        
        if self._dashboard[botLocationX][botLocationY] == 0:
            self._dashboard[botLocationX][botLocationY] = 1
        else:
            print("The location {} - {} has been occupied !!!".format(botLocationX, botLocationY))
        
        
    def checkLengthOfTheDashboard(self):
        print(len(self._dashboard))
    
    def countTotalOccupiedPosition(self):
        count = 0
        
        for row in self._dashboard:
            for col in range(len(row)):
                if row[col] == 1:
                    count += 1
        
        print("Total occupied position on the dashboard : {}".format(count))
        

# dashboard = DashBoard()

# dashboard.initialize()

# dashboard.manifest()

# dashboard.checkLengthOfTheDashboard()

# monster = {
#     "locationX": 2,
#     "locationY": 7
# }

# dashboard.occupy(monster)

# dashboard.manifest()
            