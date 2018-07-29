class Player(object):
    def blast(self,enemy):
        print("The player blasts an enemy.\n")
        enemy.die()
class Alien(object):
    def die(self):
        print("The alien gasps and says, 'Oh, this is it. This is the big one. \n","Yes, it's getting dark now. Tell my 1.6 million larvae that I loved them... \n","Good-bye, cruel universe.'")

#Main Method

print("\n\t\tDeath of an Alien\n")

alien1=Alien()
player1=Player()

player1.blast(alien1)
