from random import randint

class Die():
    def __init__(self):
        self.sides = 6
    
    def roll_die(self):
        self.sides = randint(1,6)
        print(self.sides)

a_new_die = Die()
a_new_die.roll_die()
a_new_die.roll_die()
a_new_die.roll_die()
a_new_die.roll_die()
a_new_die.roll_die()
a_new_die.roll_die()
a_new_die.roll_die()
a_new_die.roll_die()
a_new_die.roll_die()
a_new_die.roll_die()