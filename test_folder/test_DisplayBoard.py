from src.DisplayBoard import DisplayBoard
from src.Deck import Deck
from src.ShowDownPoints import ShowDownPoints
from src.PlaySixHands25 import PlaySixHands25


# testing Display.display_6hands
displayboard = DisplayBoard()
playsixhands = PlaySixHands25(Deck(6, 25, 3).deal())
displayboard.pyramid_hands = playsixhands.best_pyramid_hands

displayboard.player_win_points = playsixhands.player_win_points
displayboard.display_6hands()