from tkinter import *
import random


window = Tk()
window.geometry("300x300")
window.resizable(False, False)
window.title("RPS")
window.configure(bg='black')
computer_value = {"0": "Rock", "1": "Paper", "2": "Scissor"}


def clear_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player              ")
    l3.config(text="Computer")
    l4.config(text="")


def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"


def rock():
    com_value = computer_value[str(random.randint(0, 2))]
    if com_value == "Rock":
        match_result = "Match Draw"
    elif com_value == "Scissor":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l4.config(text=match_result)
    l1.config(text="Rock            ")
    l3.config(text=com_value)
    button_disable()


def paper():
    com_value = computer_value[str(random.randint(0, 2))]
    if com_value == "Paper":
        match_result = "Match Draw"
    elif com_value == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    l4.config(text=match_result)
    l1.config(text="Paper           ")
    l3.config(text=com_value)
    button_disable()


def scissor():
    com_value = computer_value[str(random.randint(0, 2))]
    if com_value == "Rock":
        match_result = "Computer Win"
    elif com_value == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Win"
    l4.config(text=match_result)
    l1.config(text="Scissor         ")
    l3.config(text=com_value)
    button_disable()


Label(window, text="Rock Paper Scissor", font="normal 22 bold", fg="red", bg="black").pack(pady=20)
frame = Frame(window)
frame.pack()

l1 = Label(frame, text="Player              ", font=10, fg="white", bg="black")
l2 = Label(frame, text="VS             ", font=10, fg="white", bg="black")
l3 = Label(frame, text="Computer", font=10, fg="white", bg="black")
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()
l4 = Label(window, text="", font="normal 20 bold", bg="white", width=15, borderwidth=2, relief="solid")
l4.pack(pady=20)

frame1 = Frame(window)
frame1.configure(bg="black")
frame1.pack()
b1 = Button(frame1, text="Rock", font=10, width=7, command=rock)
b2 = Button(frame1, text="Paper ", font=10, width=7, command=paper)
b3 = Button(frame1, text="Scissor", font=10, width=7, command=scissor)
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(window, text="Clear Game", font=10, fg="red", bg="white", command=clear_game).pack(pady=20)

window.mainloop()
