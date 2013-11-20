import player
import deck
import random

NUM_PLAYERS = 4

class Game:
	def __init__(self):
		self.deck = deck.Deck()
		# initialize players
		self.players = []
		for i in range(0, NUM_PLAYERS):
			self.players.append(player.Player())
			self.players[i].draw(self.deck, 5)

		self.first = 0
	
	# displays each player's hand and value
	# mostly for debug
	def printGameState(self):
		print "Number of players:",NUM_PLAYERS
		for i in range(0, NUM_PLAYERS):
			print "Player", i+1
			print self.players[i]
			print self.players[i].getType()
			print self.players[i].ties()
			print ""
	
	# for each turn
	def playHand(self, player):
		if player != 0:
			playComp(player)
		else:
			# take input from player for which cards to remove
			input = raw_input()
			toks = input.split(" ")
			# remove cards in hand
			for tok in toks:
				temp = self.players[player].cards[tok]
				self.deck.add(temp)
				self.players[player].cards[tok] = self.deck.draw()
			self.players[player].sort()

	# prints the winner
	# should change this to return the winner instead
	def findWinner(self):
		win = [0]
		ties = False
		
		# find who has the highest score or if there is a tie
		for i in range(1, NUM_PLAYERS):
			if self.players[i] > self.players[win[0]]:
				win = [i]
			elif self.players[i] == self.players[win[0]]:
				win.append(i)
		
		if len(win) > 1:
			temp = ", ".join(x+1 for x in win)
			print "Players", temp, "tied"
		else:
			print "Player", win[0]+1, "wins"