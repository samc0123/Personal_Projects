# Password manager Main file

# ---------------------------------------------------Imports-------------------------------------------
import numbers
from textwrap import indent
from tkinter import *
from tkinter import messagebox
from matplotlib.font_manager import json_dump
import pandas as pd
import os
import random
import string
import numpy as np
import json
from scipy import rand
# ------------------------------------- Globals, methods, constants, etc. ----------------------------
window = Tk()
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#FFFFFF"
BLACK = "#000000"
FONT = "Calibri"
FONT_SIZE_LBL = 14
FONT_SIZE_ENTRY = 12


# -----------------------------------------------Generate Password-----------------------------------------------

def pass_generator():
    '''Generates password for user, standard 12 chars'''
    # Get all possible chars
    alpha_list = list(string.ascii_lowercase)
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    alpha_len = len(alpha_list) - 1
    num_len = len(num_list) - 1

    password_list = []
    letters = []
    numbers = []
    password = ""

    # Random pairs of 12 - letters and numbers
    pairs = [(2, 10), (3, 9), (4, 8), (5, 7), (6, 6)]
    chosen_pair = pairs[random.randint(0, len(pairs)-1)]
    num_letters = chosen_pair[0]
    num_numbers = chosen_pair[1]

    # Choose letters

    for i in range(0, num_letters):
        letters.append(alpha_list[random.randint(0, alpha_len)])
    # Capitalize 2 random letters
    for upp in range(0, 1):
        rand_letter = random.randint(0, num_letters - 1)
        letters[rand_letter] = letters[rand_letter].upper()

    # Choose numbers
    for j in range(0, num_numbers):
        numbers.append(str(num_list[random.randint(0, num_len)]))

    # Finalize password
    password_list = letters + numbers
    random.shuffle(password_list)

    password = ''.join(str(x) for x in password_list)
    entry_password.set(f"{password}")


# ------------------------------------------------ Save Password ------------------------------------------------
def initiate_save():
    '''Establish JSON objects for storing info'''

    """  # app_df = pd.DataFrame(columns=["Website", "Username", "Password"])
    # app_df = save_details(app_df)

    # To file


    # if os.stat(path="pass.csv").st_size == 0: # insert 1 header
    #     app_df.to_csv('pass.csv',mode='a',index=False)
    #     return
    # header = False
    # app_df.to_csv('pass.csv',mode='a',index=False,header=header)
     """

    # New JSON formatted code
    web_save = web_entry.get()
    em_usrn_save = em_usrn_entry.get()
    pass_save = pass_entry.get()

    # Rework for JSON
    new_data = {
        web_save: {
            "email": em_usrn_save,
            "password": pass_save,
        }
    }
    # Dump into new JSON if not existing
    with open("pass.json", "w") as data_file:
        data_j = json.dump(new_data, data_file, indent=4)
        messagebox.showinfo(title="Created new manager",
                        message="Entry added to new password manager")

    if len(web_save) == 0 or len(pass_save) == 0:
        messagebox.showinfo(title="Error", message="Please enter a value")
    else:
            data_j=json.load(fp = data_file)
            data_j.update(new_data, indent = 4)
            messagebox.showinfo(title = "Success",
                                message = "You're entry was added")






""" def save_details() -> json:
    '''Saves the password details including website, username, and password'''

    web_save = web_entry.get()
    em_usrn_save = em_usrn_entry.get()
    pass_save = pass_entry.get()

    # Rework for JSON
    new_data = {
        web_save:{
            "email": em_usrn_save,
            "password": pass_save,
        }
    }


    df_temp = pd.DataFrame({'Website':[web_save],
    'Username':[em_usrn_save],
    'Password':[pass_save]})

    main_df = pd.concat([main_df,df_temp],ignore_index=True,axis=0)
    print(main_df)
    return main_df """



# ------------------------------------------------Screen Setup----------------------------------------
window.title("Password Manager")
window.minsize(width = 600, height = 400)
window.config(padx = 50, pady = 50, bg = BLACK)

canvas=Canvas(width = 150, height = 150, bg = BLACK, highlightthickness = 0)
lockImg=PhotoImage(file = "passImg.png")
lockImg=lockImg.zoom(20)
lockImg=lockImg.subsample(80)
canvas.create_image(75, 80, image = lockImg)
canvas.grid(column = 2, row = 1)

# -------------------------------------------- Add on-screen widgets ------------------------------------

# Labels
web_lbl=Label(text = "Wesbite", font = (
    FONT, FONT_SIZE_LBL, "normal"), bg = BLACK)
web_lbl.grid(column = 1, row = 2)

em_usrn_lbl=Label(text = "Email/Username", font = (FONT,
                  FONT_SIZE_LBL, "normal"), bg = BLACK)
em_usrn_lbl.grid(column = 1, row = 3)

pass_lbl=Label(text = "Password", font = (
    FONT, FONT_SIZE_LBL, "normal"), bg = BLACK)
pass_lbl.grid(column = 1, row = 4)

# Entry boxes
web_entry=Entry(font = (FONT, FONT_SIZE_ENTRY, "normal"),
                bg = BLACK, width = 35)
web_entry.grid(column = 2, row = 2, columnspan = 2, sticky = "W")
web_entry.focus()

em_usrn_entry=Entry(font = (FONT, FONT_SIZE_ENTRY,
                    "normal"), bg = BLACK, width = 35)
em_usrn_entry.grid(column = 2, row = 3, columnspan = 2, sticky = "W")
em_usrn_entry.insert(index = 0, string = "schernov1999@gmail.com")

entry_password=StringVar()
pass_entry= Entry(font = (FONT, FONT_SIZE_ENTRY, "normal"), bg = BLACK, width = 21, textvariable = entry_password)
pass_entry.grid(column = 2, row = 4, columnspan = 1, sticky = "W")

# Buttons
gen_pass_btn = Button(text = "Generate Password", font = (FONT, FONT_SIZE_LBL-4, "normal"), bg = BLACK, highlightthickness = 0, width = 15, command = pass_generator)
gen_pass_btn.grid(column = 3, row = 4, sticky = "W", columnspan = 1)

add_btn = Button(text = "Add", font = (FONT, FONT_SIZE_LBL - 2, "normal"), bg = BLACK, highlightthickness = 0,width = 36,command =initiate_save)
add_btn.grid(column = 2, row = 5, columnspan = 2, sticky = "W")




















window.mainloop()
