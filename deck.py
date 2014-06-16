import random
import card


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(0, 4):
            for j in range(0, 13):
                self.cards.append(card.Card(j, i))
        random.shuffle(self.cards)

    def __str__(self):
        middle = ", ".join([str(card) for card in self.cards])
        return "[" + middle + "]"

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def add(self, card):
        self.cards.append(card)

    def size(self):
        return len(self.cards)