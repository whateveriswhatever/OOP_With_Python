from MonsterDashboardGame import Monster 
# from Dashboard import DashBoard
from Dashboard import DashBoard

dashboard = DashBoard()

class Controller:
    def __init__(self, username):
        self._username = username
        self._dashboard = DashBoard()
        self._botDictionary = {}
        self._botBench = []
        
    def start(self):
        self._dashboard.initialize()
        
        # locating those created bots on the dashboard
        for bot in self._botBench:
            location = bot.getLocation()
            self._dashboard.occupy(location[0], location[1])
        
        print("Setup process...\nDone !")
        self._dashboard.manifest()
        
    def create_bot(self, nMonsters):
        for i in range(nMonsters):
            monster = Monster(100, 200, 4)
            self._botBench.append(monster)
            info = monster.receive_info()
            botName = f"Monster {i}"
            self._botDictionary[botName] = info
    
    def show_all_available_bots(self):
        print("All available bots on the dashboard : {}".format(self._botBench))    
    
    def move_bots(self):
        for bot in self._botBench:
            bot.move()
    
    def display_the_dashboard(self):
        self._dashboard.manifest()

controller = Controller("Duy")

controller.create_bot(4)

controller.start()

controller.show_all_available_bots()

controller.move_bots()

controller.display_the_dashboard()