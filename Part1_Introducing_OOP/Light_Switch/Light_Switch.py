class LightSwitch:
    def __init__(self):
        self.brightness_range = 0;
        self.isOn = False
    
    def turnOn(self):
        
        if self.isOn:
            print("The switch was actually turned on beforehand !")
        
        self.isOn = True
    
    def turnOff(self):
        
        if not self.isOn:
            print("The switch wasn't turned on beforehand !")
        
        self.isOn = False
    
    def is_on(self):
        return self.isOn

    def is_on_or_off(self):
        return "Off" if not self.is_on() else "On"

    
    def brighter(self):
        if not self.is_on():
            print("Please lay on the switch to turn that on in order to adjust the brightness !!!")
        
        if self.brightness_range < 10:
            self.brightness_range += 1
        else:
            print("The only allowed brightness range is 0 -> 10")
    
    def darker(self):
        if not self.is_on():
            print("Please lay on the switch to turn that on in order to adjust the brightness !!!")
        
        if self.brightness_range >= 1:
            self.brightness_range -= 1
        else:
            print("The only allowed brightness range is 0 -> 10")
    
    def manifest_current_brightness(self):
        return self.brightness_range


bulb = LightSwitch()

print("Is the bulb turn on or off ? : \n>> {}".format(bulb.is_on_or_off()))

bulb.turnOn()
print("Is the bulb turn on or off ? : \n>> {}".format(bulb.is_on_or_off()))

print("Current brightness of the bulb : {}".format(bulb.manifest_current_brightness()))

for i in range(4):
    bulb.brighter()
    
print("Current brightness of the bulb : {}".format(bulb.manifest_current_brightness()))
    
    