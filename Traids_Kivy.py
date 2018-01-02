"""
Program Description:

This program will randomly generate triads across a guitar fret board
on the first string set and will loop until the user exits the program.

Created by: Shaun Shippey
Date created 08/24/17
Date last modified: 9/16/17
"""

from random import randint

from tkinter import *


class Fretboard(Frame):

    canvas = 0
    fretboard_image = [0, 0, 0, 0, 0, 0]

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Fretboard")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)

        x_org = 20
        y_org = 25
        length = 480
        width = 200

        self.canvas.create_rectangle(x_org, y_org, length + x_org, width + y_org)
        # draw horizontal lines on the fretboard
        for i in range(1, 5):
            self.canvas.create_line(x_org, y_org + 40 * i, 480 + x_org, y_org + 40 * i)
        # draw vertical lines on the fretboard
        for i in range(1, 12):
            self.canvas.create_line(20 + 40 * i, 25, 20 + 40 * i, width + y_org)

            self.canvas.pack(fill=BOTH, expand=1)

        string_labels = ['E', 'B', 'G', 'D', 'A', 'E']
        for i in range(0, 6):
            canvas_id = self.canvas.create_text(x_org - 15, (y_org - 12) + 40 * i, anchor="nw")
            self.canvas.itemconfig(canvas_id, text=string_labels[i])

        for i in range(1, 13):
            canvas_id = self.canvas.create_text(x_org + 40 * i, width + y_org, anchor="n")
            self.canvas.itemconfig(canvas_id, text=i)

    # accepts either note names or note numbers
    def display(self, notes, string_set):
        # store the locations passed to the function to the first string set
        display_info = ['x', 'x', 'x', str(notes[0]), str(notes[1]), str(notes[2])]

        # rotate the the appropriate string set
        display_info = rotate(display_info, string_set)

        # display dots to indicate chord
        for i in range(0, 6):
            # if there are existing images clear them from the fretboard
            self.canvas.delete(self.fretboard_image[i])

            if display_info[i].isdigit():
                self.fretboard_image[i] = self.canvas.create_oval(15 + 40*eval(display_info[i]), (20 + 200) - 40 * i,
                                                                  25 + 40*eval(display_info[i]), (30 + 200) - 40 * i,
                                                                  fill="red")
            else:
                # place 'x' at the fret location
                self.fretboard_image[i] = 0
                pass


class AppButtons:
    root_dropdown_data = "RANDOM"
    triad_type_dropdown_data = "RANDOM"
    inversion_dropdown_data = "RANDOM"
    string_set_dropdown_data = "RANDOM"

    def __init__(self, master, fretboard, triad_info, option_info):
        self.fretboard = fretboard
        self.triad_info = triad_info
        self.option_info = option_info

        self.frame = Frame(master)
        self.frame.pack()

        self.root_data = StringVar(self.frame)
        self.root_data.set(self.root_dropdown_data)  # default value

        self.triad_type_data = StringVar(self.frame)
        self.triad_type_data.set(self.triad_type_dropdown_data)  # default value

        self.inversion_data = StringVar(self.frame)
        self.inversion_data.set(self.inversion_dropdown_data)  # default value

        self.string_set_data = StringVar(self.frame)
        self.string_set_data.set(self.string_set_dropdown_data)  # default value

        Label(self.frame, text="Root").grid(row=0, column=0)
        self.root_list = ["RANDOM",
                          "C", "F", "Bf",
                          "Ef", "Af", "Df",
                          "Fs", "B", "E",
                          "A", "D", "G"]
        root_button_options = OptionMenu(self.frame, self.root_data, *self.root_list, command=self.store_root)
        root_button_options.config(width=10)
        root_button_options.grid(row=1, column=0)

        self.triad_list = ["RANDOM",
                           "MAJOR",
                           "MINOR",
                           "DIMINISHED",
                           "AUGMENTED"]

        Label(self.frame, text="Triad Type").grid(row=0, column=1)
        triad_type_options = OptionMenu(self.frame, self.triad_type_data, *self.triad_list, command=self.store_triad_type)
        triad_type_options.config(width=10)
        triad_type_options.grid(row=1, column=1)

        self.inversion_list = ["RANDOM",
                               0,
                               1,
                               2]

        Label(self.frame, text="Inversion").grid(row=3, column=0)
        inversion_options = OptionMenu(self.frame, self.inversion_data, *self.inversion_list, command=self.store_inversion)
        inversion_options.config(width=10)
        inversion_options.grid(row=4, column=0)

        self.string_set_list = ["RANDOM",
                                0,
                                1,
                                2,
                                3]

        Label(self.frame, text="String Set").grid(row=3, column=1)
        string_set_options = OptionMenu(self.frame, self.string_set_data, *self.string_set_list, command=self.store_string_set)
        inversion_options.config(width=10)
        string_set_options.grid(row=4, column=1)

        self.string_answerButton = Button(self.frame, text="Answer", width=14, command=self.display_answer)
        self.string_answerButton.grid(row=0, column=3, padx=20)

        self.answer_root = Label(self.frame,          text="      Root: NA")
        self.answer_root.grid(row=1, column=3)
        self.answer_triad_type = Label(self.frame,    text="      Type: NA")
        self.answer_triad_type.grid(row=2, column=3)
        self.answer_inversion = Label(self.frame,     text=" Inversion: NA")
        self.answer_inversion.grid(row=3, column=3)
        self.answer_string_set = Label(self.frame,    text="String set: NA")
        self.answer_string_set.grid(row=4, column=3)

        self.display_triadButton = Button(self.frame, text="Display Triad", width=14, command=self.display_button)
        self.display_triadButton.grid(row=0, column=4, padx=20)

        self.quitButton = Button(self.frame, text="Quit", width=14, command=self.frame.quit)
        self.quitButton.grid(row=5, column=4)

    def store_root(self, root):
        self.root_dropdown_data = root

    def store_triad_type(self, triad_type):
        self.triad_type_dropdown_data = triad_type

    def store_string_set(self, string_set):
        self.string_set_dropdown_data = string_set

    def store_inversion(self, inversion):
        self.inversion_dropdown_data = inversion

    def display_answer(self):
        try:
            self.answer_root.config(text="Root: " + str(self.triad_info.root))
            self.answer_triad_type.config(text="Type: " + self.triad_info.type)
            self.answer_inversion.config(text="Inversion: " + str(self.triad_info.inversion))
            self.answer_string_set.config(text="String set: " + str(self.triad_info.string_set))
        except AttributeError:
            pass

    def display_button(self):

        # clear the answer when the display button is pressed
        self.answer_root.config(text="Root: ")
        self.answer_triad_type.config(text="Type: ")
        self.answer_inversion.config(text="Inversion: ")
        self.answer_string_set.config(text="String set: ")

        # roll the dice for a new triad if set to "RANDOM"
        if self.root_dropdown_data == "RANDOM":
            self.triad_info.root = self.root_list[randint(1, 12)]
        else:
            self.triad_info.root = self.root_dropdown_data
        if self.inversion_dropdown_data == "RANDOM":
            self.triad_info.inversion = self.triad_info.inversion_dropdown_data = randint(0, 2)
        else:
            self.triad_info.inversion = self.inversion_dropdown_data
        if self.triad_type_dropdown_data == "RANDOM":
            self.triad_info.type = triad_types[randint(0, 3)]
        else:
            self.triad_info.type = self.triad_type_dropdown_data
        if self.string_set_dropdown_data == "RANDOM":
            self.triad_info.string_set = randint(0, 3)
        else:
            self.triad_info.string_set = self.string_set_dropdown_data

        self.triad_info.notes = get_triad(self.triad_info.root, self.triad_info.type, self.triad_info.inversion)
        self.triad_info.note_numbers = get_note_numbers(self.triad_info.notes, self.triad_info.string_set)

        # # display the new triad
        self.fretboard.display(self.triad_info.note_numbers, self.triad_info.string_set)


triad_types = ["MAJOR", "MINOR", "DIMINISHED", "AUGMENTED"]


# this class holds all the information necessary for displaying triads
class TriadInfo:

    def __init__(self):
        self.note_numbers = [5, 5, 4]
        self.string_set = 0
        self.inversion = 0
        self.notes = ['x', 'x', 'x', 'C', 'E', 'G']
        self.root = "C"
        self.type = "MAJOR"

    # flags for Mode == 2 random generation
    random_root = 0
    random_string_set = 0
    random_inversion = 0

    def get_root_from_user(self):
        self.root = input("Select root (0-33 in increments of 3): ")
        if self.root.isdigit():
            if eval(self.root) < 0 or eval(self.root) > 33 or (
                            eval(self.root) % 3 != 0):
                print("Invalid selection, please enter valid selection.")
                self.get_root_from_user()
            else:
                if self.root != "":
                    print("Invalid selection, please enter valid selection.")
                    self.get_root_from_user()

        return self.root

    def get_string_set_from_user(self):
        self.string_set = input("Select string-set (0-3): ")
        if self.string_set.isdigit():
            if eval(self.string_set) < 0 or eval(self.string_set) > 3:
                print("Invalid selection, please enter valid selection.")
                self.get_string_set_from_user()
        else:  # test for character
            if self.string_set != "":
                print("Invalid selection, please enter valid selection.")
                self.get_string_set_from_user()

        return self.string_set

    def get_inversion_from_user(self):
        self.inversion = input("Select inversion (0-2): ")
        if self.inversion == "":
            pass
        elif eval(self.inversion) < 0 or eval(self.inversion) > 2:  # or isnotblank(TriadInfo.inversion):
            print("Invalid selection, please enter valid selection.")
            self.get_inversion_from_user()

        return self.inversion

    def get_triad_type_from_user(self):
        self.type = input("MAJOR, MINOR, DIMINISHED or AUGMENTED?: ")
        if self.type == "":
            self.type = "RANDOM"
        elif self.type not in triad_types:
            print("Invalid selection, please enter valid selection.")
            self.get_triad_type_from_user()

        return self.type


class OptionInfo:
    def __init__(self):
        self.option = '1'
        self.mode = '1'
        self.toggle_display = 0

    def get_option_from_user(self):
        self.option = input("Enter option: ")

        return self.option


def rotate(l, n):
    return l[n:] + l[:n]


def get_triad(root, chord_type, inversion):
    # each triad going backwards through the circle of 5ths

    root_chart = ['C', 'F', 'Bf', 'Ef', 'Af', 'Df', 'Fs', 'B', 'E', 'A', 'D', 'G']

    triad_chart = ['C', 'E', 'G',
                   'F', 'A', 'C',
                   'Bf', 'D', 'F',
                   'Ef', 'G', 'Bf',
                   'Af', 'C', 'Ef',
                   'Df', 'F', 'Af',
                   'Fs', 'As', 'Cs',
                   'B', 'Ds', 'Fs',
                   'E', 'Gs', 'B',
                   'A', 'Cs', 'E',
                   'D', 'Fs', 'A',
                   'G', 'B', 'D']

    # if the root comes in as a character convert it to a digit
    if isinstance(root, str):
        root_index = root_chart.index(root)
        root_index = root_index * 3
    # if the root comes in as an integer go ahead and store it
    else:
        root_index = root
    # store triad from array
    triad = triad_chart[root_index:root_index + 3]
    # modify triad for chord_type
    if chord_type == "MAJOR":
        pass

    elif chord_type == "MINOR" or chord_type == "DIMINISHED":

        if len(triad[1]) == 1:
            triad[1] = triad[1] + "f"  # make 3rd flat

        elif len(triad[1]) == 2:
            triad[1] = triad[1].replace("s", "")  # make 3rd natural

        if chord_type == "DIMINISHED":

            if len(triad[2]) == 1:
                triad[2] = triad[2] + "f"  # make 5th flat

            elif len(triad[2]) == 2:
                if 's' in triad[2]:  # make 5th natural or double-flat
                    triad[2] = triad[2].replace("s", "")
                if 'f' in triad[2]:
                    triad[2] = triad[2] + "f"

    elif chord_type == "AUGMENTED":
        if len(triad[2]) == 1:  # if the 3rd note in triad is natural
            triad[2] = triad[2] + "s"  # make 5th sharp
        elif len(triad[2]) == 2:

            if 'f' in triad[2]:  # if the 5th is flat
                triad[2] = triad[2].replace("f", "")  # remove the flat from the 5th (sharp the note)
            if 's' in triad[2]:  # if the 5th is sharp
                triad[2] = triad[2] + "s"  # add another sharp to 5th

    # rotate the triad to get the correct ordering for the inversion
    if inversion == 0:
        triad = rotate(triad, 0)

    elif inversion == 1:
        triad = rotate(triad, 1)

    elif inversion == 2:
        triad = rotate(triad, 2)

    return triad


def get_note_numbers(triad, string_set):
    fretboard_notes = [['E', 'F', 'Fs', 'G', 'Gs', 'A', 'As', 'B', 'C', 'Cs', 'D', 'Ds'],
                       ['B', 'C', 'Cs', 'D', 'Ds', 'E', 'F', 'Fs', 'G', 'Gs', 'A', 'As'],
                       ['G', 'Gs', 'A', 'As', 'B', 'C', 'Cs', 'D', 'Ds', 'E', 'F', 'Fs'],
                       ['D', 'Ds', 'E', 'F', 'Fs', 'G', 'Gs', 'A', 'As', 'B', 'C', 'Cs'],
                       ['A', 'As', 'B', 'C', 'Cs', 'D', 'Ds', 'E', 'F', 'Fs', 'G', 'Gs'],
                       ['E', 'F', 'Fs', 'G', 'Gs', 'A', 'As', 'B', 'C', 'Cs', 'D', 'Ds']]

    # blank list to hold the strings in the string set
    strings = []

    for i in range(len(triad) - 1 + string_set, string_set - 1, -1):
        strings.append(i)

    # blank list to hold the notes on the strings of the string set
    notes = []

    # for each note in the chord store it to a array of size of the chord
    for i in range(len(triad)):
        # if the note is natural just go ahead and store it
        if len(triad[i]) == 1:
            notes.append(fretboard_notes[strings[i]].index(triad[i]))
        # if there are accidentals we need to store them to the triad_chart
        else:
            # if there is a single sharp, just in case the the sharp note is not already in the
            # fretboard chart (such as, B# or E#), replace the note in the chart with the
            # note from the triad
            if triad[i].count('s') == 1:
                # remove the sharp from the triad
                triad[i] = triad[i].replace("s", "")
                # replace the note at the location of the sharp with the sharp note on the fretboard
                fretboard_notes[strings[i]][(fretboard_notes[strings[i]].index(triad[i]) + 1) % 12] = triad[i] + "s"
                # put the sharp back in the triad
                triad[i] = triad[i] + "s"
                # store the note fretboard location of the triad note
                notes.append(fretboard_notes[strings[i]].index(triad[i]))

            # if there is a single flat replace the respective sharp in the chord chart
            # in the triad chart
            elif triad[i].count('f') == 1:
                # remove the flat from the triad
                triad[i] = triad[i].replace("f", "")
                # replace the flat with a sharp on the fretboard
                fretboard_notes[strings[i]][fretboard_notes[strings[i]].index(triad[i]) - 1] = triad[i] + "f"
                # put the flat back in the triad
                triad[i] = triad[i] + "f"
                # store the note fretboard location of the triad note
                notes.append(fretboard_notes[strings[i]].index(triad[i]))

            # if there are two flat or sharp, replace the necessary note
            # in the triad chart
            if triad[i].count('s') == 2:
                # remove the sharps from the triad
                triad[i] = triad[i].replace("ss", "")
                # replace the single sharp with a double sharp in the fretboard chart
                fretboard_notes[strings[i]][(fretboard_notes[strings[i]].index(triad[i]) + 2) % 12] = triad[i] + "ss"
                # put the double sharp back into the triad
                triad[i] = triad[i] + "ss"
                # store the note's fretboard location on the triad note
                notes.append(fretboard_notes[strings[i]].index(triad[i]))

            elif triad[i].count('f') == 2:
                # remove the flat from the triad
                triad[i] = triad[i].replace("ff", "")
                # replace the single flat with a double flat in the fretboard chart
                fretboard_notes[strings[i]][fretboard_notes[strings[i]].index(triad[i]) - 2] = triad[i] + "ff"
                # put the double sharp back into the triad
                triad[i] = triad[i] + "ff"
                # store the note's fretboard location on the triad note
                notes.append(fretboard_notes[strings[i]].index(triad[i]))

    return notes


def display_on_fretboard(notes, string_set):
    # if necessary convert 's' and 'f' characters to flat sharp symbols
    for i in range(len(notes)):
        if type(notes[i]) is str:
            while notes[i].count('f') != 0:
                notes[i] = notes[i].replace("f", u'\u266D')
            while notes[i].count('s') != 0:
                notes[i] = notes[i].replace("s", '#')

    # store the locations passed to the function to the first string set
    display_info = ['x', 'x', 'x', str(notes[0]), str(notes[1]), str(notes[2])]

    # rotate the the appropriate string set
    display_info = rotate(display_info, string_set)
    for i in range(0, len(display_info)):
        print('{:>5}'.format(display_info[i]), end="")

    print()


def print_string_names():
    print('{:>5}'.format('E') + '{:>5}'.format('A') + '{:>5}'.format('D')
          + '{:>5}'.format('G') + '{:>5}'.format('B') + '{:>5}'.format('E'))


def print_menu():
    print("\nThis program will generate triads across a guitar fretboard.\n"
          "Please see the list of options below for program functionality.")

    print("___________________________________________________________\n"
          "Options:\n\n"

          "Y = Yes     : Display the new triad\n"
          "N = No      : Exit the program\n"
          "A = Answer  : Display the notes for the displayed triad\n\n"
          "T = Toggle  : Toggle between displaying numbers with notes\n"
          "            : as answers or displaying notes with numbers as \n"
          "            : answers.\n\n"

          "M = Mode    : Alter generation of chords displayed\n"
          "            : Modes:\n"
          "            :        1. Random\n"
          "            :        2. User selected criteria\n"
          "___________________________________________________________")


def process_option(option_info, triad_info):
    # if mode is 1 then use random number generation for everything
    if option_info.option == "Y" or option_info.option == "":
        if option_info.mode == '1':
            # roll the dice for a new triad
            triad_info.root = randint(0, 11) * 3
            triad_info.string_set = randint(0, 3)
            triad_info.inversion = randint(0, 2)
            triad_info.type = triad_types[randint(0, 3)]

            triad_info.notes = get_triad(triad_info.root, triad_info.type, triad_info.inversion)
            triad_info.note_numbers = get_note_numbers(triad_info.notes, triad_info.string_set)

            # display the new triad
            print_string_names()
            if option_info.toggle_display == 0:
                display_on_fretboard(triad_info.note_numbers, triad_info.string_set)
            else:
                display_on_fretboard(triad_info.notes, triad_info.string_set)
            print()

        elif option_info.mode == '2':
            # use user defined settings, if the user has not entered a setting randomly generate the
            # parameter
            if triad_info.root == "" or triad_info.random_root == 1:
                triad_info.root = randint(0, 11) * 3
                triad_info.random_root = 1
            if triad_info.string_set == "" or triad_info.random_string_set == 1:
                triad_info.string_set = randint(0, 3)
                triad_info.random_string_set = 1
            if triad_info.inversion == "" or triad_info.random_inversion == 1:
                triad_info.inversion = randint(0, 2)
                triad_info.random_inversion = 1
            if triad_info.type == "RANDOM":
                triad_info.type = triad_types[randint(0, 3)]
                triad_info.notes = get_triad(triad_info.root, triad_info.type, triad_info.inversion)
            else:
                triad_info.notes = get_triad(triad_info.root, triad_info.type, triad_info.inversion)

            # we have all the information we need in the format that we need them, go ahead and get the note
            # locations
            triad_info.note_numbers = get_note_numbers(triad_info.notes, triad_info.string_set)

            # display the new triad
            print_string_names()
            if option_info.toggle_display == 0:
                display_on_fretboard(triad_info.note_numbers, triad_info.string_set)
            else:
                display_on_fretboard(triad_info.notes, triad_info.string_set)
            print()

    # for exiting the program
    elif option_info.option == "N":
        exit()  # terminate the program

    # for displaying the answer
    elif option_info.option == "A":
        # display the answer
        if option_info.toggle_display == 0:
            if triad_info.notes != "":
                display_on_fretboard(triad_info.notes, triad_info.string_set)
                print("root:", triad_info.root)
                print("type:", triad_info.type)
                print("string set:", triad_info.string_set)
                print("inversion:", triad_info.inversion)
            else:
                print("You dope! You need to generate a triad first before displaying "
                      "the answer!")
        else:
            if triad_info.notes != "":
                display_on_fretboard(triad_info.note_numbers, triad_info.string_set)
                print("root:", triad_info.root)
                print("type:", triad_info.type)
                print("string set:", triad_info.string_set)
                print("inversion:", triad_info.inversion)

            else:
                print("You dope! You need to generate a triad first before displaying "
                      "the answer!")

    elif option_info.option == "T":
        # toggle displaying notes first with numbers as answers vs displaying
        # numbers first and notes as answers
        OptionInfo.toggle_display ^= 1

    # for changing the mode
    elif option_info.option == "M":

        # prompt user for mode setting
        option_info.mode = input("Please enter mode (1-2): ")
        while not (OptionInfo.mode == '1' or OptionInfo.mode == '2'):
            print("Invalid selection, please enter valid selection.")
            OptionInfo.mode = input("Please enter mode (1-2): ")

        if option_info.mode == '1':
            # confirm to the user that the mode has been updated
            print("Mode updated.")
            print("Mode = 1     : Random")
            # go back to main
            main()

        elif option_info.mode == '2':
            # confirm to the user that the mode has been updated
            print("\nMode updated.")
            print("Mode = 2     : User selected criteria\n")

            # prompt user for triad information
            print("Please enter information for triad generation.\n"
                  "Any fields left blank will be randomly generated.\n")

            # get necessary triad input from user
            triad_info.get_root_from_user()
            if triad_info.root.isdigit():
                print("Root:", triad_info.root)
            else:
                print("Root: RANDOM", )

            triad_info.get_string_set_from_user()
            if triad_info.string_set.isdigit():
                print("String set:", triad_info.string_set)
            else:
                print("String set: RANDOM")

            triad_info.get_inversion_from_user()
            if triad_info.inversion.isdigit():
                print("Inversion:", triad_info.inversion)
            else:
                print("Inversion: RANDOM")

            triad_info.get_triad_type_from_user()
            if triad_info.type == "":
                print("Triad Type: RANDOM", triad_info.type)
            else:
                print("Triad Type:", triad_info.type)

    elif option_info.option == "ALL":
        print_string_names()
        for string_set in range(0, 4):
            print("string set: ", string_set)
            for root in range(0, 36, 3):
                print("root: ", root)
                for inversion in range(0, 3):
                    print("inversion: ", inversion)
                    for triad_type in range(0, 4):
                        print("type:", triad_types[triad_type])
                        triad_info.root = root
                        triad_info.string_set = string_set
                        triad_info.inversion = inversion
                        triad_info.type = triad_types[triad_type]
                        triad_info.notes = get_triad(triad_info.root, triad_info.type, triad_info.inversion)
                        triad_info.note_numbers = get_note_numbers(triad_info.notes, triad_info.string_set)
                        display_on_fretboard(triad_info.note_numbers, triad_info.string_set)
                        display_on_fretboard(triad_info.notes, triad_info.string_set)

    else:
        print("Invalid option, please enter a valid option")
        option_info.option = input("Enter option: ")
        process_option(option_info, triad_info)


def main():
    root = Tk()

    triad_info = TriadInfo
    option_info = OptionInfo
    fretboard = Fretboard()
    AppButtons(root, fretboard, triad_info, option_info)

    root.geometry("520x455+300+300")

    root.mainloop()


if __name__ == '__main__':
    main()
