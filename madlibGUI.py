## Import tk interface to create GUI with Python
from tkinter import *

## Configure GUI window
screen = Tk()
screen.title("Murakami Madlibs")
screen.geometry("500x600")
Label(screen, text= "Welcome to Murakami Madlibs! \n Are you ready to write your own masterpiece?" , font = 'arial 16').pack()

## Create madlib story
def madlib(tl: screen, first_name, last_name, object_1, adjective, animal, object_2, opinion, monster, place_1):
    
    text = f"{first_name} {last_name} is feeling melancholy after being left by their {object_1}. The future seems {adjective}. After meeting a talking {animal}, they set out on an adventure to find a {object_2}. On {first_name}'s travels, they reflect on whether {opinion}. Suddenly, a {monster} attacks them and they are thrown back to a {place_1}. {first_name} wakes up dazed and confused but finds the {object_2}."

    Label(tl, text=text, font=("ariel", 16), wraplength=tl.winfo_width()).place(x=0, y=410)

## Create prompts, entry boxes, and buttons for user input
Label(screen, text='Enter a first name:').place(x=10, y=50)
Label(screen, text='Enter a last name:').place(x=10, y=90)
Label(screen, text='Enter a noun:').place(x=10, y=130)
Label(screen, text='Enter an adjective:').place(x=10, y=170)
Label(screen, text='Enter an animal:').place(x=10, y=210)
Label(screen, text='Enter another noun:').place(x=10, y=250)
Label(screen, text='Enter an opinion you feel strongly about:').place(x=10, y=290)
Label(screen, text='Enter a monster:').place(x=10, y=330)
Label(screen, text='Enter a place:').place(x=10, y=370)
first_name = Entry(screen, width=17)
first_name.place(x=270, y=50)
last_name = Entry(screen, width=17)
last_name.place(x=270, y=90)
object_1 = Entry(screen, width=17)
object_1.place(x=270, y=130)
adjective = Entry(screen, width=17)
adjective.place(x=270, y=170)
animal = Entry(screen, width=17)
animal.place(x=270, y=210)
object_2 = Entry(screen, width=17)
object_2.place(x=270, y=250)
opinion = Entry(screen, width=17)
opinion.place(x=270, y=290)
monster = Entry(screen, width=17)
monster.place(x=270, y=330)
place_1 = Entry(screen, width=17)
place_1.place(x=270, y=370)
SubmitButton = Button(screen, text="Write my story", font=('ariel', 12), command = lambda:madlib(screen, first_name.get(), last_name.get(), object_1.get(), adjective.get(), animal.get(), object_2.get(), opinion.get(), monster.get(), place_1.get()))
SubmitButton.place(x=150, y=410)

screen.mainloop()