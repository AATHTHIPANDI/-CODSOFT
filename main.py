from tkinter import *
import random

lst = ["ROCK", "PAPER", "SCISSOR"]
chance = 3


def play(user_in):
    global chance
    if chance > 0:
        comp_in = random.choice(lst)
        if user_in == comp_in:
            result = "DRAW"
        elif (user_in == "ROCK" and comp_in == "SCISSOR") or (user_in == "PAPER" and comp_in == "ROCK") or (user_in == "SCISSOR" and comp_in == "PAPER"):
            result = "YOU WIN"
        else:
            result = "YOU LOSE"

        chance -= 1
        note.config(text=f"You have {chance} chances left!")
        text.insert(END, f"You chose {user_in}, Computer chose {comp_in}.\nResult: {result}\n")

        if chance == 0:
            note.config(text="Game Over!")
            rock.config(state=DISABLED)
            paper.config(state=DISABLED)
            scissor.config(state=DISABLED)
    else:
        note.config(text="Game Over!")


window = Tk()
window.minsize(500, 500)

heading = Label(text="ROCK PAPER SCISSORS", font=("Courier", 20, "bold"))
heading.pack()

note = Label(text="You have 3 chances!!", fg="red", font=("Courier", 15, "bold"))
note.place(x=10, y=30)

text = Text(width=40, height=10)
text.place(x=90, y=70)


rock = Button(text="ROCK", background="orange", width=8, command=lambda: play("ROCK"),
              font=("New text Roman", 20, "bold"))
rock.place(x=10, y=250)

paper = Button(text="PAPER", background="white", width=8, command=lambda: play("PAPER"),
               font=("New text Roman", 20, "bold"))
paper.place(x=160, y=250)

scissor = Button(text="SCISSOR", width=8, background="pink", command=lambda: play("SCISSOR"),
                 font=("New text Roman", 20, "bold"))
scissor.place(x=310, y=250)

reset = Button(text="SCISSOR", width=8, background="pink", command=lambda: play("SCISSOR"),
                 font=("New text Roman", 20, "bold"))
window.mainloop()
