from src.PlayerHand import PlayerHand

class PyramidHand:
    """ PyramidHands
        :parameter
        pyramid_hands - 7 hands, hand 0 is empty, hand 1 to hand 6 of pyramid play
        :returns
    """
    def __init__(self, pyramid_hand):
        self.pyramid_hand = pyramid_hand
        self.pyramid_hand_points = [0,0,0,0,0,0,0]
        self.pyramid_compact = [[] for i in range(7)]
        # create compact format for all 6 hands
        for i in range(1,7):
            self.pyramid_compact[i] = '.'.join(self.pyramid_hand[i])

    def is_valid(self):
        """
        :returns: valid_hand, message
        """
        # check for missing the minimum cards per pokerhand
        min_cards = [0, 1, 3, 3, 3, 5, 5]
        valid_hand = True
        message = "Pyramid Hand is Valid"
        for i, poker_hand in enumerate(self.pyramid_hand):
            if len(poker_hand) < min_cards[i]:
                valid_hand = False
                invalid = i
                message = "Hand "+ str(invalid) +" is missing cards - Try again"

        # check to make sure hand6>hand5, etc.
        if valid_hand == True:
            # replace wild card with specific card
            player = PlayerHand(self.pyramid_hand)
            self.pyramid_hand_points = player.player_hand_score

            for i in range(1, 6):
                # print (i+1, pyramid_hand_score[i+1], i, pyramid_hand_score[i])
                if self.pyramid_hand_points[i + 1] <= self.pyramid_hand_points[i]:
                    valid_hand = False
                    invalid = i
                    message = "Out of order - Hand " + str(invalid) + " > Hand " + str(invalid+1)
        return(valid_hand, message)


