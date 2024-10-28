#  File: Poker.py

#  Description: Poker is a game with 10 hands. Each hand has a different weight. The player with the highest hand wins.

#  Student's Name: Vaishnavi Sathiyamoorthy

#  Student's UT EID: vs25229

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 09/17/2022

#  Date Last Modified: 09/18/2022

import sys, random

# The ranks and suits are created
class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  # constructor
  def __init__ (self, num_players = 2, num_cards = 5):
    self.num_players = num_players
    self.deck = Deck()
    self.deck.shuffle()
    self.players_hands = []
    self.numCards_in_Hand = num_cards

    # deal the cards to the players
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.players_hands.append (hand)

  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal(self, hand):
    # Determines if the suits for all the cards are the same
    same_suit = True
    for i in range(len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    # Determines if the ranks are A, K, Q, and J
    rank_order = True
    for i in range(len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0, ''
    # Since this is the best hand, the calculation gives 10 to h.
    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Royal Flush'

  def is_straight_flush(self, hand):
    # This determines if all the suits for the card are the same
    same_suit = True
    for i in range(len(hand) - 1):
      if hand[i].suit != hand[i + 1].suit:
        same_suit = False
        break
    if same_suit == False:
      return 0, ''

    # This determines if the cards are in numerical order by rank for all 5 cards.
    rank_order = True
    for i in range(len(hand) - 1):
      if hand[i].rank > 10:
        rank_order = False
        break
      if abs(hand[i].rank - hand[i + 1].rank) != 1:
        rank_order = False
        break
    if rank_order == False:
      return 0, ''

    # Since this is the second best hand, h is 9
    points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, "Straight Flush"

  def is_four_kind(self, hand):
    # This determines if 4 of the ranks are the same. There are only 2 possible options for the order of the cards for the rank to be the same.
    four = False
    if (hand[0].rank == hand[1].rank and hand[1].rank == hand[2].rank and hand[2].rank == hand[3].rank):
      four = True
    elif (hand[1].rank == hand[2].rank and hand[2].rank == hand[3].rank and hand[3].rank == hand[4].rank):
      four = True
    else:
      return 0, ''

    # Since this is the third best hand, h is awarded 8.
    points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, "Four of a Kind"

  def is_full_house(self, hand):
    # There are two different options for a full house. first 3 and second 2 are same or first 2 and second 3 are the same.
    same_rank = False
    if hand[0].rank == hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank:
      same_rank = True
    elif hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank == hand[4].rank:
      same_rank = True
    if same_rank == False:
      return 0, ''

    # Since this is the 4th best hand, h is 7.
    points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, "Full House"

  def is_flush(self, hand):
    # This checks if all the suits of the cards are the same
    same_suit = True
    for i in range(len(hand) - 1):
      if hand[i].suit != hand[i + 1].suit:
        same_suit = False
        break
    if same_suit == False:
      return 0, ''

    # Since this is the 5th best hand, h is 6.
    points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, "Flush"

  def is_straight(self, hand):
    # This checks if the hand is in numerical order. The suit does not matter.
    rank_order = True
    for i in range(len(hand) - 1):
      if abs(hand[i].rank - hand[i + 1].rank) != 1:
        rank_order = False
        break
    if rank_order == False:
      return 0, ''

    # Since this is the 6th best hand, h is 5.
    points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, "Straight"

  def is_three_kind(self, hand):
    # This checks if any 3 of the ranks of the cards are the same. There are only 3 possible combinations.
    three = False
    if (hand[0].rank == hand[1].rank == hand[2].rank):
      three = True
    elif (hand[1].rank == hand[2].rank == hand[3].rank):
      three = True
    elif (hand[2].rank == hand[3].rank == hand[4].rank):
      three = True
    else:
      return 0, ''

    # Since this is the 7th best hand, h is awarded 4.
    points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    return points, "Three of a Kind"

  def is_two_pair(self, hand):
    # There are 3 possible combinations for there to be two pairs.
    two_pair = False
    if hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank:
      two_pair = True
    elif hand[0].rank == hand[1].rank and hand[3].rank == hand[4].rank:
      two_pair = True
    elif hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank:
      two_pair = True
    if two_pair == False:
      return 0, ''
    else:
      # Since this is the 8th best hand, h = 3
      points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)
      return points, "Two Pair"

    # determine if a hand is one pair
    # takes as argument a list of 5 Card objects
    # returns the number of points for that hand

  #fix point calculations
  def is_one_pair(self, hand):
    one_pair = False
    index = []
    # This loop determines whether there is a pair and what the indexes of the pair are
    for i in range(len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True
        index.append(i)
        index.append(i+1)
        break
    if (not one_pair):
      return 0, ''

    other_cards = []
    # This loop determines the indexes of the other cards that are not in the pair
    for i in range(len(hand)):
      match = False
      if hand[i].rank == hand[index[0]].rank:
        match = True
      if match == False:
        other_cards.append(i)

    all_rank = []
    # This loop determines the ranks of all the cards
    for i in range(len(hand)):
      all_rank.append(hand[i].rank)
    # The ranks of just the other cards are determined.
    other_cards_rank = [hand[other_cards[0]].rank, hand[other_cards[1]].rank, hand[other_cards[2]].rank]
    # The max rank of the other cards is determined
    third_rank = max(other_cards_rank)
    # The index of this rank is determined from all ranks
    third_index = all_rank.index(third_rank)
    # This rank is removed from other card ranks so the next highest rank can be found.
    other_cards_rank.remove(third_rank)
    # The max rank of the remaining other cards is determined
    second_rank = max(other_cards_rank)
    # The index of this rank is determined from all ranks
    second_index = all_rank.index(second_rank)
    # This rank is removed from other card ranks so the next highest rank can be found.
    other_cards_rank.remove(second_rank)
    # The remaining card has the lowest rank. The index of this rank is determined from all ranks
    first_index = all_rank.index(other_cards_rank[0])

    # Since this is the 9th best hand, h is 2
    points = 2 * 15 ** 5 + (hand[index[0]].rank) * 15 ** 4 + (hand[index[1]].rank) * 15 ** 3
    points = points + (hand[third_index].rank) * 15 ** 2 + (hand[second_index].rank) * 15 ** 1
    points = points + (hand[first_index].rank)

    return points, 'One Pair'

  def is_high_card(self, hand):
    # If none of the other hands work, then the points are determined from highest to lowest rank
    points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    return points, 'High Card'


  # simulate the play of poker
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players_hands)):
      sorted_hand = sorted (self.players_hands[i], reverse = True)
      self.players_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str (card) + ' '
      print ('Player ' + str(i + 1) + ' : ' + hand_str)
    print()

    # determine the type of each hand and print
    hand_type = []
    hand_points = []
    # This for loop goes through each player's hand and determines what hand they have
    for i in range(self.num_players):
      not_zero = False
      # This while loop determines which of the hands each player has. Each of the previously written functions are called.
      while not_zero == False:
        a, b = self.is_royal(self.players_hands[i])
        if a != 0:
          hand_type.append(b)
          hand_points.append(a)
          not_zero = True
          break
        a, b = self.is_straight_flush(self.players_hands[i])
        if a != 0:
          hand_type.append(b)
          hand_points.append(a)
          not_zero = True
          break
        a, b = self.is_four_kind(self.players_hands[i])
        if a != 0:
          hand_type.append(b)
          hand_points.append(a)
          not_zero = True
          break
        a, b = self.is_full_house(self.players_hands[i])
        if a != 0:
          hand_type.append(b)
          hand_points.append(a)
          not_zero = True
          break
        a, b = self.is_flush(self.players_hands[i])
        if a != 0:
          hand_type.append(b)
          hand_points.append(a)
          not_zero = True
          break
        a, b = self.is_straight(self.players_hands[i])
        if a != 0:
          hand_type.append(b)
          hand_points.append(a)
          not_zero = True
          break
        a, b = self.is_three_kind(self.players_hands[i])
        if a != 0:
          hand_type.append(b)
          hand_points.append(a)
          not_zero = True
          break
        a, b = self.is_two_pair(self.players_hands[i])
        if a != 0:
          hand_type.append(b)
          hand_points.append(a)
          not_zero = True
          break
        a, b = self.is_one_pair(self.players_hands[i])
        if a != 0:
          hand_type.append(b)
          hand_points.append(a)
          not_zero = True
          break
        a, b = self.is_high_card(self.players_hands[i])
        if a != 0:
          hand_type.append(b)
          hand_points.append(a)
          not_zero = True
          break

    # The player and their hand is printed out.
    for i in range(self.num_players):
      print('Player ' + str(i + 1) + ': ' + hand_type[i])
    print()

    # A dictionary with the types of hands and the h values is made
    hand_to_points = {"Royal Flush" : 10, "Straight Flush" : 9, "Four of a Kind" : 8, "Full House" : 7, "Flush" : 6, "Straight" : 5, "Three of a Kind" : 4, "Two Pair" : 3, "One Pair" : 2, "High Card" : 1}
    # The players are each given an h value
    player_to_hand_to_point = []
    for i in range(self.num_players):
      for hand in hand_to_points:
        if hand_type[i] == hand:
          player_to_hand_to_point.append(hand_to_points[hand])
    # The highest hand is determined
    highest_hand = max(player_to_hand_to_point)

    multiple = 0
    tied_players = []
    tied_points = []
    # This determines whether there are multiple players with the highest hand
    for i in range(self.num_players):
      if(player_to_hand_to_point[i] == highest_hand):
        multiple += 1
        tied_players.append(i+1)
        tied_points.append(hand_points[i])

    # A copy of the tied points is made so values could be removed. This allows for tied players being printed in descending order
    # The max points is removed each time
    copy_tied_points = []
    for i in range(len(tied_points)):
      copy_tied_points.append(tied_points[i])
    if multiple > 1:
      for i in range(len(tied_points)):
        max_points = max(copy_tied_points)
        index = 0
        for j in range(len(tied_points)):
          if tied_points[j] == max_points:
            index = j
        print("Player " + str(tied_players[index]) + " ties.")
        copy_tied_points.remove(max_points)
    else:
      print("Player " + str(tied_players[0]) + " wins.")

    return ""


def main():
  # read number of players from stdin
  line = sys.stdin.readline()
  line = line.strip()
  num_players = int (line)
  if (num_players < 2) or (num_players > 6):
    return

  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()

if __name__ == "__main__":
  main()
