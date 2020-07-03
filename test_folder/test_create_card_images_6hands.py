""" test_create_card_images is a class that displays six hands
 on Canvas
"""

import tkinter as tk

from src.Deck import *
from src.create_card_images import create_card_images

class test_create_card_images():
    """
    test_create_card_images
    """
    def __init__(self):
        pass


    def display_cardlist(self):
        window1 = tk.Tk()
        window_label = tk.Label(window1, text = "Playing Area")
        window_label.place(x = 25, y = 25)
        window_label.pack()
        hand_separation = 1.04
        X_GAP_factor = .6

        self.CARD_WIDTH = 72 * X_GAP_factor
        self.CARD_HEIGHT= 95

        self.CANVAS_W = 10 * self.CARD_WIDTH
        self.CANVAS_H = 7 * self.CARD_HEIGHT

        self.INITIAL_X = 0
        self.INITIAL_Y = 0

        image_dict = create_card_images()
        w1 = tk.Canvas(window1, height=self.CANVAS_H, width=self.CANVAS_W, bg="light blue")
        xloc = self.INITIAL_X
        yloc = self.INITIAL_Y
        for card in self.cardlist:
            w1.create_image(xloc, yloc, image=image_dict[card], anchor="nw", tags=("card"))
            xloc += self.CARD_WIDTH
            if xloc >= 5 * self.CARD_WIDTH:
                yloc = yloc + self.CARD_HEIGHT
                xloc = self.INITIAL_X
        w1.pack()
        w1.mainloop()

    def display_cardlists(self):
        window2 = tk.Tk()
        window_label = tk.Label(window2, text = "Playing Area")
        window_label.place(x = 25, y = 25)
        window_label.pack()
        hand_separation = 1.04
        X_GAP_factor = .7

        self.CARD_WIDTH = 72 * X_GAP_factor
        self.CARD_HEIGHT= 95

        self.CANVAS_H = 10 * self.CARD_HEIGHT
        self.CANVAS_W = 24 * self.CARD_WIDTH

        self.INITIAL_X = 0
        self.INITIAL_Y = 0

        image_dict = create_card_images()
        w2 = tk.Canvas(window2, height=self.CANVAS_H, width=self.CANVAS_W, bg="light grey")
        xloc = self.INITIAL_X
        yloc = self.INITIAL_Y
        xstart = xloc
        index = 0
        for cardlist in self.cardlists:
            xloc = round(xloc,2)
            # cardlist[0] starts at 0,0  cardlist[1] starts at 4,0, cardlist[2] 8,0
            for card in cardlist:
                # print (card, xloc, yloc)
                if index <= 5:
                    w2.create_image(xloc, yloc, image=image_dict[card], anchor="nw", tags=("card"))
                    xloc = round((xloc + self.CARD_WIDTH), 2)
                    if xloc - xstart >= 3 * X_GAP_factor * self.CARD_WIDTH:
                        xloc = xstart
                        yloc = round((yloc + self.CARD_HEIGHT),2)
            index = index + 1
            # now we need to make sure x is +4, and y is 0
            xloc = xstart + 4 * self.CARD_WIDTH + X_GAP_factor
            xstart = round(xloc,2)
            yloc = self.INITIAL_Y

        w2.pack()
        w2.mainloop()

test = test_create_card_images()  # create object
test.cardlists = Deck(6, 25, 3).deal() # set attribute test_folder.cardlist to first hand
test.display_cardlists()