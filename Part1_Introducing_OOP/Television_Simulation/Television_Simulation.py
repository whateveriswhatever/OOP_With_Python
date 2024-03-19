class Television:
    def __init__(self, programs = []):
        self._storage = ["Series Harry Potter", "Perl", "Quy Cau", "Aquaman 2", "NBA TV", "Paul Georige's Podcast", "NBA 2K24 Contest", "Francis Ha", "Perfect Days"]
        if len(programs) < 8:
            print("Please assign your 8 favourite films, showcases, or podcasts to complete the setup process for your own TV, otherwise, your TV programs will be initialized by our own recommended programs.\nHowever, you can modify that in any time !!!")
            self._programs = self._storage
        else:
            self._programs = programs # requires user having to assign only 8 TV programs, shows, or podcasts that they want to add
    
        self._is_muted = False
        self._volumn = 0
        self._isOn = False
        self._program_index = 0
    
    def switch_on(self):
        if self._isOn:
            print("The TV has actually been turned on before !")
        
        self._isOn = True
    
    def switch_off(self):
        if self._isOn:
            print("The TV hasn't been turned on yet !")
        
        self._isOn = False
    
    def out_of_range_for_volumn(self):
        return True if (self._volumn > 80 or self._volumn < 0) else False
    
    def louder(self):
        
        if self.out_of_range_for_volumn():
            print("Can't increase the volumn owing to the allowed range for volumn is only from 0 -> 80 !!!")
        
        self._volumn += 1
    
    def quieter(self):
        
        if self.out_of_range_for_volumn():
            print("Can't knock the volumn down owing to the allowed range for volumn is only from 0 -> 80 !!!")
        
        self._volumn -= 1
    
    # when customer unmute their TV, navigate them to previous volumn before they pressed the mute button
    def set_mute(self):
        # if self._is_muted:
        #     self._is_muted = False
        # else:
        #     self._is_muted = True
        self._is_muted = False if self._is_muted else True
    
    def drain_downright_the_volumn(self):
        self._volumn = 0
    
    def custom_current_volumn_by_parameter(self, range):
        self._volumn = range
    
    def mute(self):
        currVolumn = self.get_current_volumn()
        self.drain_downright_the_volumn() if self.set_mute() else self.custom_current_volumn_by_parameter(currVolumn)
    
    def get_current_volumn(self):
        return self._volumn
    
    def initalize_keyboard(self):
        keyboard = {}
        
        # the button 0 will be set to none of these provided TV programs by default 
        keyboard[0] = "Unknown"
        
        # using dictionary to assign each TV programs exquivalently to each integer button on the TV keyboard
        queue = [_ for _ in self._programs]
        currentNum = 1
        while len(queue) > 0:
            currProgram = queue.pop(0)
            keyboard[currentNum] = currProgram
            currentNum += 1
        
        print("Keyboard's info: {}".format(keyboard))
    
    
    def move_to_next_channel(self):
        self._program_index += 1
    
    def move_to_previous_channel(self):
        self._program_index -= 1
    
    def channel_navigator(self, option):
        if option == "Next":
            self.move_to_next_channel()
        elif option == "Previous":
            self.move_to_previous_channel()
        else:
            print("Move to next or jump back to the previous TV programs only !!!")
    
    def navigate_to_channel_from_keyboard(self, programIdx):
        if type(int(programIdx)) != int:
            print("Please press or type down the number from 0 -> 9 only !!!")
        
        self._program_index = programIdx
    
    def get_current_channel(self):
        return self._programs[self._program_index]
    
    def perceive_info(self):
        currChannel = self.get_current_channel()
        currVolumn = self.get_current_volumn()
        print(">> Channel: {}\n>> Volumn: {}\n>> Muted: {}".format(currChannel, currVolumn, "Yes" if self._is_muted else "No"))
            

myTelevision = Television()
myTelevision.initalize_keyboard()
myTelevision.perceive_info()


    