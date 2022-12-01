### Main Driver for Flash Card creation 
# Leveraging to learn Spanish for my trip 
# 11/22 - need to correct the storage of the correct word IDs


## ---------------------------- Imports ----------------------------------------------##

from tkinter import *
import pandas as pd
import unidecode as uc
import random
import numpy as np
## --------------------------- Globals, methods, constants ---------------------------##

window = Tk()

TEAL = "#008080"
WHITE = "#FFFFFF"
BLACK = "#000000"
FONT = "Times New Roman"

# Lists to store indices of correct/wrong words 
global correctWord, wrongWord
correctWord = []
wrongWord = []
cardAttributes = {
    'Spanish':'',
    'English':'', 
    'Number': ''
}

def currentCard (spanTxt:Text) -> int: 
    '''Stores current card properties, returns wordNumber for correct/incorrect storage'''
    # Store properties of the selected card
    word_num = str((df.loc[df["Spanish"] == spanTxt]["Number"]).iat[0])
    engTrans = df.loc[df["Spanish"]==spanTxt]["English"].iat[0]

    cardAttributes['Spanish'] = spanTxt
    cardAttributes['English'] = engTrans
    cardAttributes["Number"] = word_num

    return word_num


def chkButFnc():
    '''Function changing the words when the check button is pressed'''
    
    # Change title text of the card,background
    canvas.itemconfig(title_text, text= "Spanish")
    canvas.itemconfig(card_img,image=front_bckgrnd_img)

    # Access the next card
    next_word = random.choice(df["Spanish"])
    
    # Store card properties
    word_num = currentCard(next_word)

    # Change canvas text
    canvas.itemconfig(word_text, text = next_word)

    # Track the correct words 
    correctWord.append(word_num)
 
def xButFnc():
    '''Function changing the words when the check button is pressed'''
    
    # Change title text of the card, background
    canvas.itemconfig(title_text, text= "Spanish")
    canvas.itemconfig(card_img,image=front_bckgrnd_img)

    # Access the next card
    next_word = random.choice(df["Spanish"])

     # Store card properties
    word_num = currentCard(next_word)

    # Change canvas text
    canvas.itemconfig(word_text, text = next_word)

    # Track the wrong words 
    wrongWord.append(word_num)

def cardFlip(key):
    # Modify the title
    canvas.itemconfig(title_text,text= "English")

    # Modify the background
    canvas.itemconfig(card_img,image=back_bckgrnd_img)
    
    # Change to english 
    canvas.itemconfig(word_text,text=cardAttributes['English'])
    
    
    print("entered CardFlip func")

    



## -------------------------- Word Processing ----------------------------------------##

df = pd.read_csv("/Users/samchernov/Desktop/Learnings/gitProjects/day31_FlashCards/span_eng_trans_top500_sub.csv")
df['Spanish'] = df['Spanish'].apply(uc.unidecode)
df.to_json("/Users/samchernov/Desktop/Learnings/gitProjects/day31_FlashCards/word_data.json",orient = 'table', index= False)
print("Success")



## ---------------------------- Creating the user interface ----------------------------##
window.title("Flash Card Generator")
window.minsize(width=100, height=800)
window.config(padx=50, pady=50, bg = TEAL)

# Create new Canvas with flashcard background, front
canvas = Canvas(width=800, height=600, bg=WHITE, highlightthickness=0)
front_bckgrnd_img = PhotoImage(file="/Users/samchernov/Desktop/Learnings/gitProjects/day31_FlashCards/images/card_front.png")
back_bckgrnd_img =PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400,300,image=front_bckgrnd_img)
canvas.grid(column=0,row=0)
canvas.config(bg=TEAL)

# Add text to canvas 
title_text = canvas.create_text(400,150,text="Title", font=(FONT, 45, "italic"),fill=BLACK)
word_text = canvas.create_text(400,300,text="Word", font=(FONT, 70, "bold"),fill=BLACK)
canvas.grid(column=1, row=1,columnspan=2)



# On screen widgets 


# Buttons

x_image = PhotoImage(file="/Users/samchernov/Desktop/Learnings/gitProjects/day31_FlashCards/images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0,command=xButFnc)
x_button.grid(column=1, row = 2)

ck_image = PhotoImage(file="/Users/samchernov/Desktop/Learnings/gitProjects/day31_FlashCards/images/right.png")
ck_button = Button(image=ck_image, highlightthickness=0,command=chkButFnc)
ck_button.grid(column=2, row=2)

# Flip Card using spacebar 
window.bind("<space>", cardFlip)










window.mainloop()