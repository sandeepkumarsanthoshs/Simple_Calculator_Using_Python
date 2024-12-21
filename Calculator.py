from tkinter import *
from tkinter import font as tf

# Clearing the screen
def clear_screen():
    display.set(" ")

# Displaying entered values on the screen
def press(key):
    if display.get() == "ERROR":
        clear_screen()
    word = display.get() + key
    display.set(word)

# Displays Answers upon clicking '='
def get_ans():
    try:
        word = eval(display.get())
        display.set(word)
    except:
        word = "ERROR"
        display.set(word)

# Setting Geometry,bgcolor and font
window = Tk()
window.geometry("600x500")
window.title("Calculator")
window.configure(bg="#273746")
window.resizable(0,0)
text_font = tf.Font(family='Helvetica', size=20, weight=tf.BOLD)

# Adding the display area.
display = StringVar()
display_area = Entry(window,width=35, bd=20, textvariable=display,state = "readonly",justify="right", font=text_font, bg="powder blue")
display_area.grid(row=0, column=0, columnspan=4,padx="15")


# Number Buttons
button7 = Button(text="7", width="5", bg="#dfe1e6",font=text_font, command=lambda: press("7"))
button8 = Button(text="8", width="5", bg="#dfe1e6", font=text_font, command=lambda: press("8"))
button9 = Button(text="9", width="5", bg="#dfe1e6", font=text_font, command=lambda: press("9"))
button4 = Button(text="4", width="5", bg="#dfe1e6", font=text_font, command=lambda: press("4"))
button5 = Button(text="5", width="5", bg="#dfe1e6", font=text_font, command=lambda: press("5"))
button6 = Button(text="6", width="5", bg="#dfe1e6", font=text_font, command=lambda: press("6"))
button1 = Button(text="1", width="5", bg="#dfe1e6", font=text_font, command=lambda: press("1"))
button2 = Button(text="2", width="5", bg="#dfe1e6", font=text_font, command=lambda: press("2"))
button3 = Button(text="3", width="5", bg="#dfe1e6", font=text_font, command=lambda: press("3"))
button0 = Button(text="0", width="5", bg="#dfe1e6", font=text_font, command=lambda: press("0"))

# Operator Buttons
button_dot = Button(text=".", width="5", bg="#dfe1e6", font=text_font, command=lambda: press("."))
button_plus = Button(text="+", width="5", bg="#dfe1e6", font=text_font, command=lambda: press("+"))
button_equalto = Button(text="=", width="5", bg="#dfe1e6", font=text_font, command=lambda: get_ans())
button_minus = Button(text="-", width="5", bg="#dfe1e6", font=text_font, command=lambda: press("-"))
button_mul = Button(text="x", width="5", bg="#dfe1e6", font=text_font, command=lambda: press("*"))
button_div = Button(text="/", width="5", bg="#dfe1e6", font=text_font, command=lambda: press("/"))
button_clear = Button(text="CLR", width="5", bg="#dfe1e6",font = text_font,command=clear_screen)



#Number Buttons Grid
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button0.grid(row=4,column=0)

#Operator Buttons Grid
button_dot.grid(row=4,column=1,padx=10,pady=10)
button_plus.grid(row=4,column=2,padx=10,pady=10)
button_equalto.grid(row=4,column=3,padx=10,pady=10)
button_minus.grid(row=3,column=3,padx=10,pady=10)
button_mul.grid(row=2,column=3,padx=10,pady=10)
button_div.grid(row=1,column=3,padx=10,pady=10)
button_clear.grid(row=5,column=0,padx=10,pady=10)


window.mainloop()
