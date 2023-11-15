# Define a class
class car():
    def __init__(self, speed, color, nitrospeed, model):
        self.speed = speed
        self.color = color
        self.nitrospeed = nitrospeed
        self.model = model

# Function that avoid repetition of the sentence
    def carr(self):
        print("the speed of this car {} ,color {}, nitrosspeed {}, model{}".format(self.speed, self.color, self.nitrospeed,self.model))

# Nominate the information of car
car1 = car("380KM", "Black", "+100km","BMW")
car1.carr()
