class Television:
    def __init__(self, programs = []):
        self._storage = ["Series Harry Potter", "Perl", "Quy Cau", "Aquaman 2", "NBA TV", "Paul Georige's Podcast", "NBA 2K24 Contest", "Francis Ha", "Perfect Days"]
        if len(programs) < 8:
            print("Please assign your 8 favourite films, showcases, or podcasts to complete the setup process for your own TV, otherwise, your TV programs will be initialized by our own recommended programs.\nHowever, you can modify that in any time !!!")
            self._programs = self._storage
        else:
            self._programs = programs # requires user having to assign only 8 TV programs, shows, or podcasts that they want to add
    
        self._is_muted = False
        self._volumn = 12
        self._isOn = False
        self._program_index = 0
        self._volumn_history = []
            
        
        
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
        # self._is_muted = False if self._is_muted else True
        self._is_muted = not self._is_muted # toggling
    
    def is_muted(self):
        return self._is_muted
    
    def drain_downright_the_volumn(self):
        self._volumn = 0
    
    def custom_current_volumn_by_parameter(self, range):
        self._volumn = range
    
    def mute(self):
        currVolumn = self.get_current_volumn()
        self._volumn_history.append(currVolumn)
        self.drain_downright_the_volumn() if self.is_muted() else self.custom_current_volumn_by_parameter(currVolumn)
    
    def unmute(self):
        # if self.get_current_volumn() == 0 or self._is_muted:
        #     self._is_muted = False
        #     self.louder()
        self._is_muted = False
        # self.louder()
        self._volumn = self._volumn_history[-1]
    
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
        return keyboard
    
    
    def move_to_next_channel(self):
        if self._program_index < 9:
            self._program_index += 1
        else:
            self._program_index = 0
    
    def move_to_previous_channel(self):
        if self._program_index > 1:
            self._program_index -= 1
        else:
            self._program_index = 0
    
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
        # return self._programs[self._program_index]
        keyboard_controller = self.initalize_keyboard()
        return keyboard_controller[self._program_index]
    
    def perceive_info(self):
        currChannel = self.get_current_channel()
        currVolumn = self.get_current_volumn()
        print(">> Channel: {}\n>> Volumn: {}\n>> Muted: {}".format(currChannel, currVolumn, "Yes" if self._is_muted else "No"))
    
    def auto_setup(self):
        self.initalize_keyboard()
        print("Setup completely !")
        self.perceive_info()

# myTelevision = Television()
# myTelevision.initalize_keyboard()
# myTelevision.perceive_info()

# myTelevision.navigate_to_channel_from_keyboard(5)
# myTelevision.perceive_info()



# myTelevision.set_mute()
# myTelevision.mute()

# # myTelevision.set_mute()
# # myTelevision.mute()
# myTelevision.unmute()
# myTelevision.perceive_info()

# myTelevision.move_to_next_channel()
# myTelevision.perceive_info()
# # myTelevision.move_to_next_channel()

# print("Object scopes inner my television : {}".format(vars(myTelevision)))

