import player
import deck


d = deck.Deck()
print d
print d.size()
p1 = player.Player()
p1.draw(d, 5)
print d
print d.size()
print p1
print p1.getType(), p1.ties()