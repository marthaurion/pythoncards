import random

suits = ['C', 'D', 'H', 'S']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class Card:
	def __init__(self, value, suit):
		self.rank = ranks[value]
		self.value = value
		self.suit = suit
	
	def __str__(self):
		return self.rank + self.suit

class Deck:
	def __init__(self):
		self.cards = []
		for suit in suits:
			for rank in ranks:
				self.cards.append(Card(rank, suit))
		random.shuffle(self.cards)
	
	def cprint(self):
		for card in self.cards:
			print card.rank+card.suit

	def shuffle(self):
		random.shuffe(self.cards)

	def draw(self):
		return self.cards.pop(0)
	
	def add(self, card):
		self.cards.append(card)

	def size(self):
		return len(self.cards)

		

d = Deck()
d.cprint()
print d.size()
print d.draw()
print d.size()