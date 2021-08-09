BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
current_card= {}
to_learn={}


#read from csv
try:
    data= pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data= pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient= "records")
else:
    to_learn= data.to_dict(orient= "records")




def refresh():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card= random.choice(to_learn)
    current_card["French"]
    canvas.itemconfig(card_title, text= "French", fill= "Black")
    canvas.itemconfig(card_word, text=current_card["French"],fill= "Black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer= window.after(3000, func=flip_card)





#change the canvas

def flip_card():
    canvas.itemconfig(canvas_image, image= back_img)
    canvas.itemconfig(card_title, text="English", fill= "White")
    canvas.itemconfig(card_word, text= current_card["English"], fill= "White")


def is_known():
    to_learn.remove(current_card)
    refresh()
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index= False)



window = Tk()
window.title= ("Flash Card")
window.config(padx= 50, pady=50, bg=BACKGROUND_COLOR )

flip_timer= window.after(3000, func= flip_card)

#import logo
back_img= PhotoImage(file= "images/card_back.png")
front_img= PhotoImage(file= "images/card_front.png")
right_img= PhotoImage(file= "images/right.png")
wrong_img= PhotoImage(file= "images/wrong.png")
canvas= Canvas(width= 800, height=526,bg =BACKGROUND_COLOR)
# canvas.create_image(850,576,image= back_img)
canvas_image= canvas.create_image(400,263,image= front_img)
card_title= canvas.create_text(400, 150, font= ("Ariel", 40, "bold"))
card_word= canvas.create_text(400, 263, font= ("Ariel", 60, "bold"))

canvas.config(bg= BACKGROUND_COLOR,highlightthickness = 0)
canvas.grid(column= 0, row= 0, columnspan= 2)


#Button
unknow_button= Button(image= wrong_img,highlightthickness = 0, command= refresh)
unknow_button.grid(column= 0,row= 1)
yes_button= Button(image= right_img,highlightthickness = 0, command= is_known)
yes_button.grid(column= 1,row= 1)


refresh()




# canvas.create_text(400, 150, font=("Ariel", 40, "bold"), fill= "White")
# canvas.create_text(400, 263, font=("Ariel", 40, "bold"), fill= "White")



window.mainloop()