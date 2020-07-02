from Deck import Deck
from DisplayBoard import DisplayBoard
from PlaySixHands25 import PlaySixHands25

endgame = False
while endgame == False:

    display = DisplayBoard()
    pyramid_poker_hands = Deck(6, 25, 3).deal()

    print ("running PyramidMain")

    for i in range(6):
        print (pyramid_poker_hands[i])

    # playsixhands populates best_pyramid_hands and player_win_points
    playsixhands = PlaySixHands25(pyramid_poker_hands)

    # put best 6 hands into display.pyramid_hands
    display.pyramid_poker_hands = playsixhands.best_pyramid_hands
    display.player_win_points = playsixhands.player_win_points

    # after populating display.attributes, display_6hands
    display.display_6hands()

    # now put up playing area
    display.pyr = pyramid_poker_hands[0]
    display.display_next_hand()
    # get player hand
    # populate results of pyramid_hands[0] with player hand
    # now put up playing area