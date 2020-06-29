import unittest
from src.LegalPokerHands import *

class Test_legalpokerhands(unittest.TestCase):

    def test_legalpokerhands_1(self):
        pyramid_poker_list = ['SA!', 'SA!', 'SA*', 'SA+', 'HA+', 'CA-', 'SK-', 'SK*', 'DK-', 'SQ-', 'SQ*', 'CQ+', 'SJ*',
                              'CT*', 'S9-', 'D9+', 'S7+', 'C6-', 'S5*', 'H5+', 'C5+', 'S4-', 'C4-', 'S3-', 'C2-']
        legalpokerhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalpokerhands.hand6_count, 1529)

    def test_legalpokerhands_2(self):
        pyramid_poker_list = ['SA=', 'SA=', 'SA*', 'SA+', 'HA+', 'CA-', 'SK-', 'SK*', 'DK-', 'SQ-', 'SQ*', 'CQ+', 'SJ*',
                              'CT*', 'S9-', 'D9+', 'S7+', 'C6-', 'S5*', 'H5+', 'C5+', 'S4-', 'C4-', 'S3-', 'C2-']
        legalpokerhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalpokerhands.hand4_count, 38)

    def test_legalpokerhands_3(self):
        pyramid_poker_list = ['SA=', 'SA=', 'SA*', 'SA+', 'HA+', 'CA-', 'SK-', 'SK*', 'DK-', 'SQ-', 'SQ*', 'CQ+', 'SJ*',
                              'CT*', 'S9-', 'D9+', 'S7+', 'C6-', 'S5*', 'H5+', 'C5+', 'S4-', 'C4-', 'S3-', 'C2-']
        legalpokerhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalpokerhands.hand1_count, 16)

    def test_legalpokerhands_4(self):
        pyramid_poker_list = ['SA=', 'SA=', 'SA*', 'SA+','SK-', 'SK*', 'SQ-', 'SQ*', 'SJ*',
                              'S9-', 'S7+', 'S5*', 'S4-', 'S3-']
        legalpokerhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalpokerhands.hand6_count, 1378)

    def test_legalpokerhands_7(self):
        pyramid_poker_list = ['SA!', 'SA=', 'SA*', 'SA+','SK-', 'SK*', 'SQ-', 'SQ*', 'SJ*',
                              'S9-', 'S7+', 'S5*', 'S4-', 'S3-']
        legalpokerhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalpokerhands.hand6_count, 1830)

    def test_legalpokerhands_8(self):
        pyramid_poker_list = ['SA!', 'SA=', 'SA*', 'SA+','SK-', 'SK*', 'SQ-', 'SQ*', 'SJ*',
                              'S9-', 'S7+', 'S5*', 'S4-', 'S3-']
        legalpokerhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalpokerhands.hand4_count, 16)

    def test_legalpokerhands_9(self):
        pyramid_poker_list = ['SA!', 'SA=', 'SA*', 'SA+','SK-', 'SK*', 'SQ-', 'SQ*', 'SJ*',
                              'S9-', 'S7+', 'S5*', 'S4-', 'S3-']
        legalpokerhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalpokerhands.hand6_count, 1830)

    def test_legalpokerhands_10(self):
        pyramid_poker_list = ['SA!', 'S8=', 'SA*', 'SA+','SK-', 'SK*', 'SQ-', 'SQ*', 'SJ*',
                              'S9-', 'S7+', 'S5*', 'S4-', 'S3-']
        legalpokerhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalpokerhands.hand6_count, 1949)

    def test_legalpokerhands_11(self):
        pyramid_poker_list = ['SA!', 'S8=', 'SA*', 'SA+','SK-', 'SK*', 'SQ-', 'SQ*', 'SJ*',
                              'S9-', 'S7+', 'S5*', 'S4-', 'S3-']
        legalpokerhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalpokerhands.hand4_count, 17)

    def test_legalpokerhands_12(self):
        pyramid_poker_list = ['SA!', 'S8=', 'SA*', 'SA+','SK-', 'SK*', 'SQ-', 'SQ*', 'SJ*',
                              'S9-', 'S7+', 'S5*', 'S4-', 'S3-']
        legalpokerhands = LegalPokerHands(pyramid_poker_list)
        self.assertEqual(legalpokerhands.hand1_count, 11)

suite = unittest.TestLoader().loadTestsFromTestCase(Test_legalpokerhands)
unittest.TextTestRunner(verbosity=3).run(suite)