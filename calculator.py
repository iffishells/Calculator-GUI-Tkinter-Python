import tkinter

from tkinter import *

root = tkinter.Tk();
root.geometry("250x400+300+300")
#root.resizable(0,0)
root.title("Calculator")

parameter = ""
temp1 = ""
operator = ""

def one_isclicked():
    print("clicked")
    global parameter 
    parameter = parameter + "1"
    data.set(parameter)    
    
def two_isclicked():
    print("clicked")
    global parameter 
    parameter = parameter + "2"
    data.set(parameter)       




def three_isclicked():
    print("clicked")
    global parameter 
    parameter = parameter + "3"
    data.set(parameter)

       
def four_isclicked():
    print("clicked")
    global parameter 
    parameter = parameter + "4"
    data.set(parameter)       
def five_isclicked():
    print("clicked")
    global parameter 
    parameter = parameter + "5"
    data.set(parameter)       
def six_isclicked():
    print("clicked")
    global parameter 
    parameter = parameter + "6"
    data.set(parameter)       
def seven_isclicked():
    print("clicked")
    global parameter 
    parameter = parameter + "7"
    data.set(parameter)       
def eight_isclicked():
    print("clicked")
    global parameter 
    parameter = parameter + "8"
    data.set(parameter)       
def nine_isclicked():
    print("clicked")
    global parameter 
    parameter = parameter + "9"
    data.set(parameter)       
def zero_isclicked():
    print("clicked")
    global parameter 
    parameter = parameter + "0"
    data.set(parameter)  
     
    
def plus_clicked():
    global parameter
    global temp1
    global operator

    temp1 = parameter
    operator = "+"
    parameter =  parameter + "+"
    data.set(parameter)
     
def minus_clicked():
    global parameter
    global temp1
    global operator

    temp1 = parameter
    operator = "-"
    parameter =  parameter + "-"
    data.set(parameter)
def multiply_clicked():
    global parameter
    global temp1
    global operator

    temp1 = parameter
    operator = "*"
    parameter =  parameter + "*"
    data.set(parameter)
       
def divide_clicked():
    global parameter
    global temp1
    global operator

    temp1 = parameter
    operator = "/"
    parameter =  parameter + "/"
    data.set(parameter)
   
def equal_isclicked():
    global temp1
    global parameter
    global operator
    
    if operator == "+":
        final_result = int(temp1) + int(parameter[2:])
        print(final_result)
        data.set(str(final_result))
    elif operator =="-":
         final_result = int(temp1) - int(parameter[2:])
         print(final_result)
         data.set(str(final_result))
    elif operator == "*":
         final_result = int(temp1) + int(parameter[2:])
         print(final_result)
         data.set(str(final_result))
    elif operator =="/":
         final_result = int(temp1) + int(parameter[2:])
         print(final_result)
         data.set(str(final_result))
    
'''    print(operator)
    print("frist :" ,int(temp1))
    print("seconed : ",int(parameter[2:]))
    
    final_result = int(temp1) + int(parameter[2:])
    print(final_result)
    data.set(str(final_result))
'''
def clear():
    data.set("")


data = StringVar()

label  = Label(
    root,
    text = "",
    font=("arial" ,10,"bold"),
    fg="black",
    bg = "white",
    textvariable = data ,)
label.pack(expand =True , fill = "both")     
#making frame for each row

btnrow1 = Frame(root)
btnrow1.pack(expand =True , fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand =True , fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand =True , fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand =True , fill="both")






btn1 = Button(
    btnrow1 , 
    text = "1",
    font = ("verdana" ,22),
    relief ="groove",
    border = "0",
    command = one_isclicked,
        )
btn1.pack(side = LEFT ,expand = True , fill="both")

btn2 = Button(
    btnrow1 , 
    text = "2",
    font = ("verdana" ,22),
    relief ="groove",
    border = "0",
    command = two_isclicked,    
    )
btn2.pack(side = LEFT ,expand = True , fill="both")


btn3 = Button(
    btnrow1 , 
    text = "3",
    font = ("verdana" ,22),
    relief ="groove",
    border = "0",
    command = three_isclicked,
        )
btn3.pack(side = LEFT ,expand = True , fill="both")

btn4 = Button(
    btnrow1 ,
    text = "+",
    font = ("verdana" ,22),
    relief ="groove",
    border = "0",
    command = plus_clicked,    
    )
btn4.pack(side = LEFT ,expand = True , fill="both")




btn5 = Button(
    btnrow2, 
    text = "4",
    font = ("verdana" ,22),
    relief ="groove",
    border = "0",   
    command = four_isclicked,
    )
btn5.pack(side = LEFT ,expand = True , fill="both")


btn6 = Button(
    btnrow2 , 
    text = "5",
    font = ("verdana" ,22),
    relief ="groove",
    border = "0",  
    command = five_isclicked,
    )
btn6.pack(side = LEFT ,expand = True , fill="both")



btn7 = Button(
    btnrow2 , 
    text = "6",
    font = ("verdana" ,22),
    relief ="groove",
    border = "0",
    command = six_isclicked, 
    )
btn7.pack(side = LEFT ,expand = True , fill="both")

btn8 = Button(
    btnrow2 , 
    text = "-",
    font = ("verdana" ,22), 
    relief ="groove",
    border = "0",
    command = minus_clicked,
    )
btn8.pack(side = LEFT ,expand = True , fill="both")



#for button 3
btn5 = Button(
    btnrow3, 
    text = "7",
    font = ("verdana" ,22), 
    relief ="groove",
    border = "0",
    command = seven_isclicked,
    )
btn5.pack(side = LEFT ,expand = True , fill="both")


btn6 = Button(
    btnrow3 , 
    text = "8",
    font = ("verdana" ,22), 
    relief ="groove",
    border = "0",
    command = eight_isclicked,
    )
btn6.pack(side = LEFT ,expand = True , fill="both")



btn7 = Button(
    btnrow3 , 
    text = "9",
    font = ("verdana" ,22), 
    relief ="groove",
    border = "0",
    command = nine_isclicked,    
    )
btn7.pack(side = LEFT ,expand = True , fill="both")

btn8 = Button(
    btnrow3 , 
    text = "*",
    font = ("verdana" ,22), 
    relief ="groove",
    border = "0",
    command = minus_clicked,
    
    )
btn8.pack(side = LEFT ,expand = True , fill="both")




#for button roww 4

btn5 = Button(
    btnrow4, 
    text = "C",
    font = ("verdana" ,22),  
    relief ="groove",
    border = "0",
    command = clear,
    )
btn5.pack(side = LEFT ,expand = True , fill="both")


btn6 = Button(
    btnrow4 , 
    text = "0",
    font = ("verdana" ,22), 
    relief ="groove",
    border = "0",
    command = zero_isclicked,
    )
btn6.pack(side = LEFT ,expand = True , fill="both")



btn7 = Button(
    btnrow4 , 
    text = "=",
    font = ("verdana" ,22), 
    relief ="groove",
    border = "0",
    command = equal_isclicked,
    )
btn7.pack(side = LEFT ,expand = True , fill="both")

btn8 = Button(
    btnrow4 , 
    text = "/",
    font = ("verdana" ,22), 
    relief ="groove",
    border = "0",
    command = divide_clicked,
    )
btn8.pack(side = LEFT ,expand = True , fill="both")

    


root.mainloop();