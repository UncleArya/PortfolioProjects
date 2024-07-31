from tkinter import Tk, Canvas, StringVar, Entry, Button, Radiobutton
from tkinter import CENTER, W, E
from PIL import Image, ImageOps
from pathlib import Path


def image_resize():
    file_path = get_file_path()
    width = int(Image.open(file_path).width)
    height = int(Image.open(file_path).height)
    size = get_resize_method(width, height)
    file_name = Path(file_path).stem
    directory = Path(file_path).parent
    with Image.open(file_path) as image:
        ImageOps.contain(image, size).save(f"{directory}/{file_name}-resized.jpg")


def get_file_path():
    return file_path.get()


def get_resize_method(width, height):
    curr_width = width
    curr_height = height
    if resize_method.get() == "Dimension":
        return resize_by_dimensions(curr_width, curr_height)
    else:
        return resize_by_percentage(curr_width, curr_height)


def resize_by_dimensions(curr_width, curr_height):
    width = curr_width
    height = curr_height
    if new_width.get():
        width = int(new_width.get())
    if new_height.get():
        height = int(new_height.get())
    new_size = (width, height)
    return new_size


def resize_by_percentage(curr_width, curr_height):
    percent = float(resize_percentage.get()) / 100
    width = int(curr_width * percent)
    height = int(curr_height * percent)
    new_size = (width, height)
    return new_size


def start():
    """Initialize the GUI"""
    window.mainloop()


# ---------- GUI ---------- #
# Constants
BASE_COLOUR = "#eff1f5"
TEXT_COLOUR = "#4c4f69"
ACCENT_COLOUR = "#9ca0b0"
FONT_FAMILY = "Verdana"
H1_FONT = (FONT_FAMILY, 24, "bold")
H2_FONT = (FONT_FAMILY, 16, "bold")
BODY_FONT = (FONT_FAMILY, 12, "normal")

# Window
window = Tk()
window.title("Arya's Image Resizer")
window.config(padx=0, pady=0, bg=BASE_COLOUR)
window.resizable(width=False, height=False)
window.geometry("500x450")
canvas = Canvas(width=500, height=450, bg=BASE_COLOUR)
canvas.place(x=0, y=0)

# Title
title_label = canvas.create_text(250, 50, anchor=CENTER, text="Image Resizer")
canvas.itemconfig(title_label, font=H1_FONT, fill=TEXT_COLOUR)

# Original File Location
file_path_label = canvas.create_text(55, 100, anchor=W, text="File Path:")
canvas.itemconfig(file_path_label, font=H2_FONT, fill=TEXT_COLOUR)
file_path = StringVar()
file_path_entry = Entry(window, textvariable=file_path)
file_path_entry.config(width=43, font=BODY_FONT)
canvas.create_window(250, 125, anchor=CENTER, window=file_path_entry)

# Radio Buttons
resize_method = StringVar()
resize_by_dimensions_radio = Radiobutton(window, text="Resize by dimension", value="Dimension", variable=resize_method)
resize_by_dimensions_radio.config(font=H2_FONT, fg=TEXT_COLOUR, bg=BASE_COLOUR, highlightthickness=0)
resize_by_dimensions_radio.config(activeforeground=TEXT_COLOUR, activebackground=BASE_COLOUR)
canvas.create_window(50, 175, anchor=W, window=resize_by_dimensions_radio)
resize_by_percentage_radio = Radiobutton(window, text="Resize by percentage", value="Percent", variable=resize_method)
resize_by_percentage_radio.config(font=H2_FONT, fg=TEXT_COLOUR, bg=BASE_COLOUR, highlightthickness=0)
resize_by_percentage_radio.config(activeforeground=TEXT_COLOUR, activebackground=BASE_COLOUR)
canvas.create_window(50, 275, anchor=W, window=resize_by_percentage_radio)

# Resize By Dimensions
new_width_label = canvas.create_text(145, 225, anchor=E, text="Width:")
canvas.itemconfig(new_width_label, font=H2_FONT, fill=TEXT_COLOUR)
new_width = StringVar()
new_width.set("")
new_width_entry = Entry(window, textvariable=new_width)
new_width_entry.config(width=10, font=BODY_FONT)
canvas.create_window(150, 225, anchor=W, window=new_width_entry)

new_height_label = canvas.create_text(345, 225, anchor=E, text="Height:")
canvas.itemconfig(new_height_label, font=H2_FONT, fill=TEXT_COLOUR)
new_height = StringVar()
new_height.set("")
new_height_entry = Entry(window, textvariable=new_height)
new_height_entry.config(width=10, font=BODY_FONT)
canvas.create_window(350, 225, anchor=W, window=new_height_entry)

# Resize by Percentage
resize_percentage_label = canvas.create_text(145, 325, anchor=E, text="Percent:")
canvas.itemconfig(resize_percentage_label, font=H2_FONT, fill=TEXT_COLOUR)
resize_percentage = StringVar()
resize_percentage.set("")
resize_percentage_entry = Entry(window, textvariable=resize_percentage)
resize_percentage_entry.config(width=10, font=BODY_FONT)
canvas.create_window(150, 325, anchor=W, window=resize_percentage_entry)

# Convert Button
convert_button = Button(window, text="Convert", command=image_resize)
convert_button.config(border=3, fg=BASE_COLOUR, bg=ACCENT_COLOUR, font=H2_FONT)
convert_button.config(activebackground=BASE_COLOUR, activeforeground=TEXT_COLOUR)
canvas.create_window(250, 390, anchor=CENTER, window=convert_button)


start()
