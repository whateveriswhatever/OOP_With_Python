from MonsterDashboardGame import Monster 
from Dashboard import DashBoard

bench = []

dashboard = DashBoard()

dashboard.initialize()

for i in range(20):
    monster = Monster(100, 200, 4)
    bench.append(monster)

print("bench : {}".format(bench))

for i in range(len(bench)):
    print("Monster {}".format(i))
    bench[i].info()
    location = bench[i].getLocation()
    xCoordinate = location[0]
    yCoordinate = location[1]
    print("X : {} >><< Y : {}".format(xCoordinate, yCoordinate))
    dashboard.occupy(xCoordinate, yCoordinate)
        
dashboard.manifest()
dashboard.countTotalOccupiedPosition()

for i in range(len(bench)):
    bench[i].move()
    location = bench[i].getLocation()
    xCoordinate = location[0]
    yCoordinate = location[1]
    print("X : {} >><< Y : {}".format(xCoordinate, yCoordinate))
    dashboard.occupy(xCoordinate, yCoordinate)

dashboard.manifest()