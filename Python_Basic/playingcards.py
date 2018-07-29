class Card(object):
    RANKS=["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS=["c","d","h","s"]

    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit

    def __str__(self):
        rep=self.rank+self.suit
        return  rep

class Hand(object):
    def __init__(self):
        self.cards=[]

    def __str__(self):
        rep=""
        if self.cards:
            for card in self.cards:
                rep+=str(card)+" "
        else:
            rep = "<empty>"
        return rep
    def clear(self):
        self.cards=[]

    def add(self,card):
        self.cards.append(card);

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

#Main
card1=Card(rank="1",suit="c")
print(card1)
my_hand = Hand()
print("\nPrinting my hand before I add any cards:")
#print(my_hand)
my_hand.add(card1)
print("My Hand:")
print(my_hand)
your_hand = Hand()
my_hand.give(card1, your_hand)
print("My Hand:")
print(my_hand)
print("Your Hand:")
print(your_hand)
my_hand.clear()
print("\nMy hand after clearing it:")
print(my_hand)