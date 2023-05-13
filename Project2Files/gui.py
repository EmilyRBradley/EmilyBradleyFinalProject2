from tkinter import *

class GUI:
    def __init__(self, window):
        self.window = window
        self.cells = {}
        self.create_gameboard()

    def create_gameboard(self):
        board_frame = Frame(self.window)
        for row in range(9):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(9):
                entry_box = Entry(self.board_frame, width=30)
                self._cells[entry_box] = (row, col)
                entry_box.grid(row=row, column=col, padx=1, pady=1)
        board_frame.pack()
