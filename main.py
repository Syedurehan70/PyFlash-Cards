from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
ran_word_dict = {}
known_word_list = []


# --------------------------Flip The Card------------------------------------------
def flipping():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=ran_word_dict["English"], fill="white")


# -------------------------CSV READ-----------------------------------------------
def save():
    updated_data = pandas.DataFrame(word_dict_list)
    updated_data.to_csv("data/words_to_learn.csv", index=False)
    window.destroy()


def known_words():
    # REMOVES THE CURRENT CARD
    if len(word_dict_list) != 0:
        word_dict_list.remove(ran_word_dict)
        unknown_words()
    else:
        canvas.itemconfig(card_title, text="Well Done", fill="black")
        canvas.itemconfig(card_word, text="You've Learned all \n the cards", fill="black")
        canvas.itemconfig(canvas_image, image=front_img)


def unknown_words():
    global ran_word_dict, stop
    # it's going stop the previous sec count, so it can run from the start in every round
    window.after_cancel(stop)
    if len(word_dict_list) != 0:
        ran_word_dict = random.choice(word_dict_list)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=ran_word_dict["French"], fill="black")
        canvas.itemconfig(canvas_image, image=front_img)
        stop = window.after(3000, flipping)
    else:
        canvas.itemconfig(card_title, text="Well Done", fill="black")
        canvas.itemconfig(card_word, text="You've Learned all \n the cards", fill="black")
        canvas.itemconfig(canvas_image, image=front_img)


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    # created a list of dictionaries, w.r.t to rows
    word_dict_list = data.to_dict(orient="records")

# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# only created a variable
stop = window.after(3000, flipping)

# Canvas setup
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 100, text="", font=("Arial", 30, "italic"))
card_word = canvas.create_text(400, 250, text="", font=("Arial", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=3)

# Buttons
check_img = PhotoImage(file="./images/right.png")
check = Button(image=check_img, highlightthickness=0, command=known_words)
check.grid(row=1, column=2)

cross_img = PhotoImage(file="./images/wrong.png")
cross = Button(image=cross_img, highlightthickness=0, command=unknown_words)
cross.grid(row=1, column=0)

exit_button = Button(text="Exit", highlightthickness=0, bg="purple", fg="white", command=save)
exit_button.grid(row=1, column=1)
unknown_words()

window.mainloop()
