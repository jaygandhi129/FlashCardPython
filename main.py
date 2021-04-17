import pandas

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from pandas import *
import random

#########################Reading from CSV ######################
current_card = {}
to_learn = {}
try:
    data = read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient='records')


########### Showing Ans ######################################
def show_ans():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)


######################### Changing word ############################

def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text,text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, show_ans)

def is_known():
    to_learn.remove(current_card)
    change_word()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


########################## UI ###########################################

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, show_ans)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 264, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, pady=50)

my_image1 = PhotoImage(file="images/right.png")
right_button = Button(image=my_image1, highlightthickness=0, border=0, command=is_known)
right_button.grid(row=1, column=0)

my_image2 = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=my_image2, highlightthickness=0, border=0, command=change_word)
wrong_button.grid(row=1, column=1)


change_word()
window.mainloop()
