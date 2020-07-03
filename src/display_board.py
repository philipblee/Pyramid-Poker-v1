def display_board(w, X_GAP, Y_GAP, X_OFFSET, Y_OFFSET):
    """
    displays empty board with no cards on Canvas w
    :param w: Canvas
    :param X_GAP: card width
    :param Y_GAP: card height
    :param X_OFFSET: shift card rectangles from x axis
    :param Y_OFFSET: shift card rectangles from y axis
    :return:
    """
  # playing_board is list(total number white squares, then list of yellow cells)
    playing_board = [[0,[]],
                    [1,[]],
                    [3,[]],
                    [5,[3,4]],
                    [6,[3,4,5]],
                    [8,[5,6,7]],
                    [10,[5,6,7,8,9]]]

    X_OFFSET = 5 * X_GAP + 5
    y = Y_OFFSET

    for hand_show in playing_board[6:0:-1]:
        x = X_OFFSET
        fill_color = "white"
        squares = hand_show[0]
        yellow = hand_show[1]
        for i in range(squares):
            if i in yellow:
                fill_color = "light yellow"
            w.create_rectangle((x, y, x + X_GAP, y + Y_GAP), fill=fill_color, tag=("hand"+str(i), "board"))
            x += X_GAP
        y += Y_GAP

    # create 5 grey rectangles - discards
    x = 5
    for i in range(5):
        fill_color = "light grey"
        w.create_rectangle((x + 5*X_GAP, y, x + 6*X_GAP, y + Y_GAP), fill=fill_color, tags=("hand3", "board"))
        x += X_GAP
