from tkinter import Tk, Label, Entry, StringVar, IntVar
import random
from prompt_library import WORD_BANK


class Word_Generator:
    def __init__(self):
        self.word_bank = WORD_BANK
        self.current_paragraph = random.randint(0,len(self.word_bank)-1)
        self.current_word = -1
        self.total_character_count = 0
        self.total_word_count = 0
        self.correct_word_count = 0
        self.starting_time = 60
        self.elapsed_time = 0

    def get_next_word(self):
        self.current_word += 1
        self.active_word()

    def active_word(self):
        self.displayed_word = self.word_bank[self.current_paragraph].split(" ")[self.current_word]
        word_prompt_var.set(self.displayed_word)

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
        self.get_next_word()
    
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
        word_score_var.set(words_per_minute)

    def update_accuracy(self):
        accuracy = int(round((self.correct_word_count / self.total_word_count) * 100, 0))
        accuracy_var.set(f"{accuracy}")
        
    def timer(self, time, time_elapsed):
        self.elapsed_time = time_elapsed
        timer_var.set(time)
        if time > 0:
            window.after(1000, self.timer, time - 1, time_elapsed + 1)
        elif time == 0:
            print("Time up!") # TODO


word = Word_Generator()


#* ---------- GUI ---------- #
# Window Properties
window = Tk()
window.title("Arya's Typing Speed Tester")
window.config(padx=50, pady=50, bg="beige")

# Title
title_text = Label(text="Arya's Typing Speed Tester")
title_text.config(font="TkMenuFont")
title_text.grid(row=0, columnspan=5)

# Word Prompt
word_prompt_var = StringVar()
word_prompt_var.set("Ready? Hit 'Enter' to Start")
word_prompt_label = Label(window, textvariable=word_prompt_var)
word_prompt_label.config(font="TkMenuFont")
word_prompt_label.grid(row=1, columnspan=5)

# User Input
user_input_var = StringVar()
user_input_label = Entry(window, textvariable=user_input_var)
user_input_label.bind("<space>", word.on_space)
user_input_label.bind("<Return>", word.on_return)
user_input_label.config()
user_input_label.grid(row=2, columnspan=5)

# Timer
timer_var = IntVar()
timer_var.set("-")
timer_label = Label(window, textvariable=timer_var)
timer_label.config()
timer_label.grid(row=3, column=1)

# Word Score
word_score_var = IntVar()
word_score_var.set("-")
word_score_label = Label(window, textvariable=word_score_var)
word_score_label.config()
word_score_label.grid(row=3, column=2)

# Accuracy
accuracy_var = IntVar()
accuracy_var.set("-")
accuracy_label = Label(window, textvariable=accuracy_var)
accuracy_label.config()
accuracy_label.grid(row=3, column=3)

window.mainloop()



# To log keypresses:
# def keypress(key):
#     print(key.char)
# user_input.bind("<Key>", keypress)
