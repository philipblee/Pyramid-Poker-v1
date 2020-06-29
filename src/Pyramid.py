import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class Pyramid(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Home, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Home)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Pyramid Poker Home Page", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        buttonhome = tk.Button(self, text="Home", command=lambda: controller.show_frame(Home))
        buttonhome.pack()

        buttonplay = tk.Button(self, text="Play Pyramid Poker", command=lambda: controller.show_frame(PageOne))
        buttonplay.pack()

        buttonview = tk.Button(self, text="View Results", command=lambda: controller.show_frame(PageTwo))
        buttonview.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Play Pyramid Poker", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        buttonhome = tk.Button(self, text="Home", command=lambda: controller.show_frame(Home))
        buttonhome.pack()

        buttonplay = tk.Button(self, text="Play Pyramid Poker", command=lambda: controller.show_frame(PageOne))
        buttonplay.pack()

        buttonview = tk.Button(self, text="View Results", command=lambda: controller.show_frame(PageTwo))
        buttonview.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="View Results", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        buttonhome = tk.Button(self, text="Home", command=lambda: controller.show_frame(Home))
        buttonhome.pack()

        buttonplay = tk.Button(self, text="Play Pyramid Poker", command=lambda: controller.show_frame(PageOne))
        buttonplay.pack()

        buttonview = tk.Button(self, text="View Results", command=lambda: controller.show_frame(PageTwo))
        buttonview.pack()


pyramid = Pyramid()
pyramid.mainloop()