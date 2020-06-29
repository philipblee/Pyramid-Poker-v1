'''
Created on Jan 14, 2018
@author: aditya
This program shows the use of notebook in tkinter
Notebook is used to create Tabs in the application.
This enables browsing different pages in the application.
Frame widget from tkinter is used in this Application to demostrate the use of Notebook/tabs.
Please note that other widgets can also be used as per the requirement.
'''

import tkinter as tk
from tkinter import ttk

from DisplayPyramid import DisplayPyramid

class NoteBookApp:
    def __init__(self, master):
        self.master = master
        self.notebk = ttk.Notebook(self.master)
        self.notebk.pack()
        self.frame1 = ttk.Frame(self.notebk, width=1000, height=800, relief=tk.SUNKEN)
        self.frame2 = ttk.Frame(self.notebk, width=1000, height=800, relief=tk.SUNKEN)
        self.frame4 = ttk.Frame(self.notebk, width=1000, height=800, relief=tk.SUNKEN)
        self.notebk.add(self.frame1, text='One')
        self.notebk.add(self.frame2, text='Two')
        self.notebk.add(self.frame4, text='Three')


def launchNoteBookApp():
    root = tk.Tk()
    NoteBookApp(root)
    tk.mainloop()


if __name__ == '__main__':
    launchNoteBookApp()