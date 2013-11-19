import player
import deck


d = deck.Deck()
print d
print d.size()
p1 = player.Player()
p1.draw(d, 5)
p2 = player.Player()
p2.draw(d, 5)
print d
print d.size()
print ""
print "Player 1 hand:", p1
print p1.getType(), p1.ties()
print ""
print "Player 2 hand:", p2
print p2.getType(), p2.ties()

# check who won
print ""
if p1 > p2:
	print "Player 1 wins"
elif p1 < p2:
	print "Player 2 wins"
else:
	print "It's a tie"