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
        self.cardlist = []
        self.card_image_dict = {}
        pass


    def display_cardlist(self):
        window1 = tk.Tk()
        window_label = tk.Label(window1, text = "Playing Area")
        window_label.place(x = 25, y = 25)
        window_label.pack()
        hand_separation = 1.04
        X_GAP_factor = .6
        print (self.cardlist)
        self.CARD_WIDTH = 72 * X_GAP_factor
        self.CARD_HEIGHT= 95

        self.CANVAS_W = 10 * self.CARD_WIDTH
        self.CANVAS_H = 7 * self.CARD_HEIGHT

        self.INITIAL_X = 0
        self.INITIAL_Y = 0

        self.card_image_dict = create_card_images()
        w2 = tk.Canvas(window1, height=7 * 100, width=15 * 70, bg="light blue", relief="raised")
        i = 0
        j = 0
        for card in self.cardlist:
            w2.create_image(70 * i + 35, 100 * j + 50, image=self.card_image_dict[card])
            i += 1
            if i > 12:
                i = 0
                j = j + 1

        w2.pack()
        w2.mainloop()

test = test_create_card_images()  # create object
test.cardlist = Deck(1,52,1).deck
test.display_cardlist()

