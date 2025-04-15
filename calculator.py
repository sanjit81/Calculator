from tkinter import *
import tkinter as tk

                # Initialize the main window
win = tk.Tk()
win.title("Python Calculator")
win.geometry("361x381+500+200")
win.config(bg="black")
win.resizable(0, 0)
operator=""
input_value=StringVar
                # Initialize the display variable
val = ""
data = tk.StringVar()

                # Function to update the display when a button is clicked
def btnclick(number):
        global operator 
        operator =  opertor + str(number)
        input_value.set(operator)  
        #val += str(number)
        #data.set(val)

                # Function to clear the display
def btnClear():
        global operator
        operator=""
        input_value.set("")
        #val = ""
        #data.set("")

def btnEquals():
        global val
        
                # Create the display Entry widget
        display = tk.Entry(win, textvariable=data, bd=29, justify="right", bg="powder blue", font=("arial", 20))
        display.grid(row=0, column=0, columnspan=4)

                # Create number buttons
        btn7=Button(win,text="7",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(7))
        btn7.grid(row=1,column=0)

        btn8=Button(win,text="8",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(8))
        btn8.grid(row=1,column=1)

        btn9=Button(win,text="9",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(9))
        btn9.grid(row=1,column=2)

        btn_add=Button(win,text="+",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick('+'))
        btn_add.grid(row=1,column=3)

        btn4=Button(win,text="4",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(4))
        btn4.grid(row=2,column=0)

        btn5=Button(win,text="5",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(5))
        btn5.grid(row=2,column=1)

        btn6=Button(win,text="6",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(6))
        btn6.grid(row=2,column=2)

        btn_sub=Button(win,text="-",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick('-'))
        btn_sub.grid(row=2,column=3)

        btn1=Button(win,text="1",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(1))
        btn1.grid(row=3,column=0)

        btn2=Button(win,text="2",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(2))
        btn2.grid(row=3,column=1)

        btn3=Button(win,text="3",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(3))
        btn3.grid(row=3,column=2)

        btn_mult=Button(win,text="*",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick('*'))
        btn_mult.grid(row=3,column=3)

        btn_clear = Button(win,text="C",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClear)
        btn_clear.grid(row=4,column=0)

        btn0=Button(win,text="0",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(0))
        btn0.grid(row=4,column=1)

        btn_equal=Button(win,text="=",font=("arial",12,"bold"),bd=12,height=2,width=6,command=btnEquals)
        btn_equal.grid(row=4,column=2)

        btn_div=Button(win,text="/",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick('/'))
        btn_div.grid(row=4,column=3)

                # Add more buttons as needed...

                # Run the application
        win.mainloop()