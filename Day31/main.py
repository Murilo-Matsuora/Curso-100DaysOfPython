from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
import os
# C:\Users\muril\Documents\Meus\Programas\Cursos\Udemy-Python

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
TEXT_FONT = ("Arial", 60, "bold")

def next_card(learned_words = False):
    global to_learn, current_card, flip_timer
    window.after_cancel(flip_timer)

    if len(to_learn) <= 0:
        print("CONGRATULATIONS! YOU LEARNED ALL THE WORDS!")
        return
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_canvas_img, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card, current_card["English"])

def remove_and_next_card():
    global current_card
    global to_learn, current_card
    try:
        to_learn.remove(current_card)
    except ValueError:
        print("Couldn't remove word")
    to_learn_df = pd.DataFrame(to_learn)
    to_learn_df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

def flip_card(translation):
    canvas.itemconfig(card_canvas_img, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=translation, fill="white")

def ask_reset():
    print("CONGRATULATIONS! YOU LEARNED ALL THE WORDS!")
    reset = messagebox.askyesno(title="Empty .csv", message="Congratulations, there are no more words to learn! Do you wish to reset?")
    if reset:
        os.remove("./data/words_to_learn.csv")

#--------------------------------------------------------------------------------------
# DATA
has_unknown_words = True
try:
    try:
        data = pd.read_csv("./data/words_to_learn.csv")
    except pd.errors.EmptyDataError:
        ask_reset()
        to_learn = {}
        num_of_words = 0
        has_unknown_words = False
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")

if has_unknown_words:
    to_learn = data.to_dict(orient="records")
    num_of_words = data.count()
else:
    num_of_words = 0



#--------------------------------------------------------------------------------------
# INTERFACE
window = Tk()
window.title("Flashly")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_canvas_img = canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text="word", font=TEXT_FONT)

canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_btn = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_btn.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
known_btn = Button(image=check_image, highlightthickness=0, command=remove_and_next_card)
known_btn.grid(row=1, column=1)

if num_of_words > 0:
    current_card = random.choice(to_learn)
    flip_timer = window.after(3000, flip_card, current_card["English"])
    next_card()
else:
    window.quit()

window.mainloop()