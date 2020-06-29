from src.create_card_images import *
from src.Deck import *

""" create_card_images_test displays six hands
one pyramid hand of 25 card per row
"""

root = tk.Tk()
card_image_dict = create_card_images()
# for k in card_image_dict:
#     print (k, card_image_dict[k])

deck = Deck(6,25,3)
pyramid_poker_lists = deck.deal()

Y_GAP = 95
X_GAP = 72
CANVAS_H = 7 * Y_GAP
CANVAS_W = 25 * X_GAP
X_OFFSET = 10
Y_OFFSET = 10
xloc = X_OFFSET
yloc = Y_OFFSET

w = tk.Canvas(root, height=CANVAS_H, width=CANVAS_W, bg="light blue")
for pyramid_poker_list in pyramid_poker_lists:
    for card in pyramid_poker_list:
            # print (card, card_image_dict[card])
            w.create_image(xloc, yloc, image=card_image_dict[card], anchor="nw", tags=("card"))
            xloc += X_GAP
            if xloc >= CANVAS_W:
                yloc = yloc + Y_GAP
                xloc = X_OFFSET

w.pack()
w.mainloop()



