import card


class Player:
    handNames = ['High', 'Pair', 'Two Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind',
                 'Straight Flush', 'Royal Flush']

    # override object methods
    def __init__(self):
        self.cards = []

    def __str__(self):
        middle = ", ".join([str(card_i) for card_i in self.cards])
        return "[" + middle + "]"

    # comparison operators
    def __eq__(self, h2):
        val1 = self.calc_value()
        val2 = h2.calc_value()

        # if you don't check the first value up front
        # the lists could be different length
        if val1[0] != val2[0]:
            return False

        # if the first element of the value is the same
        # the two lists should have the same length
        elif len(val1) > 1:
            for i in range(1, len(val1)):
                if val1[i] != val2[i]:
                    return False

        # if it reaches the end, the two are equal
        return True

    def __gt__(self, h2):
        val1 = self.calc_value()
        val2 = h2.calc_value()
        # if the first element of the value is the same
        # the two lists should have the same length
        if val1[0] != val2[0]:
            return val1[0] > val2[0]
        elif len(val1) > 1:
            for i in range(1, len(val1)):
                if val1[i] != val2[i]:
                    return val1[i] > val2[i]
        # if it reaches the end, the two are equal
        return False

    def __lt__(self, h2):
        val1 = self.calc_value()
        val2 = h2.calc_value()
        # if the first element of the value is the same
        # the two lists should have the same length
        if val1[0] != val2[0]:
            return val1[0] < val2[0]
        elif len(val1) > 1:
            for i in range(1, len(val1)):
                if val1[i] != val2[i]:
                    return val1[i] < val2[i]
        # if it reaches the end, the two are equal
        return False

    def size(self):
        return len(self.cards)

    def sort(self):
        self.cards.sort()

    def draw(self, deck, n):
        for i in range(0, n):
            self.cards.append(deck.draw())
        self.sort()

    # takes an index as input
    def discard(self, rem_card):
        return self.cards.pop(rem_card)

    def get_type(self):
        return self.handNames[self.calc_value()[0]]

    # return a tuple of cards that have at least one duplicate in the hand
    # meant to be used to prevent computers from discarding pairs
    def get_matches(self):
        temp = self.calc_value()

        # first check the case where there is only one pair
        if temp[0] == 1 or temp[0] == 3 or temp[0] == 7:
            return temp[1]
        # next check the case where there are two pairs
        elif temp[0] == 2 or temp[0] == 6:
            return temp[1], temp[2]
        else:
            return None

    # returns the tiebreaker values
    # this is mostly for debug
    def ties(self):
        temp = self.calc_value()
        if len(temp) <= 1:
            return "No ties."

        values = ""
        for i in range(1, len(temp)):
            values += card.Card.rankNames[temp[i]]
            values += " "
        return values

    def calc_value(self):
        # check for matches
        m1 = -1
        m2 = -1
        for i in range(0, self.size() - 1):
            if self.cards[i].rank == m1 or self.cards[i].rank == m2:
                continue
            if self.cards[i].rank == self.cards[i + 1].rank:
                if m1 == -1:
                    m1 = self.cards[i].rank
                else:
                    m2 = self.cards[i].rank
        # now check results of match search
        if m1 == -1:
            return self.calc_no_match()
        else:
            if m2 == -1:
                return self.calc_1pair(m1)
            else:
                return self.calc_2pair(m1, m2)

    def calc_1pair(self, m1):
        count = 0

        # count number of matched cards
        for card_i in self.cards:
            if card_i.rank == m1:
                count += 1

        # return index based on number of matched
        temp = []
        if count == 2:
            temp.append(1)
        elif count == 3:
            temp.append(3)
        else:
            temp.append(7)

        # add the pair/triple/quad as the first tiebreaker
        temp.append(m1)

        # then compare all other single cards
        for i in range(4, -1, -1):
            if self.cards[i].rank != m1:
                temp.append(self.cards[i].rank)
        return tuple(temp)

    def calc_2pair(self, m1, m2):
        count1 = 0
        count2 = 0

        # loop through and find number of each
        for card_i in self.cards:
            if card_i.rank == m1:
                count1 += 1
            elif card_i.rank == m2:
                count2 += 1

        # return index based on number of matched
        if count1 == 2 and count2 == 2:
            # for ties, first compare the pairs, then check the singleton
            if m1 > m2:
                temp = [2, m1, m2]
            else:
                temp = [2, m2, m1]

            # add the singleton
            for i in range(0, 5):
                if self.cards[i].rank != m1 and self.cards[i].rank != m2:
                    temp.append(self.cards[i].rank)
                    break
            return tuple(temp)

        elif (count1 == 3 and count2 == 2) or (count1 == 2 and count2 == 3):
            # for full house ties, check the triple, then the pair
            if m1 > m2:
                return 6, m1, m2
            else:
                return 6, m2, m1
        else:
            print("SOMETHING WENT WRONG IN 2PAIR")
            return 0

    def calc_no_match(self):
        straight = self.check_straight()
        flush = self.check_flush()
        # if straight, but not flush, then straight
        if straight and not flush:
            # tie breaker is highest card
            return 4, self.cards[4].rank

        # if straight and flush, straight flush, but check for royal
        elif straight and flush:
            if self.cards[0] == 8:
                return 9
            else:
                return 8, self.cards[4].rank

        # treating flush and high card the same because they compare the same
        else:
            # set type based on whether it is a flush
            if flush:
                temp = [5]
            else:
                temp = [0]

            # compare highest cards for ties
            for i in range(4, -1, -1):
                temp.append(self.cards[i].rank)
            return tuple(temp)

    # returns true if the cards are a straight and false otherwise
    def check_straight(self):
        # loops through and checks whether each index is one higher than the one before it
        for i in range(1, self.size()):
            if self.cards[i].rank - self.cards[i - 1].rank != 1:
                return False
        return True

    # returns true if cards are all same suit and false otherwise
    def check_flush(self):
        # loop through and check for the same suit
        for i in range(1, self.size()):
            if self.cards[i].suit != self.cards[i - 1].suit:
                return False
        return True
