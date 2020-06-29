from src.print_obj import *
from src.Analysis import Analysis
from src.Deck import Deck


g = globals()
l = locals()
x = 10
y = 20
z = 30

print_obj(x, g)
print_obj(y, g)
print_obj(z, g)

# print_obj(g, g)

print (g)

print (l)

pyramid_poker_hands = Deck(6, 25, 3).deal()
a = Analysis(pyramid_poker_hands[0])


print_obj(a.singles_list, g)
print_obj(a.pairs_list, g)
print_obj(a.trips_list, g)

