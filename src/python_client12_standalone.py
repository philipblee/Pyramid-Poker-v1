"""python_client12_standalone
"""

from Deck import Deck
from display_points import display_points, display_points_clear
from create_card_images import create_card_images
from PlayerHand import PlayerHand
from BestHand25Wild import BestHand25Wild
import tkinter as tk
from sort_cards import rank_sort, suit_rank_sort
from PlaySixHands25 import PlaySixHands25

player_names = ["Peter ", "Johnny", "Ming  ", "Tony  ", "Edmond", "Philip"]
window = tk.Tk()
topFrame = tk.Frame(window)

def onClick(event):
    w.click = event.x, event.y
    w.tag_raise("current")

def onMotion(event):
    x, y = w.click
    dx = event.x - x
    dy = event.y - y
    w.move('current', dx, dy)
    w.click = event.x, event.y

def onRelease(event):  # anytime you change where widgets are, you need to fix
    """ when left-mouse button is released, place card in card slot if empty,
        if it is not empty, move it 1/10 of X_GAP to right
        if, <= 5 cards left, re-arrange in discard slots
        """
    Y_OFFSET = 9
    X_OFFSET = 0
    mx = (event.x - .5 * X_GAP) // X_GAP * X_GAP + 1 + X_OFFSET
    my = (event.y) // Y_GAP * Y_GAP + 20

    if my < 0: my = 0
    if my > 6 * Y_GAP: my = 6 * Y_GAP + Y_OFFSET
    if mx < 0: mx = 0
    if mx > 15 * X_GAP: mx = 15 * X_GAP

    current_card_x = w.coords("current")[0]
    current_card_y = w.coords("current")[1]
    delta_x = mx - current_card_x + 5
    delta_y = my - current_card_y - 11

    w.move("current", delta_x, delta_y)  # this just snaps into place based on rectangle
    current_card_x = w.coords("current")[0]
    current_card_y = w.coords("current")[1]
    x1 = current_card_x +10
    y1 = current_card_y +10
    x2 = current_card_x + X_GAP -10
    y2 = current_card_y + Y_GAP -10

    # look for "overlappers" to current card slot
    overlappers = w.find_overlapping(x1, y1, x2, y2)
    if len(overlappers) > 0:
        overlap_cards = []
        current_card = []
        # if tagged as "card" append, then remove tagged as "current"
        for object in overlappers:
            for tag in w.gettags(object):
                if tag == "card":
                    overlap_cards.append(object)
                if tag == "current":
                    current_card = object
        overlap_cards.remove(current_card)
        # print ("overlap cards", overlap_cards)

        # if overlap - moving card to right by 33%
        if overlap_cards != []:
            w.move("current", + X_GAP/4, 0)

    # count number of cards left
    cards_left = list(w.find_withtag("card"))
    list_of_cards_left = list(cards_left)
    for object_id in list_of_cards_left:
        # remove those with x > 5 or y < 0 or y == 6
        if w.coords(object_id)[0] > 5 * X_GAP - 10 or \
            w.coords(object_id)[1] < 0 * Y_GAP or \
            w.coords(object_id)[1] == 6 * Y_GAP:
            cards_left.remove(object_id)

    fixed_destination = [0*X_GAP + 9, 6 * Y_GAP+19], [1*X_GAP + 9, 6 * Y_GAP+19], \
                        [2*X_GAP + 9, 6 * Y_GAP+19], [3*X_GAP + 9, 6 * Y_GAP+19], [4*X_GAP + 9, 6 * Y_GAP+19]
    start_location = 5 - len(cards_left)   # start_location is between 0 and 4, 5 cards start at 0, 4 at 1
    destination = fixed_destination[start_location:]

    # when there are 5 or less cards left, move cards to discard area
    index = 0
    if len(cards_left) <= 5:
        for object_id in cards_left:
            x_coord = w.coords(object_id)[0]
            y_coord = w.coords(object_id)[1]
            delta_x = destination[index][0] - x_coord
            delta_y = destination[index][1] - y_coord - 10
            w.move(object_id, delta_x, delta_y)
            index += 1
    return

def display_next_hand(*args):
    """ Create the card list use Deck().deal and display_cardlist them"""
    global twentyfive_cards, six_hands
    # disable show_next and enable show_best
    display_best25_hand_button["state"] = "normal"
    display_next_hand_button["state"] = "disabled"
    six_hands = Deck(6, 25, 3).deal()
    pyramid_poker_hand = six_hands[0]
    twentyfive_cards = (sorted(pyramid_poker_hand, key =rank_sort, reverse=True))
    window.title("Play Pyramid Poker")
    w.delete("all")   # clear out last hand

    # create 10 rectangles - hand 6
    X_OFFSET = 5 * X_GAP + 5
    x = X_OFFSET
    y = Y_OFFSET
    for i in range(10):
        fill_color = "light yellow"
        if i >= 0 and i <= 4:
            fill_color = "white"
        w.create_rectangle((x, y , x + X_GAP, y + Y_GAP), fill=fill_color, tag=("hand6", "board"))
        x += X_GAP

    # create 7 rectangles - hand 5
    x = X_OFFSET
    y += Y_GAP
    for i in range(8):
        fill_color = "light yellow"
        if i <= 4:
            fill_color = "white"
        w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill=fill_color, tags=("hand5", "board"))
        x += X_GAP

    # create 6 rectangles - hand 4
    x = X_OFFSET
    y += Y_GAP
    for i in range(6):
        fill_color = "white"
        if i == 3 or i == 4 or i == 5:
            fill_color = "light yellow"
        w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill=fill_color, tags=("hand4", "board"))
        x += X_GAP

    # create 5 rectangles - hand 3
    x = X_OFFSET
    y += Y_GAP
    for i in range(5):
        fill_color = "white"
        if i == 4 or i == 3:
            fill_color = "light yellow"
        w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill=fill_color, tags=("hand3", "board"))
        x += X_GAP

    # create 3 rectangles - hand 2
    x = X_OFFSET
    y += Y_GAP
    for i in range(3):
        w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill="white", tags=("hand2","board"))
        x += X_GAP

    # create 1 rectangle - hand 1
    x = X_OFFSET
    y += Y_GAP
    for i in range(1):
        w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill="white", tags=("hand1","board"))
        x += X_GAP

    # create 5 grey rectangles - discards
    x = 5
    y += Y_GAP
    for i in range(5):
        fill_color = "light grey"
        w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill=fill_color, tags=("hand3", "board"))
        x += X_GAP

    show_twentyfive_cards()
    rank_button["state"] = "disabled"

    # clear out player, best and diff scores for previous hand
    x = 10 * X_GAP + 6
    y = 3 * Y_GAP + 15
    display_points_clear(x, y) # best hand points

def show_twentyfive_cards():
    w.delete("card")
    x = 0
    y = 12
    # conserve space - put cards 5 x 5 matrix
    for card in twentyfive_cards:
        w.create_image(x + 4, y - 4, image=image_dict[card], anchor="nw", tags=("card", card))
        x += X_GAP
        if x >4 * X_GAP:
            y += Y_GAP
            x = 0

def toggle_finished():
    if display_best25_hand_button["state"] == "normal":
        display_best25_hand_button["state"] = "disabled"
        disable_show_best["text"] = "Toggle"
    else:
        display_best25_hand_button["state"] = "normal"
        disable_show_best["text"] = "Toggle"

def display_player_hand():
    """ determines player_hand based on position of cards in twentyfive_cards
    """
    player_hand = [[],[],[],[],[],[],[]]
    player_hand_points = [0,0,0,0,0,0,0]
    min_cards = [0, 1, 3, 3, 3, 5, 5]

    # determine the player_hand based on Board placement of cards
    for card in twentyfive_cards:
         card_placex = int((w.coords(card)[0] + X_OFFSET)//X_GAP) + 1 # determines x coordinate of card
         card_placey = int((w.coords(card)[1] + Y_OFFSET)//Y_GAP) # determines y coordinate of card
         if card_placex > 5 and card_placey != 6:
             hand_number = 6 - card_placey
             player_hand[hand_number].append(card)

    # check for missing the minimum cards per pokerhand
    valid_hand = True
    for i in range(1, 7):
        if len(player_hand[i]) < min_cards[i]:
            valid_hand = False
            message = "Player Hand is missing cards - Try again"

    # check to make sure hand6>hand5, etc.
    if valid_hand == True:
        # replace wild card with specific card
        player = PlayerHand(player_hand)
        player_hand_points = player.player_hand_score

        for i in range (1,6):
            # print (i+1, player_hand_score[i+1], i, player_hand_score[i])
            if player_hand_points[i+1] <= player_hand_points[i]:
                valid_hand = False
                message = "Player Hand out of order - Try again"
                # print (message)

    if valid_hand == False:

        pass
        # message = "Player Hand Invalid - Try Again"

    else:
        message = "Player Hand Valid"
        x_label = 10 * X_GAP + 10 # for labels
        y_label = 310 + 150 # aligns with player hand
        xloc3 = x_label
        yloc3 = y_label + 25
        valid_hand_label = tk.Label(text=message , fg="blue", bg="white", font=12)
        valid_hand_label.place(x=x_label + 3 *X_GAP, y=y_label+75)
        player_hand_label = tk.Label(text="Player's Hand Points" , fg="blue", bg="white", font=12)
        player_hand_label.place(x=x_label, y=y_label+25)
        display_points(player_hand_points, xloc3, yloc3 + 25)
    return player_hand_points

def display_best25_hand(*args):
    """ Given twenty_five cards, find the best hand and show scoring
    """
    global message_left_click_label

    display_best25_hand_button["state"] = "disabled"
    display_next_hand_button["state"] = "normal"

    player_points = display_player_hand()
    player_total_points = player_points[0]

    message_left_click_label = tk.Label(text="TBD")

    # make sure there are cards in twentyfive_cards
    if twentyfive_cards == []:
        message_left_click_label = tk.Label(text="Click button - Show Next Hand")
        message_left_click_label.pack()
        return
    message_left_click_label.pack_forget()

    card_list2 = twentyfive_cards
    # card_list2_string = ", ".join(card_list2)
    # logging.info(card_list2_string)

    # start_time = time.time()
    temp_card_list2 = list(card_list2)
    myhand = BestHand25Wild(temp_card_list2)
    besthand25_points = myhand.best_hand_points
    best_25handx = myhand.best_25handx

    # showing best hand
    window.title("Best Hand Below and Best Scores on Right")
    y_list = [0, 5 * Y_GAP, 4 *  Y_GAP, 3 * Y_GAP, 2 * Y_GAP, Y_GAP, 0]
    for i in [6,5,4,3,2,1]:
        x = 8
        y = y_list[i]+8
        overlap_factor = 1
        for card in best_25handx[i]:
            if len(best_25handx[i]) > 5:
                overlap_factor = 5/(len(best_25handx[i])+1)
            w.create_image(x, y, image=image_dict[card[0:3]], anchor="nw", tag="best")
            x += X_GAP * overlap_factor

    # showing points of best hand
    x_label = 10 * X_GAP + 10
    y_label = 310 # aligns with best_hand
    x = x_label
    y = y_label
    display_points(besthand25_points, x, y)

    player_total_adv = player_total_points - besthand25_points[0]

    # display_cardlist points diff next to player scores, y is the same, x is 200 less
    x_label = 13 * X_GAP
    y = y
    points_diff = [0,0,0,0,0,0,0]
    for i in range (1,7):
        points_diff[i] = round(player_points[i][1] - besthand25_points [i][1], 3)
    points_diff[0] = round (player_points[0] - besthand25_points[0],3)

    display_points(points_diff, x_label, y)

    # keeping points of wins, losses and ties
    global wins
    global ties
    global losses
    global cumulative_points

    if player_total_points > besthand25_points[0]:
         wins += 1
         # print ("Player Wins - ", end="")

    elif besthand25_points[0] > player_total_points:
         losses +=1
         # print ("Player Loses - ", end="")

    elif besthand25_points[0] == player_total_points:
         ties +=1
         # print ("Player Ties - ", end="")

    cumulative_points += player_total_adv
    cumulative_points = round(cumulative_points, 2)

    x_label = 13 * X_GAP
    y_label = 7 * Y_GAP
    wins_label = tk.Label(text="wins = " + str(wins) + 5 * " ", fg="blue", bg="white", font=12)
    wins_label.place(x=x_label, y=y_label-75)
    losses_label = tk.Label(text="losses = " + str(losses) + 5 * " ", fg="blue", bg="white", font=12)
    losses_label.place(x=x_label, y=y_label-50)
    ties_label = tk.Label(text="ties = " + str(ties)+ 5 * " ", fg="blue", bg="white", font=12)
    ties_label.place(x=x_label, y=y_label-25)
    cum_label = tk.Label(text="cum = " + str(cumulative_points) + 12 * " ", fg="blue", bg="white", font=12)
    cum_label.place(x=x_label, y=y_label)

def switch_best():
    if display_best25_hand_button["state"] == "normal":
        display_best25_hand_button["state"] = "disabled"
        disable_show_best["text"] = "Toggle"
    else:
        display_best25_hand_button["state"] = "normal"
        disable_show_best["text"] = "Toggle"

def switch_next():
    if display_next_hand_button["state"] == "normal":
        display_next_hand_button["state"] = "disabled"
        disable_show_next["text"] = "Toggle"
    else:
        display_next_hand_button["state"] = "normal"
        disable_show_next["text"] = "Toggle"
        
def switch_player_score():
    if display_player_hand_button["state"] == "normal":
        display_player_hand_button["state"] = "disabled"
        disable_show_player_score["text"] = "Toggle"
    else:
        display_player_hand_button["state"] = "normal"
        disable_show_player_score["text"] = "Toggle"

def switch_suit():
    if suit_button["state"] == "normal":
        suit_button["state"] = "disabled"
    else:
        suit_button["state"] = "normal"
        disable_show_next["text"] = "Toggle"

def switch_rank():
    if rank_button["state"] == "normal":
        rank_button["state"] = "disabled"
    else:
        rank_button["state"] = "normal"
        disable_show_next["text"] = "Toggle"

def switch_done():
    if done_button["state"] == "normal":
        done_button["state"] = "disabled"
    else:
        done_button["state"] = "normal"
        disable_show_next["text"] = "Toggle"

def suit_quick_sort():
    """ sorting by suit and display_cardlist"""
    twentyfive_cards.sort(key=suit_rank_sort, reverse=True)
    show_twentyfive_cards()
    suit_button["state"] = "disabled"
    rank_button["state"] = "normal"

def rank_quick_sort():
    """ sorting by rank and display_cardlist"""
    twentyfive_cards.sort(key=rank_sort, reverse=True)
    show_twentyfive_cards()
    rank_button["state"] = "disabled"
    suit_button["state"] = "normal"

def commandpass():
    pass

def showdown():
    global six_hands
    board4 = Board()
    playsixhands = PlaySixHands25(six_hands)
    board4.pyramid_hands = playsixhands.best_pyramid_hands
    board4.player_win_points = playsixhands.player_win_points
    board4.display_6hands()

image_dict = create_card_images()
X_GAP = 72
Y_GAP = 95
X_OFFSET = 10
Y_OFFSET = 7
y = Y_OFFSET
x = X_OFFSET
wins = 0
losses = 0
ties = 0
cumulative_points = 0
w = tk.Canvas(window, height=7*Y_GAP+10+Y_OFFSET + 10, width=15*X_GAP+X_OFFSET, bg="light blue", relief="raised")

xloc1 = 11 * X_GAP + 10
yloc1 = 2 * Y_GAP + 10
xloc2 =xloc1 + 2 * X_GAP
button_width = 1.9 * X_GAP

# finished_setup_button, toggle_show_next_hand to enable/disable
done_button = tk.Button(window, text="I'm Done!", font=12, command=commandpass)
done_button.place(x=xloc2, y=yloc1-75, width=button_width, height=24)
disable_done = tk.Button(window, text="Toggle", font=12, command=switch_done)
disable_done.place(x=xloc2, y=yloc1-50, width=button_width, height=24)
showdown_button = tk.Button(window, text="Showdown", font=12, command=showdown)
showdown_button.place(x=xloc2, y=yloc1-25, width=button_width, height=24)

# show_next_hand_button, toggle with disable_show_next
display_next_hand_button = tk.Button(window, text="Next Hand", font=12, command=display_next_hand)
display_next_hand_button.place(x=xloc1, y=yloc1, width=button_width, height=24)
disable_show_next = tk.Button(window, text="Toggle", font=12, command=switch_next)
disable_show_next.place(x=xloc2, y=yloc1, width=button_width, height=24)

# show_best25_hand_button, toggle_show_best to enable/disable
display_best25_hand_button = tk.Button(window, text="Best Hand", font=12, command=display_best25_hand)
display_best25_hand_button.place(x=xloc1, y=yloc1 + 25, width=button_width, height=24)
disable_show_best = tk.Button(window, text="Toggle", font=12, command=switch_best)
disable_show_best.place(x=xloc2, y=yloc1 + 25, width=button_width, height=24)

display_player_hand_button = tk.Button(window, text="Points", font=12, command=display_player_hand)
display_player_hand_button.place(x=xloc1, y=yloc1 + 50, width=button_width, height=24)
disable_show_player_score = tk.Button(window, text="Toggle", font=12, command=switch_player_score)
disable_show_player_score.place(x=xloc2, y=yloc1 + 50, width=button_width, height=24)

suit_button = tk.Button(window, text="Suit", font=12, command=suit_quick_sort)
suit_button.place(x=xloc1, y=yloc1 + 75, width=button_width, height=24)

rank_button = tk.Button(window, text="Rank", font=12, command=rank_quick_sort)
rank_button.place(x=xloc2, y=yloc1 + 75, width=button_width, height=24)

w.pack()
display_next_hand()

w.tag_bind("card", "<Button-1>", onClick)
w.tag_bind("card", "<B1-Motion>", onMotion)
w.tag_bind("card", "<ButtonRelease-1>", onRelease)

window.mainloop()