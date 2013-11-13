import random

class Card:
	suitNames = ['C', 'D', 'H', 'S']
	rankNames = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
	
	def __str__(self):
		return Card.rankNames[self.rank] + Card.suitNames[self.suit]
	
	def __gt__(self, c2):
		if self.rank == c2.rank:
			return self.suit > c2.suit
		else:
			return self.rank > c2.rank
	
	def __lt__(self, c2):
		if self.rank == c2.rank:
			return self.suit < c2.suit
		else:
			return self.rank < c2.rank
	
	def __eq__(self, c2):
		return self.rank == c2.rank and self.suit == c2.suit

class Deck:
	def __init__(self):
		self.cards = []
		for i in range(0, 4):
			for j in range(0, 13):
				self.cards.append(Card(j, i))
		random.shuffle(self.cards)
	
	def __str__(self):
		middle = ", ".join([str(card) for card in self.cards])
		return "[" + middle + "]"

	def shuffle(self):
		random.shuffe(self.cards)

	def draw(self):
		return self.cards.pop(0)
	
	def add(self, card):
		self.cards.append(card)
		
	def size(self):
		return len(self.cards)

class Player:
	def __init__(self):
		self.cards = []
	
	def __str__(self):
		middle = ", ".join([str(card) for card in self.cards])
		return "[" + middle + "]"
	
	def size(self):
		return len(self.cards)
	
	def sort(self):
		self.cards.sort()
	
	def draw(self, deck, n):
		for i in range(0,n):
			self.cards.append(deck.draw())
		self.sort()
	
	# takes an index as input
	def discard(self, card):
		return self.cards.pop(card)

	def calcValue(self):
		pass

d = Deck()
print d
print d.size()
p1 = Player()
p1.draw(d, 5)
print d
print d.size()
print p1