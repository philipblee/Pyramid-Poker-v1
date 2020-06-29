import unittest
from src.Deck import *

class Test_Deck(unittest.TestCase):

    def test_Deck_6_25_3(self):
        deck = Deck(6, 25 ,3)
        pyramid_poker_hands = deck.deal()
        self.assertEqual(len(pyramid_poker_hands), 6)
        self.assertEqual(len(pyramid_poker_hands[0]), 25)
        self.assertEqual(len(deck.deck), 159)

    def test_Deck_4_25_2(self):
        deck = Deck(4, 25, 2)
        deck.num_decks = 2
        deck.num_players = 4
        pyramid_poker_hands = deck.deal()
        self.assertEqual(len(pyramid_poker_hands), 4)
        self.assertEqual(len(pyramid_poker_hands[0]), 25)
        self.assertEqual(len(deck.deck), 106)

    def test_Deck_5_25_3(self):
        deck = Deck(5, 25, 3)
        pyramid_poker_hands = deck.deal()
        self.assertEqual(len(pyramid_poker_hands), 5)
        self.assertEqual(len(pyramid_poker_hands[0]), 25)
        self.assertEqual(len(deck.deck), 159)

    def test_Deck_5_25_1(self):
        deck = Deck(1, 25, 3)
        pyramid_poker_hands = deck.deal()
        self.assertEqual(len(pyramid_poker_hands), 1)
        self.assertEqual(len(pyramid_poker_hands[0]), 25)
        self.assertEqual(len(deck.deck), 159)

    def test_Deck_7_25_1(self):
        deck = Deck(7, 25, 3)
        pyramid_poker_hands = deck.deal()
        self.assertEqual(len(pyramid_poker_hands), 7)
        self.assertEqual(len(pyramid_poker_hands[0]), 25)
        self.assertEqual(len(deck.deck), 212)


suite = unittest.TestLoader().loadTestsFromTestCase(Test_Deck)
unittest.TextTestRunner(verbosity=3).run(suite)