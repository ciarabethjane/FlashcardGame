from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# Create dataframe
df = pd.read_csv("data/french_words.csv")

# Get random words from data file
words = df.sample()
wordDict = words.to_dict()
engDict = wordDict["English"]
engKeys = str(engDict.values())
engWord = engKeys[14:-3]
frDict = wordDict["French"]
frKeys = str(frDict.values())
frWord = frKeys[14:-3]


'''def newWords():
    words = df.sample()
    wordDict = words.to_dict()
    engDict = wordDict["English"]
    engKeys = str(engDict.values())
    engWord = engKeys[14:-3]
    frDict = wordDict["French"]
    frKeys = str(frDict.values())
    frWord = frKeys[14:-3]'''

# Button interactions
def correct_clicked():
    words = df.sample()
    wordDict = words.to_dict()
    engDict = wordDict["English"]
    engKeys = str(engDict.values())
    engWord = engKeys[14:-3]
    frDict = wordDict["French"]
    frKeys = str(frDict.values())
    frWord = frKeys[14:-3]
    canvas.create_image(400, 263, image=cardFront)
    canvas.create_text(400, 150, text=str(engWord), font=("Ariel", 40, "italic"))
    canvas.create_text(400, 263, text=str(frWord), font=("Ariel", 60, "bold"))



def incorrect_clicked():
    words = df.sample()
    wordDict = words.to_dict()
    engDict = wordDict["English"]
    engKeys = str(engDict.values())
    engWord = engKeys[14:-3]
    frDict = wordDict["French"]
    frKeys = str(frDict.values())
    frWord = frKeys[14:-3]
    canvas.create_image(400, 263, image=cardFront)
    canvas.create_text(400, 150, text=str(engWord), font=("Ariel", 40, "italic"))
    canvas.create_text(400, 263, text=str(frWord), font=("Ariel", 60, "bold"))



# Create the GUI

window = Tk()
window.title("Flashcard Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
cardFront = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=cardFront)
canvas.create_text(400, 150, text=str(engWord), font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text=str(frWord), font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=4)

incorrectImage = PhotoImage(file="images/wrong.png")
ukButton = Button(image=incorrectImage, command=incorrect_clicked)
ukButton.grid(row=1, column=1)

correctImage = PhotoImage(file="images/right.png")
correctButton = Button(image=correctImage, command=correct_clicked)
correctButton.grid(row=1, column=2)



window.mainloop()