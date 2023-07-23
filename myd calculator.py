import tkinter as tk
from math import sqrt, factorial

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        text_Input.set(operator)
    except Exception as e:
        operator = ""
        text_Input.set("Error")

def btnSqrt():
    global operator
    try:
        num = eval(operator)
        if num < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        result = sqrt(num)
        operator = str(result)
        text_Input.set(operator)
    except Exception as e:
        operator = ""
        text_Input.set("Error")

def btnFactorial():
    global operator
    try:
        num = eval(operator)
        if num < 0:
            raise ValueError("Cannot calculate factorial of a negative number.")
        result = factorial(int(num))
        operator = str(result)
        text_Input.set(operator)
    except Exception as e:
        operator = ""
        text_Input.set("Error")

def btnDecimal():
    global operator
    if '.' not in operator:
        operator += '.'
    text_Input.set(operator)

def btnBackspace():
    global operator
    operator = operator[:-1]
    text_Input.set(operator)

cal = tk.Tk()
cal.title("Calculator by yusuf")
operator = ""
text_Input = tk.StringVar()

txtDisplay = tk.Entry(cal, font=('verdana', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="white", justify='right')
txtDisplay.grid(columnspan=4)

btn7=tk.Button(cal, padx=16, bd=8, fg="white", font=('arial', 20, 'bold'), bg="black", text="7", command=lambda:btnClick(7)).grid(row=2, column=0)
btn8=tk.Button(cal, padx=16 ,bd=8, fg="white", font=('arial', 20, 'bold'), bg="black", text="8", command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=tk.Button(cal, padx=16 ,bd=8, fg="white", font=('arial', 20, 'bold'), bg="black", text="9", command=lambda:btnClick(9)).grid(row=2,column=2)
Addition=tk.Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="+", command=lambda:btnClick("+"), bg="white").grid(row=2,column=3)

btn4=tk.Button(cal, padx=16 ,bd=8, fg="white", font=('arial', 20, 'bold'), bg="black", text="4", command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=tk.Button(cal, padx=16 ,bd=8, fg="white", font=('arial', 20, 'bold'), bg="black", text="5", command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=tk.Button(cal, padx=16 ,bd=8, fg="white", font=('arial', 20, 'bold'), bg="black", text="6", command=lambda:btnClick(6)).grid(row=3,column=2)
Subtraction=tk.Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="-", command=lambda:btnClick("-"), bg="white").grid(row=3,column=3)

btn1=tk.Button(cal, padx=16 ,bd=8, fg="white", font=('arial', 20, 'bold'), bg="black", text="1", command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=tk.Button(cal, padx=16 ,bd=8, fg="white", font=('arial', 20, 'bold'), bg="black", text="2", command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=tk.Button(cal, padx=16 ,bd=8, fg="white", font=('arial', 20, 'bold'), bg="black",text="3", command=lambda:btnClick(3)).grid(row=4,column=2)
Multiplication=tk.Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="*", command=lambda:btnClick("*"), bg="white").grid(row=4,column=3)

btnClear=tk.Button(cal, padx=16 ,bd=8, fg="black", font=('arial', 20, 'bold'), bg="light green", text="C", command=btnClearDisplay).grid(row=5,column=0)
btn0=tk.Button(cal, padx=16 ,bd=8, fg="white", font=('arial', 20, 'bold'), text="0", command=lambda:btnClick(0), bg="black").grid(row=5,column=1)
btnEquals=tk.Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="=", bg="light green", command=btnEqualsInput).grid(row=5,column=2)
Division=tk.Button(cal,padx=16,bd=8,fg="black",font=('arial',20,'bold'), text="/", command=lambda:btnClick("/"), bg="white").grid(row=5,column=3)											

btnSqrt=tk.Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), bg="white", text="√", command=btnSqrt).grid(row=1, column=0)
btnFactorial=tk.Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), bg="white", text="!", command=btnFactorial).grid(row=1, column=1)
btnDecimal=tk.Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), bg="white", text=".", command=btnDecimal).grid(row=1, column=2)
btnBackspace=tk.Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), bg="light green", text="⌫", command=btnBackspace).grid(row=1, column=3)
cal.mainloop()