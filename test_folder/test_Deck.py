from src.Deck import *


deck = Deck(6, 25, 3)
pyramid_poker_list = deck.deal()[0]
print (pyramid_poker_list)

pyramid_poker_string = '.'.join(pyramid_poker_list)
print (pyramid_poker_string)
print (pyramid_poker_string.split("."))
