# Import required modules
from tkinter import *
import tkinter.font as font
 
 
 
# Creating the main window
root = Tk()
 
# Assigning it the desired geometry
root.geometry("380x450")
 
# Assigning the name of our window
root.title("Calculator")
 
# Assigning it the capability to
# be resizable (It is default)
root.resizable(0, 0)
 
# Creating a StringVar to take
# the text entered in the Entry widget
inp = StringVar()
myFont = font.Font(size=15)
 
# Creating an Entry widget to get the
# mathematical expression
# And also to display the results
screen = Entry(root, text=inp, width=30,
               justify='right', font=(10), bd=4)
 
# We will use a grid like structure
screen.grid(row=0, columnspan=4, padx=15, pady=15, ipady=5)

back_arrow_unicode = u"\u2190"
squareroot_unicode = u"\u221A"
square_unicode = "x" + u"\u00B2"
one_over_x = u"\u215F" + "x"
cube_unicode = "x" + u"\u00B3"
# Key matrix contains all the required the keys
key_matrix = [["C","%", "/",back_arrow_unicode],
              [square_unicode,cube_unicode, squareroot_unicode, one_over_x],
              ["7", "8", "9", "*"],
              ["4", "5", "6", "-"],
              ["1", "2", "3", "+"],
              ["!", 0, ".", "="]]
 
# Creating a dictionary for the buttons
btn_dict = {}
 
# Variable to store our results
ans_to_print = 0
 
# Defining the function for calculation
def Calculate(event):
   
    # getting the name of the button clicked
    button = event.widget.cget("text")
 
    # Referring the global values
    global key_matrix, inp, ans_to_print
 
    try:
        # Event containing a sqrt operation
        if button == squareroot_unicode:
            # ans = float(inp.get())**(0.5)
            ans = float(eval(inp.get()))**(0.5)            
            ans_to_print = str(ans)
            inp.set(str(ans))
 
        elif button == "C":  # Clear Button
            inp.set("")
 
        elif button == "!":  # Factorial
            def fact(n): return 1 if n == 0 else n*fact(n-1)
            inp.set(str(fact(int(inp.get()))))
 
        elif button == back_arrow_unicode:  # Backspace
            inp.set(inp.get()[:len(inp.get())-1])
 
        elif button == "=":  # Showing The Results
            # Calculating the mathematical exp. using eval
            ans_to_print = str(eval(inp.get()))
            inp.set(ans_to_print)
          
        elif button == square_unicode:
            a = eval(inp.get())
            inp.set(str(a**2))
        
        elif button == "%":
            b = eval(inp.get())
            inp.set(str(b/100))
        
        elif button == one_over_x:
            c = eval(inp.get())
            inp.set(str(1/c))
        
        elif button == cube_unicode:
            d = eval(inp.get())
            inp.set(str(d**3))

 
        # You may add many more operations
 
        else:
            # Displaying the digit pressed on screen
            inp.set(inp.get()+str(button))
 
    except:
        # In case invalid syntax given in expression
        inp.set("Wrong Operation")
 

# Creating the buttons using for loop
 
# Number of rows containing buttons
for i in range(len(key_matrix)): 
    # Number of columns 
    for j in range(len(key_matrix[i])): 
 
        # Creating and Adding the buttons to dictionary
        btn = Button(
          root, bd=1, text=str(key_matrix[i][j]), font=myFont)
        
        btn_dict["btn_"+str(key_matrix[i][j])] = btn
         
        # Positioning buttons
        btn.grid(
          row=i+1, column=j, padx=5, pady=5, ipadx=5, ipady=5)
         
        # Assigning an action to the buttons
        btn.bind('<Button-1>', Calculate)