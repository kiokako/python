import random
class Pound:
    def __init__(self, rare=False):
        self.rare = rare
        if self.rare:
            self.value =  1.25
        else:
            self.value = 1.00
        
        self.value = 1.00
        self.colour = "gold"
        self.num = 1
        self.diameter = 22.5
        self.thickness = 3.15
        self.heads = True
        
    def rust(self):
        self.colour = "greenish"

    def clean(self):
        self.colour = "gold"

    def flip(self):
        options = [True,False]
        choice = random.choice(options)
        self.heads = choice
