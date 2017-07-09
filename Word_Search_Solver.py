#__author__ = 'Launa Greer'

import tkinter
from tkinter import *

# START
# Test Case:  Receive a word search puzzle
#puzzle = ['GNEEB', 'GOMCI','RIAAR','ALHTD','TPIGS']
puzzle = ['OLACUCCCCBCD', 'JORNUIAYZWYL', 'DTGXQDSOSAND', 'WIRHPHTWNJHB', 'WOMZWZLVJMBN', 'FNTUBEEVZMHO',
    'SWIMMINGSUIT', 'CTOWELKQZBFO', 'RVULBALLOJSV', 'AUZGGJBEACHD', 'BSUNGLASSESZ', 'ICECREAMUBAX']

def word_locator(p, w):
    # Search for given word 'w' spelled either backwards or forwards
    word = w
    backwards_word = word[::-1]

    # Determine the dimensions of the puzzle, p
    puzzle_height = len(p[0])
    puzzle_width = len(p)

    # Search rows of puzzle for word spelled backwards or forwards.  If found, return list of letter coordinates.
    for row in p:
        if word in row or backwards_word in row:
            if word in row:
                starting_index = row.index(word)
            else:
                starting_index = row.index(backwards_word)
            return [[p.index(row), letter] for letter in range(starting_index,starting_index + len(word))]

    # Search columns of puzzle for word spelled backwards or forwards. If found, return list of letter coordinates.
    for i in range(0, puzzle_width):
        column = ""
        column_coord = []
        for row in p:
            column += row[i]
            column_coord.append([p.index(row), i])
        if word in column or backwards_word in column:
            if word in column:
                starting_index = column.index(word[0])
            else:
                starting_index = column.index(word[-1])
            return [column_coord[i] for i in range(starting_index, starting_index + len(word))]

    # Search upward and downward diagonals of puzzle for word spelled backwards or forwards.
    # If found, return list of letter coordinates. NOTE:  Based on a matrix transformation developed by user
    # from stackoverflow.com
    for y in range(0, 2 * puzzle_width - 1):
        up_diagonal = ''
        up_diagonal_coord = []
        for x in range(puzzle_width):
            if 0 <= y-x < puzzle_width:
                up_diagonal += p[y-x][x]
                up_diagonal_coord.append([y-x, x])
        if word in up_diagonal or backwards_word in up_diagonal:
            if word in up_diagonal:
                starting_index = up_diagonal.index(word[0])
            else:
                starting_index = up_diagonal.index(word[-1])
            return [up_diagonal_coord[i] for i in range(starting_index, starting_index + len(word))]

    for y in range(-puzzle_width + 1, puzzle_width):
        down_diagonal = ''
        down_diagonal_coord = []
        for x in range(puzzle_width):
            if 0 <= x-y < puzzle_width:
                down_diagonal += p[x-y][x]
                down_diagonal_coord.append([x-y, x])
        if word in down_diagonal or backwards_word in down_diagonal:
            if word in down_diagonal:
                starting_index = down_diagonal.index(word[0])
            else:
                starting_index = down_diagonal.index(word[-1])
            return [down_diagonal_coord[i] for i in range(starting_index, starting_index + len(word))]

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, padx=3, pady=3, bg='white')
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        # Puzzle grid
        self.all_letters = []
        for i in range(len(puzzle)):
            letter_row = []
            for j in range(len(puzzle[0])):
                letter = Label(self, text=puzzle[i][j], font=("Helvetica", "16"), bg='white')
                letter.grid(row=i + 3, column=j)
                letter_row.append([letter])
            self.all_letters.append(letter_row)

        # "Enter word to find" label
        input_section = Label(self, text="ENTER WORD TO FIND", font=("Arial", "12"), bg='white')
        input_section.grid(columnspan=len(puzzle[0]))

        # User entry section
        self.user_word = Entry(self)
        self.user_word.grid(columnspan=len(puzzle[0]), pady=10)

        # Enter Button
        self.enter = Button(self, text="LET'S DO THIS!", command=self.gameplay)
        self.enter.grid(columnspan=len(puzzle[0]))

    def gameplay(self):
        word_to_find = (self.user_word.get()).upper().replace(' ', '')
        self.user_word.delete(0, END)
        word_location = word_locator(puzzle, word_to_find)
        for coord in word_location:
            self.all_letters[coord[0]][coord[1]][0].config(bg='yellow')

app = Application() # Instantiate the application class
app.master.title("Word Search")

photo = tkinter.PhotoImage(file="WordSearchTitle.gif",)
header = tkinter.Label(app, image=photo, bg='white')
header.grid(row=0, column=0, rowspan=2, columnspan=len(puzzle[0]), pady=15)

app.mainloop()