from src.Analysis import *
from src.Deck import *
from varname import nameof

pyramid_poker_list = Deck(6, 25, 3).deal()[0]
# pyramid_poker_list =['S2-', 'D2-', 'D3*', 'H5+', 'D4+', 'S4*', 'H8+', 'S9+', 'C7-', 'H7*', 'D9*', 'S7-', 'H5*', 'D7-', 'HA*', 'D6*', 'SA-', 'H4*', 'D3+', 'CT+', 'ST*', 'C7*', 'H4-', 'HQ-', 'C5-']
# pyramid_poker_list  =['CT-', 'H3*', 'S9+', 'D7-', 'D4-', 'CJ+', 'H5-', 'S8+', 'CK-', 'HT-', 'SQ+', 'D9+', 'H2+', 'H4*', 'H8-', 'SA-', 'H5+', 'H9+', 'SQ*', 'SJ-', 'SQ-', 'C4-', 'C2-', 'DQ*', 'H6-']
# pyramid_poker_list = \
# ['DA+', 'DA*', 'CA-', 'HK+', 'HQ+', 'DQ+', 'HJ-', 'HJ*', 'ST*', 'HT*', 'DT-', 'CT-', 'S9+', 'H9*', 'H8*', 'D8-', 'C8*', 'D7*', 'D7-', 'D6*', 'H5-', 'D5-', 'C5-', 'H4*', 'C3*']

print (pyramid_poker_list.sort(key=rank_sort))
analysis = Analysis(pyramid_poker_list)

def print_var(variable):
    print (nameof(variable), variable)

for i in range(0, 51):
    print ('{:<2} {:<18} {:<5} {}'.format(i, analysis.desc[i], len(analysis.suit_rank_array[i]), analysis.suit_rank_array[i]))
