from tkinter import Tk, Label, Entry, StringVar


def on_space(event):
    print(typed_input.get().strip())
    user_input.delete(0, "end")


# ---------- GUI ---------- #
# Window Properties
window = Tk()
window.title("Arya's Typing Speed Tester")
window.config(padx=50, pady=50, bg="beige")

# Title
title_text = Label(text="Arya's Typing Speed Tester")
title_text.config(font="TkMenuFont")
title_text.grid(row=0, columnspan=5)

# Word Prompt
prompt_box = Label(text="WORD")
prompt_box.config(font="TkMenuFont")
prompt_box.grid(row=1, columnspan=5)

# User Input
typed_input = StringVar()
user_input = Entry(textvariable=typed_input)
user_input.bind("<space>", on_space)
user_input.config()
user_input.grid(row=2, columnspan=5)

# Timer
timer = Label(text="0")
timer.config()
timer.grid(row=3, column=1)

# Word Score
word_score = Label(text="0")
word_score.config()
word_score.grid(row=3, column=2)

# Accuracy
accuracy = Label(text=0)
accuracy.config()
accuracy.grid(row=3, column=3)

window.mainloop()


# To log keypresses:
# def keypress(key):
#     print(key.char)
# user_input.bind("<Key>", keypress)
