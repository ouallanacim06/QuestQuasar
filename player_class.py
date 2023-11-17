class player:
    def __init__(self, name,gender):
        self.name = name
        self.xp = 0
        self.gender = gender
        
    def moving(self):
        print("moving")