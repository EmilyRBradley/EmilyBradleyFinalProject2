from tkinter import *


class GUI:
    def __init__(self, window):
        self.window = window
        self.cells = {}

        self.frame_title = Frame(self.window)
        self.label_title = Label(self.frame_title, text='SUDOKU')
        self.label_title.pack(padx=10, side='top')
        self.frame_title.pack(anchor='center', pady=10)

        self.frame_board = Frame(self.window)
        for row in range(9):
            for col in range(9):
                entry_box = Entry(self.frame_board, width=3)
                self.cells[entry_box] = (row, col)
                entry_box.grid(row=row, column=col, padx=1, pady=1)
        self.frame_board.pack()

        self.frame_enter = Frame(self.window)
        self.button_enter = Button(self.frame_enter, text='ENTER', command=self.check_entry)
        self.label_check = Label(self.frame_enter, text='')
        self.button_enter.pack(padx=5, side='top')
        self.label_check.pack(padx=5, side='top')
        self.frame_enter.pack(anchor='s', pady=10)

    def check_entry(self):
        try:
            for row, col in self.cells:
                test_num = self.entry_box.get()
                test_num = int(test_num)
                if test_num < 0 or test_num > 10:
                    raise TypeError
        except TypeError:
            self.label_check.config(text='Values must be between 1-9')
        except ValueError:
            self.label_check.config(text='Enter numeric values')

