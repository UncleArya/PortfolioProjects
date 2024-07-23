from tkinter import *
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
        # word_prompt_var.set(self.displayed_word)
        canvas.itemconfig(word_prompt_label, text=self.displayed_word)

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
        # word_score_var.set(words_per_minute)
        canvas.itemconfig(word_score_label, text=words_per_minute)

    def update_accuracy(self):
        accuracy = int(round((self.correct_word_count / self.total_word_count) * 100, 0))
        # accuracy_var.set(f"{accuracy}")
        canvas.itemconfig(accuracy_label, text=accuracy)
        
    def timer(self, time, time_elapsed):
        self.elapsed_time = time_elapsed
        # timer_var.set(time)
        canvas.itemconfig(timer_label, text=time)
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
H1_FONT = ("TkFixedFont", 24, "bold")
H2_FONT = ("TkFixedFont", 20, "bold")
BODY_FONT = ("TkFixedFont", 16, "normal")

# Window Properties
window = Tk()
window.title("Arya's Typing Speed Tester")
window.config(padx=0, pady=0, bg="")
window.resizable(width=False, height=False)
window.geometry("800x800")
background_image = PhotoImage(file="./assets/background.png")
# background_label = Label(window, image=background_image)
# background_label.config(highlightthickness=0, borderwidth=0)
# background_label.place(x=0, y=0)
canvas = Canvas(width=800, height=800)
canvas.create_image(400, 400, image=background_image)
canvas.config(highlightthickness=0, borderwidth=0)
canvas.place(x=0,y=0)

# Title
# title_frame = Frame(window, width=700, height=50)
# title_frame.config(bg=BASE_COLOUR)
# title_frame.place(x=50, y=50)
# title_text = Label(title_frame, text="Arya's Typing Speed Tester")
# title_text.config(font="TkMenuFont", bg=BASE_COLOUR, fg=TEXT_COLOUR)
# title_text.place(relx=0.5, rely=0.5, anchor=CENTER)
title_text = canvas.create_text(400, 75, anchor=CENTER, text="Arya's Typing Speed Tester")
canvas.itemconfig(title_text, font=H1_FONT, fill=TEXT_COLOUR)

# Word Prompt
# word_prompt_var = StringVar()
# word_prompt_var.set("Ready?")
# word_prompt_frame = Frame(window, width=700, height=100)
# word_prompt_frame.config(bg="")
# word_prompt_frame.place(x=50, y=150)
# word_prompt_label = Label(word_prompt_frame, textvariable=word_prompt_var)
# word_prompt_label.config(font="TkMenuFont", bg=BG_DARK, fg=TEXT_COLOUR)
# word_prompt_label.place(relx=0.5, rely=0.5, anchor=CENTER)
word_prompt_label = canvas.create_text(400, 200, anchor=CENTER, text="Ready?")
canvas.itemconfig(word_prompt_label, font=H2_FONT, fill=TEXT_COLOUR)

# User Input
user_input_var = StringVar()
user_input_var.set("Hit 'Enter' to Start!")
user_input_label = Entry(window, textvariable=user_input_var)
user_input_label.bind("<space>", word.on_space)
user_input_label.bind("<Return>", word.on_return)
user_input_label.config(bg=BG_LIGHT, width=50, highlightthickness=0, border=1) # UPDATE border=0
user_input_label.config(justify=CENTER, font=BODY_FONT, fg=TEXT_COLOUR)
# user_input_label.grid(row=2, columnspan=5)
canvas.create_window(400, 350, window=user_input_label)

# Timer
# timer_var = IntVar()
# timer_var.set(60)
# timer_label = Label(window, textvariable=timer_var)
# timer_label.config()
# timer_label.grid(row=3, column=1)
timer_label = canvas.create_text(150, 575, anchor=CENTER, text="--")
canvas.itemconfig(timer_label, font=H2_FONT, fill=TEXT_COLOUR)

# Word Score
# word_score_var = IntVar()
# word_score_var.set(0)
# word_score_label = Label(window, textvariable=word_score_var)
# word_score_label.config()
# word_score_label.grid(row=3, column=2)
word_score_label = canvas.create_text(400, 575, anchor=CENTER, text="--")
canvas.itemconfig(word_score_label, font=H2_FONT, fill=TEXT_COLOUR)

# Accuracy
# accuracy_var = IntVar()
# accuracy_var.set(0)
# accuracy_label = Label(window, textvariable=accuracy_var)
# accuracy_label.config()
# accuracy_label.grid(row=3, column=3)
accuracy_label = canvas.create_text(650, 575, anchor=CENTER, text="--")
canvas.itemconfig(accuracy_label, font=H2_FONT, fill=TEXT_COLOUR)

window.mainloop()



# To log keypresses:
# def keypress(key):
#     print(key.char)
# user_input.bind("<Key>", keypress)
