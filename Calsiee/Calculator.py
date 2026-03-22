import tkinter

button_values = [["AC","+/-","%","/"],
                 ["7","8","9","x"],
                 ["4","5","6","-"],
                 ["1","2","3","+"],
                 ["0",".","!","="]]
right_symbols=["/","x","-","+","="]
top_symbols=["AC","+/-","%","/"]

row_count=len(button_values)#5
colomn_count=len(button_values[0])


light="#E0BBE4"
dark="#D291BC"
darker="#957DAD"
white="white"
black="#1C1C1C"

#window
window=tkinter.Tk()
window.title("Calsiee")
window.resizable(False,False)


frame=tkinter.Frame(window)
label=tkinter.Label(frame,text="0",font=("Arial", 45),background=black,
                    foreground=white,anchor="e",width=colomn_count)
frame.pack()

label.grid(row=0,column=0,columnspan=colomn_count,sticky="we")

for row in range (row_count):
    for column in range (colomn_count):
        value=button_values[row][column]
        button=tkinter.Button(frame,text=value,font=("Arial",30),
                              width=colomn_count-1,height=1,
                              command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground=black,background=dark)
        elif value in right_symbols:
            button.config(foreground=white,background=darker)
        else:
            button.config(foreground=white,background=light)
        
        button.grid(row=row+1,column=column)
frame.pack()

#A+B,A-B,A*B,A/B
A="0"
operator=None
B=None

def clear_all():
    global A,B,operator
    A="0"
    operator=None
    B=None

def remove_zero_decimal(num):
    if num %1 ==0:
        num=int(num)
    return str(num)



def button_clicked(value):
    global right_symbols,top_symbols , label,A,B,operator
    if value in right_symbols:
        if value=="=":
            if A is not None and operator is not None:
                B=label["text"]
                numA=float(A)
                numB=float(B)

                if operator=="+":
                    label["text"]=remove_zero_decimal(numA+numB)
                elif operator=="-":
                    label["text"]=remove_zero_decimal(numA-numB)
                elif operator=="x":
                    label["text"]=remove_zero_decimal(numA*numB)
                elif operator=="/":
                    if numB== 0:
                        label["text"]="Error"
                    else:
                        label["text"]=remove_zero_decimal(numA/numB)
                clear_all()

        elif value in "+-*/":
            if operator is None:
                A=label["text"]
                label["text"]="0"
                B="0"

            operator=value
        
    elif value in top_symbols:
        if value=="AC":
            clear_all()
            label["text"]="0"
        elif value=="+/-":
            result=float(label["text"])*-1
            label["text"]=remove_zero_decimal(result)
        elif value=="%":
            result=float(label["text"])/100
            label["text"]=remove_zero_decimal(result)
    else:
        if value==".":
            if value not in label["text"]:
                label["text"]+=value
        elif value in "0123456789":
            if label["text"]=="0":
                label["text"]=value
            else:
                label["text"]+=value


#center the window
window.update()
window_height=window.winfo_height()
window_width=window.winfo_width()
screen_height=window.winfo_screenheight()
screen_width=window.winfo_screenwidth()

window_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_height/2)-(window_height/2))

#format"(W)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()