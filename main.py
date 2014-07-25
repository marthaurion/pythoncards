import game

def main_game():
    g = game.Game()
    g.print_game_state()
    for i in range(4):
        g.play_hand(i)
    g.print_game_state()
    g.find_winner()
    if len(g.deck.cards) == len(set(g.deck.cards)):
        print "No duplicate cards in deck."
    print "[", ", ".join([str(card) for card in g.deck.cards]), "]"
    print(len(g.deck.cards))

main_game()