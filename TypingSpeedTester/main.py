from tkinter import *
import random
from prompt_library import WORD_BANK


class Word_Generator:
    def __init__(self):
        self.word_bank = WORD_BANK
        self.current_paragraph = random.randint(0,len(self.word_bank)-1)
        self.current_word = -1
        self.leading_word = self.current_word - 1
        self.trailing_word = self.current_word + 1
        self.total_character_count = 0
        self.total_word_count = 0
        self.correct_word_count = 0
        self.starting_time = 60
        self.elapsed_time = 0

    def get_next_word(self):
        self.current_word += 1
        self.trailing_word += 1
        self.leading_word += 1
        self.update_words()

    def active_word(self):
        self.displayed_word = self.word_bank[self.current_paragraph].split(" ")[self.current_word]
        canvas.itemconfig(word_prompt_label, text=self.displayed_word)

    def update_words(self): # FIXME - CLEAN UP THIS
        self.two_words_previous()
        self.one_word_previous()
        self.two_words_upcoming()
        self.one_word_upcoming()
        length_two_previous_words = len(self.word0 + self.word1)
        length_two_next_words = len(self.word3 + self.word4)
        self.displayed_word = self.word_bank[self.current_paragraph].split(" ")[self.current_word]
        max_words_length = max(length_two_previous_words, length_two_next_words)
        blank_word = "".rjust(int(max_words_length/2))
        word0_formatted = self.word0.rjust(max_words_length - len(self.word1))
        word4_formatted = self.word4.ljust(max_words_length - len(self.word3))
        if self.current_word == 0:
            canvas.itemconfig(word_prompt_label, text=f"{blank_word} {blank_word} {self.displayed_word} {self.word3} {word4_formatted}")
        elif self.current_word == 1:
            canvas.itemconfig(word_prompt_label, text=f"{blank_word} {self.word1} {self.displayed_word} {self.word3} {word4_formatted}")
        else:
            canvas.itemconfig(word_prompt_label, text=f"{word0_formatted} {self.word1} {self.displayed_word} {self.word3} {word4_formatted}")
    
    def one_word_upcoming(self):
        self.word3 =  self.word_bank[self.current_paragraph].split(" ")[self.current_word + 1]
    
    def two_words_upcoming(self):
        self.word4 =  self.word_bank[self.current_paragraph].split(" ")[self.current_word + 2]
    
    def one_word_previous(self):
        if self.current_word < 1:
            self.word1 = ""
        else:
            self.word1 =  self.word_bank[self.current_paragraph].split(" ")[self.current_word - 1]
    
    def two_words_previous(self):
        if self.current_word < 2:
            self.word0 = ""
        else:
            self.word0 =  self.word_bank[self.current_paragraph].split(" ")[self.current_word - 2]
    
    def on_space(self, event):
        self.user_input = user_input_var.get()
        self.user_input_no_spaces = user_input_var.get().strip()
        print(self.user_input_no_spaces) #DEBUG
        self.count_characters(self.user_input)
        self.check_accuracy(self.user_input_no_spaces)
        user_input_label.delete(0, "end")
        self.get_next_word()
        
    def on_return(self, event):
        self.timer(self.starting_time, self.elapsed_time)
        user_input_label.delete(0, "end")
        self.get_next_word()
        
    def on_entry_click(self, event):
        if user_input_var.get() != "":
            user_input_label.delete(0, "end")
    
    def count_characters(self, word):
        word_characters = len(word)
        print(word_characters) # DEBUG
        self.total_character_count += word_characters
        self.update_word_score()
        
    def check_accuracy(self, word):
        self.total_word_count += 1
        if self.displayed_word == word:
            self.correct_word_count += 1
            print("Correct") #DEBUG
        else:
            print("Incorrect") #DEBUG
        self.update_accuracy()
            
    def update_word_score(self):
        words_per_minute = int(round((self.total_character_count / 5) / (self.elapsed_time / 60), 0))
        canvas.itemconfig(word_score, text=words_per_minute)

    def update_accuracy(self):
        word_accuracy = int(round((self.correct_word_count / self.total_word_count) * 100, 0))
        canvas.itemconfig(accuracy, text=word_accuracy)
        
    def timer(self, time, time_elapsed):
        self.elapsed_time = time_elapsed
        canvas.itemconfig(timer, text=time)
        if time > 0:
            window.after(1000, self.timer, time - 1, time_elapsed + 1)
        elif time == 0:
            print("Time up!") # TODO


word = Word_Generator()


#* ---------- GUI ---------- #
# Constants
BASE_COLOUR = "#1e1e2e"
BG_DARK = "#313244"
BG_MEDIUM = "#45475a"
BG_LIGHT = "#585b70"
TEXT_COLOUR = "#cdd6f4"
TEXT_ACCENT_COLOUR = "#a6adc8"
INCORRECT_TEXT_COLOUR = "#f38ba8"
CORRECT_TEXT_COLOUR = "#a6e3a1"
H1_FONT = ("Courier", 30, "bold")
H2_FONT = ("Courier", 20, "bold")
H3_FONT = ("Courier", 14, "bold")
BODY_FONT = ("Courier", 16, "normal")

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
canvas.place(x=0,y=0)

# Title
title_text = canvas.create_text(400, 75, anchor=CENTER, text="Arya's Typing Tester")
canvas.itemconfig(title_text, font=H1_FONT, fill=TEXT_COLOUR)

# Word Prompt
word_prompt_label = canvas.create_text(400, 200, anchor=CENTER, text="Ready? Hit 'Enter' Below To Begin!")
canvas.itemconfig(word_prompt_label, font=H2_FONT, fill=TEXT_COLOUR)

# User Input
user_input_var = StringVar()
user_input_var.set("Click here to begin typing")
user_input_label = Entry(window, textvariable=user_input_var)
user_input_label.bind("<space>", word.on_space)
user_input_label.bind("<Return>", word.on_return)
user_input_label.bind("<FocusIn>", word.on_entry_click)
user_input_label.config(bg=BG_LIGHT, width=50, highlightthickness=0, border=1) # UPDATE border=0
user_input_label.config(justify=CENTER, font=BODY_FONT, fg=TEXT_COLOUR)
canvas.create_window(400, 350, window=user_input_label)

# Timer
timer_label = canvas.create_text(150, 475, anchor=CENTER, text="Time Remaining")
canvas.itemconfig(timer_label, font=H3_FONT, fill=TEXT_COLOUR)
timer = canvas.create_text(150, 575, anchor=CENTER, text="--")
canvas.itemconfig(timer, font=H2_FONT, fill=TEXT_COLOUR)

# Word Score
word_score_label = canvas.create_text(400, 475, anchor=CENTER, text="Words Per Minute")
canvas.itemconfig(word_score_label, font=H3_FONT, fill=TEXT_COLOUR)
word_score = canvas.create_text(400, 575, anchor=CENTER, text="--")
canvas.itemconfig(word_score, font=H2_FONT, fill=TEXT_COLOUR)

# Accuracy
accuracy_label = canvas.create_text(650, 475, anchor=CENTER, text="Accuracy (%)")
canvas.itemconfig(accuracy_label, font=H3_FONT, fill= TEXT_COLOUR)
accuracy = canvas.create_text(650, 575, anchor=CENTER, text="--")
canvas.itemconfig(accuracy, font=H2_FONT, fill=TEXT_COLOUR)

window.mainloop()



# To log keypresses:
# def keypress(key):
#     print(key.char)
# user_input.bind("<Key>", keypress)
