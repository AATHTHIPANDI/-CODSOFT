from tkinter import *

def click_button(value):
    current_text = text.get("1.0", END).strip()
    text.delete("1.0", END)
    text.insert(END, current_text + value)

def clear_text():
    text.delete("1.0", END)

def calculate():
    try:
        expression = text.get("1.0", END).strip()
        result = str(eval(expression))
        clear_text()
        text.insert(END, result)
    except Exception:
        clear_text()
        text.insert(END, "Error")

window = Tk()
window.minsize(500, 700)
window.title("Simple Calculator")

title_label = Label(text="SIMPLE CALCULATOR", font=("Times New Roman", 24, "bold"))
title_label.place(x=0, y=0)

text = Text(height=2, width=30, font=("Times New Roman", 18))
text.place(x=100, y=50)


buttons = [
    ('1', 100, 150), ('2', 180, 150), ('3', 260, 150), ('4', 340, 150),
    ('5', 100, 230), ('6', 180, 230), ('7', 260, 230), ('8', 340, 230),
    ('9', 100, 310), ('0', 180, 310),
    ('+', 260, 310), ('-', 340, 310), ('*', 100, 390), ('/', 180, 390),
    ('ANS', 260, 390), ('CLEAR', 100, 470)
]

for (text_value, x_pos, y_pos) in buttons:
    if text_value == 'ANS':
        Button(text=text_value, height=4, width=18, font=("Pixel Coleco", 10, "bold"), command=calculate).place(x=x_pos, y=y_pos)
    elif text_value == 'CLEAR':
        Button(text=text_value, height=4, width=18, font=("Pixel Coleco", 10, "bold"), command=clear_text).place(x=x_pos, y=y_pos)
    else:
        Button(text=text_value, height=4, width=8, font=("Pixel Coleco", 10, "bold"), command=lambda value=text_value: click_button(value)).place(x=x_pos, y=y_pos)

window.mainloop()
