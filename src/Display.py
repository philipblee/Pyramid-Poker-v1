""" Board is a class that displays cards on Canvas
    if Board.cardlist populated, it displays cards in one row
    if Board.handslist populated, it plays all six hands and
        displays them with showdown points by hand and total

"""


import tkinter as tk
import tkinter.font as font
from create_card_images import create_card_images
from PlaySixHands25 import *
from display_points import *
from Deck import Deck  # Board uses Deck2
from Display_Pyramid_Hand import *

class Display():
    def __init__(self):
        print ("running class Board init")

        new_list1 = [[0, 0, 0, 0, 0, 0, 0] for i in range (7)]
        new_list2 = [new_list1 for i in range (7)]


        self.player_win_points = new_list2

        self.player_names = ["Pete", "John", "Ming", "Tony", "Ed", "Phil"]
        self.Y_GAP = 95
        self.X_GAP = 72
        self.CANVAS_H = 7 * self.Y_GAP
        self.CANVAS_W = 25 * self.X_GAP
        self.X_OFFSET = 10
        self.Y_OFFSET = 10
        self.pyramid_poker_hands = []
        self.twentyfive_cards = []
        self.card_image_dict ={}

    def display_next_hand(self, *args):
        """ Create the card list use Deck().deal and display_cardlist them"""
        # global twentyfive_cards, six_hands
        # disable show_next and enable show_best
        print("running display_next_hand")
        # display_best25_hand_button["state"] = "normal"
        # display_next_hand_button["state"] = "disabled"
        # six_hands = Deck(6, 25, 3).deal()
        # pyramid_poker_hand = six_hands[0]
        pyramid_poker_hand = self.pyramid_poker_hands[0]
        twentyfive_cards = (sorted(pyramid_poker_hand, key=rank_sort, reverse=True))
        # window.title("Play Pyramid Poker")
        # w.delete("all")  # clear out last hand

        # playing_board is list(number of white squares, then list of yellow cells)
        playing_board = [[0, []],
                         [1, []],
                         [3, []],
                         [5, [3, 4]],
                         [6, [3, 4, 5]],
                         [8, [5, 6, 7]],
                         [10, [5, 6, 7, 8, 9]]]

        X_OFFSET = 5 * self.X_GAP + 5
        y = self.Y_OFFSET

        for hand_show in playing_board[6:0:-1]:
            x = X_OFFSET
            fill_color = "white"
            squares = hand_show[0]
            yellow = hand_show[1]
            for i in range(squares):
                if i in yellow:
                    fill_color = "light yellow"
                w.create_rectangle((x, y, x + self.X_GAP, y + self.Y_GAP), fill=fill_color, tag=("hand" + str(i), "board"))
                x += self.X_GAP
            y += self.Y_GAP

        # create 5 grey rectangles - discards
        x = 5
        for i in range(5):
            fill_color = "light grey"
            w.create_rectangle((x, y, x + self.X_GAP, y + self.Y_GAP), fill=fill_color, tags=("hand3", "board"))
            x += self.X_GAP

        self.show_twentyfive_cards()
        # rank_button["state"] = "disabled"

        # clear out player, best and diff scores for previous hand
        x = 10 * self.X_GAP + 6
        y = 3 * self.Y_GAP + 15
        display_points_clear(x, y)  # best hand points

    def show_twentyfive_cards(self):
        w.delete("card")
        x = 0
        y = 12
        # conserve space - put cards 5 x 5 matrix
        for card in self.twentyfive_cards:
            w.create_image(x + 4, y - 4, image=self.card_image_dict[card], anchor="nw", tags=("card", card))
            x += self.X_GAP
            if x > 4 * self.X_GAP:
                y += self.Y_GAP
                x = 0

    def display_cardlist(self):
        print ("running display_cardlist")
        window1 = tk.Tk()

        window_label = tk.Label(window1, text = "window1")
        window_label.place(x = 25, y = 25)
        window_label.pack()
        hand_separation = 1.04
        X_GAP_factor = .8
        self.CANVAS_W = 25 * self.X_GAP * X_GAP_factor * hand_separation + 25
        self.X_GAP = 72 * X_GAP_factor
        self.CANVAS_H = 8.2 * self.Y_GAP + 25
        self.Y_OFFSET = 2.2 * self.Y_GAP
        image_dict = create_card_images()
        w2 = tk.Canvas(window1, height=self.CANVAS_H, width=self.CANVAS_W, bg="light blue")
        xloc = self.X_OFFSET
        yloc = self.Y_OFFSET
        for card in self.cardlist:
            print(card, image_dict[card],xloc, yloc)
            w2.create_image(xloc, yloc, image=image_dict[card], anchor="nw", tags=("card"))
            xloc += self.X_GAP
            if xloc >= self.CANVAS_W:
                yloc = yloc + self.Y_GAP
                xloc = self.X_OFFSET
        w2.pack()
        w2.mainloop()

    def display_6hands(self):
        print ("running display_6hands")
        window2 = tk.Tk()

        hand_separation = 1.04
        X_GAP_factor = .8
        self.CANVAS_W = 30 * self.X_GAP * X_GAP_factor * hand_separation + 25
        self.X_GAP = 72 * .8
        self.CANVAS_H = 8.2 * self.Y_GAP + 25
        self.Y_OFFSET = 2.2 * self.Y_GAP
        card_image_dict = create_card_images()

        w = tk.Canvas(window2, height=self.CANVAS_H, width=self.CANVAS_W, bg="light blue")
        xloc = round(self.X_OFFSET)
        # print ("right before entering first for loop")
        # print (len(self.handslist))
        for handx in self.pyramid_poker_hands:
            yloc = round(self.Y_OFFSET)
            # print (handx)
            for i in range(1, 7):
                xloc_start = xloc
                if handx != []:
                    X_GAP_Factor = 1
                    if len(handx[i]) > 5:
                        X_GAP_Factor = 5/len(handx[i])
                    for card in handx[i]:
                        # print(card, xloc, yloc)
                        w.create_image(xloc, yloc, image=card_image_dict[card], anchor="nw", tags=("card"))
                        xloc += self.X_GAP * X_GAP_Factor
                    xloc = xloc_start
                    yloc = yloc + self.Y_GAP
            xloc = xloc_start + 5 * self.X_GAP * hand_separation
        
        # show player_win_points using grid method
        xloc = self.X_OFFSET
        yloc = 30
        player_win_points = self.player_win_points

        # points display parameters
        color = "white"
        label_width = 4
        line_height = 24
        font_size = 16
        for i in range(6):
            total_points = 0
            for j in range(6):
                total_points += player_win_points[i][j][0]
            # printing row labels
            tk.Label(window2, text="H1", font=font_size, bg=color, width=label_width).place(x=xloc, y=yloc)
            tk.Label(window2, text="H2", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+1*line_height)
            tk.Label(window2, text="H3", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+2*line_height)
            tk.Label(window2, text="H4", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+3*line_height)
            tk.Label(window2, text="H5", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+4*line_height)
            tk.Label(window2, text="H6", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+5*line_height)
            tk.Label(window2, text="Tot", font=font_size, bg=color, width = label_width).place(x=xloc, y=yloc+6*line_height)
            for j in range(6):
                player = self.player_names[j]
                xloc = xloc + 38
                if i == j:
                    player_win_points[i][j][1] = "-"
                    player_win_points[i][j][2] = "-"
                    player_win_points[i][j][3] = "-"
                    player_win_points[i][j][4] = "-"
                    player_win_points[i][j][5] = "-"
                    player_win_points[i][j][6] = "-"
                    player_win_points[i][j][0] = "-"
                # displaying player name for player j on row 1
                tk.Label(window2, text=player, font=("Arial 10 bold"), bg=color, width = label_width,
                         anchor="e").place(x=xloc+2, y=yloc-1*line_height)
                # displaying column of points for player j on rows 2-7
                tk.Label(window2, text=str(player_win_points[i][j][1]), font=font_size, bg=color, width = label_width,
                         anchor="e").place(x=xloc, y=yloc+0*line_height)
                tk.Label(window2, text=str(player_win_points[i][j][2]), font=font_size, bg=color, width = label_width,
                         anchor="e").place(x=xloc, y=yloc+1*line_height)
                tk.Label(window2, text=str(player_win_points[i][j][3]), font=font_size, bg=color, width = label_width,
                         anchor="e").place(x=xloc, y=yloc+2*line_height)
                tk.Label(window2, text=str(player_win_points[i][j][4]), font=font_size, bg=color, width = label_width,
                         anchor="e").place(x=xloc, y=yloc+3*line_height)
                tk.Label(window2, text=str(player_win_points[i][j][5]), font=font_size, bg=color, width = label_width,
                         anchor="e").place(x=xloc, y=yloc+4*line_height)
                tk.Label(window2, text=str(player_win_points[i][j][6]), font=font_size, bg=color, width = label_width,
                         anchor="e").place(x=xloc, y=yloc+5*line_height)
                tk.Label(window2, text=str(player_win_points[i][j][0]), font=font_size, bg=color, width = label_width,
                         anchor="e").place(x=xloc, y=yloc+6*line_height)

            # displaying total points on row 8
            tk.Label(window2, text=str(total_points),
                     font=font_size, bg=color, anchor="e", width=label_width).place(x=xloc, y=yloc+7*line_height)
            xloc = xloc + hand_separation * 70
        w.pack()
        w.mainloop()


# board2 = Board()
# board2.cardlist = Deck2.deal()[0]
# board2.display_cardlist()

# testing Board.display_6hands

