import player
import deck
import random  # use this for computer

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
    def print_game_state(self):
        print "Number of players:", NUM_PLAYERS
        for i in range(0, NUM_PLAYERS):
            print "Player",str(i + 1)
            print self.players[i]
            print self.players[i].get_type()
            print self.players[i].ties()
            print ""

    # for each turn
    # player is the index of the player
    def play_hand(self, player_num):
        if player_num != 0:
            self.play_comp(player_num)
        else:
            self.player_turn()

    # assume the player is player 1
    def player_turn(self):
        # take input from player for which cards to remove
        toks = str(input("Cards to discard: ")).split(" ")  # remove cards in hand
        discards = 0
        for i in range(5):
            # check if the card is in the input
            if str(i) in toks:
                # discard and re-draw
                temp = self.players[0].discard(i-discards)
                self.deck.add(temp)
                discards += 1
        self.players[0].draw(self.deck, discards)

    # player is the index of the players
    def play_comp(self, player_num):
        discards = 0
        for i in range(5):
            if random.randrange(2) == 1:
                temp = self.players[player_num].discard(i-discards)
                self.deck.add(temp)
                discards += 1
        self.players[player_num].draw(self.deck, discards)

    # prints the winner
    # should change this to return the winner instead
    def find_winner(self):
        win = [0]

        # find who has the highest score or if there is a tie
        for i in range(1, NUM_PLAYERS):
            if self.players[i] > self.players[win[0]]:
                win = [i]
            elif self.players[i] == self.players[win[0]]:
                win.append(i)

        if len(win) > 1:
            temp = ", ".join(str(x+1) for x in win)
            print "Players", temp, " tied"
        else:
            print "Player", win[0] + 1, "wins"