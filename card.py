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
