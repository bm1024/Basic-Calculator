""" 
Author: Bianca Magyar
Date: 8/19/2020
Version 1.0
Description: This program runs a basic calculator 
             to add, subtract, multiply and divide.
             It is written in Python and implements 
             a GUI.
"""

#import everything from tkinter
from tkinter import *

#declare expression variable globally
expr = ""

#function that updates expression in entry field
def button_click(clicked):
    #declare expression as global
    global expr
    
    #concatenate the expression
    expr = expr + str(clicked)
    
    #update expression
    equation.set(expr)

def button_equal():
    #exception handling for errors
    try:
        global expr
        
        #evaluate expression
        total = eval(expr)
        equation.set(total)
        
        #reassign expression to new total
        expr = str(total)
        
    except:
        #display error message
        equation.set(" ERROR ")
        
        #reassign to clear expression with error
        expr = ""

#clear expression in entry field
def button_clear():
    global expr
    expr = ""
    equation.set("")



if __name__ == "__main__":
    
    root = Tk()
    root.title("Basic Calculator")
    
    #initiate instance of StringVar class
    equation = StringVar()
    
    #set up entry field
    e= Entry(root, width=60, borderwidth=5, textvariable=equation)
    e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
    
    #equation starting point
    equation.set("0")
    
    
    #define buttons
    #numerical buttons
    button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
    button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
    button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
    button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
    button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
    button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
    button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
    button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
    button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
    button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
    
    #operator buttons
    button_add = Button(root, text="+", padx=40, pady=20, command=lambda: button_click("+"))
    button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: button_click("-"))
    button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: button_click("*"))
    button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: button_click("/"))
    
    #clear and equal buttons
    button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)
    button_clear = Button(root, text="Clear", padx=30, pady=20, command=button_clear)
    
    
    #display buttons on the screen in a grid format
    #row 1
    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)
    button_divide.grid(row=1, column=3)
    
    #row 2
    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)
    button_multiply.grid(row=2, column=3)
    
    #row 3
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)
    button_subtract.grid(row=3, column=3)
    
    #row 4  
    button_clear.grid(row=4, column=0)
    button_0.grid(row=4, column=1)  
    button_equal.grid(row=4, column=2)  
    button_add.grid(row=4, column=3) 
         
    root.mainloop()