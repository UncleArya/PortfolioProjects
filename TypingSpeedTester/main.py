from tkinter import Tk, Canvas, PhotoImage, StringVar, Entry, Button
from tkinter import CENTER, W, E
import random
from prompt_library import WORD_BANK


# ---------- Program Execution ---------- #
class Typing_Program:
    def __init__(self):
        """Contains the functions required to execute the typing program."""
        self.word_bank = WORD_BANK
        self.starting_time = 60
        self.elapsed_time = 0
        self.timer_running = False

    def start_button(self):
        """Button functionality to start the program. Randomly selects words from the work bank, sets counters to 0, and starts a timer."""
        self.timer_running = True
        if self.elapsed_time == 0:
            self.current_paragraph = random.randint(0, len(self.word_bank) - 1)
            self.current_word_index = -1
            self.total_character_count = 0
            self.total_word_count = 0
            self.correct_word_count = 0
            self.timer(self.starting_time, self.elapsed_time)
            canvas.itemconfig(starting_word_label, text="")
            user_input_label.delete(0, "end")
            self.update_words()

    def reset_button(self):
        """Button functionality to stop/reset the program. Stops and resets the timer, clears GUI elements."""
        self.timer_running = False
        self.starting_time = 60
        self.elapsed_time = 0
        canvas.itemconfig(timer, text="--")
        canvas.itemconfig(word_score, text="--")
        canvas.itemconfig(accuracy, text="--")
        canvas.itemconfig(active_word_label, text="")
        canvas.itemconfig(previous_word_label, text="")
        canvas.itemconfig(next_word_label, text="")
        canvas.itemconfig(starting_word_label, text="Ready? Hit 'Start' To Begin!")
        user_input_label.delete(0, "end")
        user_input_label.config(state="normal")

    def update_words(self):
        """Moves the sentence forward by one word."""
        self.current_word_index += 1
        self.active_word()
        self.previous_word()
        self.next_word()

    def active_word(self):
        """Applies style to active word typist must duplicate."""
        self.displayed_word = self.word_bank[self.current_paragraph].split(" ")[self.current_word_index]
        canvas.itemconfig(active_word_label, text=self.displayed_word)

    def previous_word(self):
        """Applies style to most previous word typist attempted to duplicate."""
        if self.current_word_index < 1:
            self.previous_displayed_word = ""
        else:
            self.previous_displayed_word = self.word_bank[self.current_paragraph].split(" ")[
                self.current_word_index - 1
            ]
        canvas.itemconfig(previous_word_label, text=self.previous_displayed_word)

    def next_word(self):
        """Applies style to next word the typist will be asked to duplicate."""
        current_word_length = len(self.displayed_word)
        new_x_location = ((current_word_length + 1) * 17) + 380
        self.next_displayed_word = self.word_bank[self.current_paragraph].split(" ")[self.current_word_index + 1]
        canvas.coords(next_word_label, new_x_location, 375)
        canvas.itemconfig(next_word_label, text=self.next_displayed_word)

    def on_space(self, event):
        """When user hits space key, the user input is obtained, checked for accuracy, added to words per minute count, and requests next word."""
        if self.timer_running:
            self.user_input = user_input_var.get()
            self.user_input_no_spaces = user_input_var.get().strip()
            self.count_characters(self.user_input)
            self.check_accuracy(self.user_input_no_spaces)
            user_input_label.delete(0, "end")
            self.update_words()

    def on_entry_click(self, event):
        """Clears entry box when cursor is inserted."""
        if user_input_var.get() != "":
            user_input_label.delete(0, "end")

    def count_characters(self, word):
        """Count number of characters in user inputted word."""
        word_characters = len(word)
        self.total_character_count += word_characters

    def check_accuracy(self, word):
        """Check if user inputted word matches the requested word."""
        self.total_word_count += 1
        if self.displayed_word == word:
            self.correct_word_count += 1
            canvas.itemconfig(previous_word_label, fill=CORRECT_TEXT_COLOUR)
        else:
            canvas.itemconfig(previous_word_label, fill=INCORRECT_TEXT_COLOUR)
        self.update_accuracy()

    def update_word_score(self):
        """Update UI element for words per minute calculation."""
        if self.total_word_count > 0:
            words_per_minute = int(round((self.total_character_count / 5) / (self.elapsed_time / 60), 0))
            canvas.itemconfig(word_score, text=words_per_minute)

    def update_accuracy(self):
        """Update UI element for user word accuracy"""
        word_accuracy = int(round((self.correct_word_count / self.total_word_count) * 100, 0))
        canvas.itemconfig(accuracy, text=word_accuracy)

    def timer(self, time, time_elapsed):
        """Timer mechanism for typing program"""
        if self.timer_running:
            self.elapsed_time = time_elapsed
            canvas.itemconfig(timer, text=time)
            self.update_word_score()
            if time > 0:
                window.after(1000, self.timer, time - 1, time_elapsed + 1)
            elif time == 0:
                self.timer_running = False
                user_input_label.config(state="disabled")
                canvas.itemconfig(active_word_label, text="")
                canvas.itemconfig(previous_word_label, text="")
                canvas.itemconfig(next_word_label, text="")
                canvas.itemconfig(starting_word_label, text="Done! Hit 'Reset' To Go Again!")


run = Typing_Program()

# ---------- GUI ---------- #
# Constants
BASE_COLOUR = "#1e1e2e"
BG_DARK = "#313244"
BG_MEDIUM = "#45475a"
BG_LIGHT = "#585b70"
TEXT_COLOUR = "#cdd6f4"
ACTIVE_TEXT_COLOUR = "#b4befe"
TEXT_ACCENT_COLOUR = "#9399b2"
INCORRECT_TEXT_COLOUR = "#f38ba8"
CORRECT_TEXT_COLOUR = "#a6e3a1"
H1_FONT = ("Courier", 30, "bold")
H2_FONT = ("Courier", 20, "bold")
H3_FONT = ("Courier", 14, "bold")
H4_FONT = ("Courier", 12, "normal")
BODY_FONT = ("Courier", 20, "normal")

# Window Properties
window = Tk()
window.title("Arya's Typing Tester")
window.config(padx=0, pady=0, bg="")
window.resizable(width=False, height=False)
window.geometry("800x800")
background_image = PhotoImage(file="./assets/background.png")
canvas = Canvas(width=800, height=800)
canvas.create_image(400, 400, image=background_image)
canvas.config(highlightthickness=0, borderwidth=0)
canvas.place(x=0, y=0)

# Title
title_text = canvas.create_text(400, 100, anchor=CENTER, text="Arya's Typing Tester")
canvas.itemconfig(title_text, font=H1_FONT, fill=TEXT_COLOUR)

# Word Prompt
active_word_label = canvas.create_text(380, 375, anchor=W, text="")
canvas.itemconfig(active_word_label, font=H2_FONT, fill=ACTIVE_TEXT_COLOUR)
previous_word_label = canvas.create_text(360, 375, anchor=E, text="")
canvas.itemconfig(previous_word_label, font=H2_FONT, fill=TEXT_COLOUR)
next_word_label = canvas.create_text(380, 375, anchor=W, text="")
canvas.itemconfig(next_word_label, font=H2_FONT, fill=TEXT_ACCENT_COLOUR)
starting_word_label = canvas.create_text(400, 375, anchor=CENTER, text="Ready? Hit 'Start' To Begin!")
canvas.itemconfig(starting_word_label, font=H2_FONT, fill=TEXT_COLOUR)

# User Input
user_input_var = StringVar()
user_input_var.set("Place Cursor Here")
user_input_label = Entry(window, textvariable=user_input_var)
user_input_label.bind("<space>", run.on_space)
user_input_label.bind("<FocusIn>", run.on_entry_click)
user_input_label.config(bg=BG_LIGHT, width=40, highlightthickness=0, border=0)
user_input_label.config(justify=CENTER, font=BODY_FONT, fg=TEXT_COLOUR, insertbackground=TEXT_COLOUR)
canvas.create_window(400, 500, window=user_input_label)

# Timer
timer_label = canvas.create_text(150, 602, anchor=CENTER, text="Time Remaining")
canvas.itemconfig(timer_label, font=H3_FONT, fill=TEXT_COLOUR)
timer = canvas.create_text(150, 705, anchor=CENTER, text="--")
canvas.itemconfig(timer, font=H1_FONT, fill=TEXT_COLOUR)

# Word Score
word_score_label = canvas.create_text(400, 602, anchor=CENTER, text="Words Per Minute")
canvas.itemconfig(word_score_label, font=H3_FONT, fill=TEXT_COLOUR)
word_score = canvas.create_text(400, 705, anchor=CENTER, text="--")
canvas.itemconfig(word_score, font=H1_FONT, fill=TEXT_COLOUR)

# Accuracy
accuracy_label = canvas.create_text(650, 602, anchor=CENTER, text="Accuracy (%)")
canvas.itemconfig(accuracy_label, font=H3_FONT, fill=TEXT_COLOUR)
accuracy = canvas.create_text(650, 705, anchor=CENTER, text="--")
canvas.itemconfig(accuracy, font=H1_FONT, fill=TEXT_COLOUR)

# Start Button
start_button = Button(text="START", command=run.start_button)
start_button.config(bg=BG_LIGHT, padx=19, pady=9, highlightthickness=0, border=0, activebackground=BG_LIGHT)
start_button.config(fg=ACTIVE_TEXT_COLOUR, activeforeground=TEXT_ACCENT_COLOUR, font=H3_FONT)
canvas.create_window(100, 204, window=start_button)

# Reset Button
reset_button = Button(text="RESET", command=run.reset_button)
reset_button.config(bg=BG_LIGHT, padx=19, pady=9, highlightthickness=0, border=0, activebackground=BG_LIGHT)
reset_button.config(fg=ACTIVE_TEXT_COLOUR, activeforeground=TEXT_ACCENT_COLOUR, font=H3_FONT)
canvas.create_window(100, 279, window=reset_button)

# Instructions
instructions_label = canvas.create_text(475, 195, anchor=CENTER, text="~~~ Instructions ~~~")
canvas.itemconfig(instructions_label, font=H3_FONT, fill=TEXT_ACCENT_COLOUR)
instructions_line_1 = canvas.create_text(210, 220, anchor=W, text="~ Place cursor in centre box and hit 'Start' button")
canvas.itemconfig(instructions_line_1, font=H4_FONT, fill=TEXT_ACCENT_COLOUR)
instructions_line_2 = canvas.create_text(210, 240, anchor=W, text="~ Timer will run for 60 seconds")
canvas.itemconfig(instructions_line_2, font=H4_FONT, fill=TEXT_ACCENT_COLOUR)
instructions_line_3 = canvas.create_text(210, 260, anchor=W, text="~ Hitting 'Space' moves to next word")
canvas.itemconfig(instructions_line_3, font=H4_FONT, fill=TEXT_ACCENT_COLOUR)
instructions_line_4 = canvas.create_text(210, 280, anchor=W, text="~ Hit 'Reset' button to stop and go again")
canvas.itemconfig(instructions_line_4, font=H4_FONT, fill=TEXT_ACCENT_COLOUR)

window.mainloop()
