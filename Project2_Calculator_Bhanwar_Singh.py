from tkinter import *
operator = ""

def buttonClick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)

def buttonEqual():
        global operator
        try:
                results = str(eval(operator))
                input_value.set(results)
                operator = results
        except:
                input_value.set("Error")
                operator = ""

def buttonClear():
        global operator         
        operator= ""
        input_value.set("")
        
def buttonBackspace():
    global operator
    operator = operator[:-1]  
    input_value.set(operator)
    
import math
def buttonSqrt():
    global operator
    try:
        value = float(operator)
        result = str(math.sqrt(value))
        input_value.set(result)
        operator = result
    except:
        input_value.set("Error")
        operator = ""
                
main = Tk()
main.title ("Calculator")
main.geometry("400x460")

operator = ""
input_value = StringVar()
display_text = Entry(main, font=("arial",20,"bold"),textvariable=input_value,bd=39,insertwidth=4,
                     bg="powder blue", justify=RIGHT)
display_text.grid(columnspan=4)

#Row 1-  7 8 9 +

btn_7 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="7",command=lambda: buttonClick(7))
btn_7.grid(row=1,column=0)

btn_8 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="8",command= lambda : buttonClick(8))
btn_8.grid(row=1,column=1)

btn_9 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="9",command= lambda: buttonClick(9))
btn_9.grid(row=1,column=2)

btn_add = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="+" ,command= lambda: buttonClick("+"))
btn_add.grid(row=1,column=3)

#row 2-  4 5 6 -

btn_4 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="4",command= lambda: buttonClick(4))
btn_4.grid(row=2,column=0)

btn_5 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="5",command= lambda: buttonClick(5))
btn_5.grid(row=2,column=1)

btn_6 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="6",command= lambda: buttonClick(6))
btn_6.grid(row=2,column=2)

btn_sub = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="-",command= lambda: buttonClick("-"))
btn_sub.grid(row=2,column=3)

#row 3-  1 2 3 x

btn_1 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="1",command= lambda: buttonClick(1))
btn_1.grid(row=3,column=0)

btn_2 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="2",command= lambda: buttonClick(2))
btn_2.grid(row=3,column=1)

btn_3 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="3",command= lambda: buttonClick(3))
btn_3.grid(row=3,column=2)

btn_mult = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="x",command= lambda: buttonClick("*"))
btn_mult.grid(row=3,column=3)

#Row 4-   ÷ 0 . = 

btn_0 = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="0",command= lambda: buttonClick(0))
btn_0.grid(row=4,column=1)

btn_equal = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="=",command=buttonEqual)
btn_equal.grid(row=4,column=3)

btn_div = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="÷",command= lambda: buttonClick("/"))
btn_div.grid(row=4,column=2)

btn_dot = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text=".",command= lambda: buttonClick("."))
btn_dot.grid(row=4,column=0)

#Row 5-    AC % √ ←
btn_clear = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="AC",command= buttonClear)
btn_clear.grid(row=5,column=0)

btn_pcnt = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="%",command= lambda: buttonClick("/100"))
btn_pcnt.grid(row=5,column=1)

btn_sqrt = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="√",command=buttonSqrt)
btn_sqrt.grid(row=5,column=2)

btn_back = Button(main,padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="←",command=buttonBackspace)
btn_back.grid(row=5,column=3)

main.mainloop()