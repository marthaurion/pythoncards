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
	handNames = ['High', 'Pair', 'Two Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush']
	
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
		for i in range(0, n):
			self.cards.append(deck.draw())
		self.sort()
	
	# takes an index as input
	def discard(self, card):
		return self.cards.pop(card)

	def getType(self):
		return self.handNames[self.calcValue()]
		
	def calcValue(self):
		# check for matches
		m1 = -1
		m2 = -1
		for i in range(0, self.size()-1):
			if self.cards[i].rank == m1 or self.cards[i].rank == m2:
				continue
			if self.cards[i].rank == self.cards[i+1].rank:
				if m1 == -1:
					m1 = self.cards[i].rank
				else:
					m2 = self.cards[i].rank
		# now check results of match search
		if m1 == -1:
			return self.calcNoMatch()
		else:
			if m2 == -1:
				return self.calc1Pair(m1)
			else:
				return self.calc2Pair(m1, m2)
	
	def calc1Pair(self, m1):
		count = 0
		
		# count number of matched cards
		for card in self.cards:
			if card.rank == m1:
				count += 1
		
		# return index based on number of matched
		if count == 2:
			return 1
		elif count == 3:
			return 3
		else:
			return 7

	def calc2Pair(self, m1, m2):
		count1 = 0
		count2 = 0
		
		# loop through and find number of each
		for card in self.cards:
			if card.rank == m1:
				count1 += 1
			elif card.rank == m2:
				count2 += 1
		
		# return index based on number of matched
		if count1 == 2 and count2 == 2:
			return 2
		elif (count1 == 3 and count2 == 2) or (count1 == 2 and count2 == 3):
			return 6
		else:
			print "SOMETHING WENT WRONG IN 2PAIR"
			return 0
	
	def calcNoMatch(self):
		straight = self.checkStraight()
		flush = self.checkFlush()
		# if straight, but not flush, then straight
		if straight and not flush:
			return 4
		# if flush, but not straight, then flush
		elif not straight and flush:
			return 5
		# if straight and flush, straight flush, but check for royal
		elif straight and flush:
			if self.cards[0] == 8:
				return 9
			else:
				return 8
		
		# if neither straight or flush, it must be high card
		else:
			return 0

	# returns true if the cards are a straight and false otherwise
	def checkStraight(self):
		# loops through and checks whether each index is one higher than the one before it
		for i in range(1, self.size()):
			if self.cards[i].rank - self.cards[i-1].rank != 1:
				return False
		return True
			
	# returns true if cards are all same suit and false otherwise
	def checkFlush(self):
		# loop through and check for the same suit
		for i in range(1, self.size()):
			if self.cards[i].suit != self.cards[i-1].rank:
				return False
		return True


d = Deck()
print d
print d.size()
p1 = Player()
p1.draw(d, 5)
print d
print d.size()
print p1
print p1.getType()