import tkinter as tk
app = tk.Tk(screenName='PythonClass', baseName='class')


app.title('Counting Seconds')
# app.geometry("400x400")
# button1 = tk.Button(app, text='1', width=10, command=app.destroy, bg='red')

text_area = tk.Text(app, height=5, width=40, borderwidth=2, pady=2, padx=5)
text_area.grid(columnspan=5)

text = ""


def add_button_to_field(textButton):
    try:
        global text
        text+=textButton
        text_area.delete(1.0, 'end')
        text_area.insert(1.0, text)
        print(text)
    
    except:
        text = "Error"
        text_area.delete(1.0, 'end')
        text_area.insert("1.0", text)
        print("Error occured")
        pass


def clear():
    global text
    text = ""
    text_area.delete(1.0, 'end')
    text_area.insert(1.0, text)

buttonClear = tk.Button(app, text='C', width=10, command=lambda: clear())
    
button1 = tk.Button(app, text='1', width=10, command=lambda: add_button_to_field('1'))
button2 = tk.Button(app, text='2', width=10, command=lambda: add_button_to_field('2'))
button3 = tk.Button(app, text='3', width=10, command=lambda: add_button_to_field('3'))

button4 = tk.Button(app, text='4', width=10, command=lambda: add_button_to_field('4'))
button5 = tk.Button(app, text='5', width=10, command=lambda: add_button_to_field('5'))
button6 = tk.Button(app, text='6', width=10, command=lambda: add_button_to_field('6'))

button7 = tk.Button(app, text='7', width=10, command=lambda: add_button_to_field('7'))
button8 = tk.Button(app, text='8', width=10, command=lambda: add_button_to_field('8'))
button9 = tk.Button(app, text='9', width=10, command=lambda: add_button_to_field('9'))

button0 = tk.Button(app, text='0', width=10, command=lambda: add_button_to_field('0'))
buttonMinus = tk.Button(app, text='-', width=10, command=lambda: add_button_to_field('-'))
buttonDiv = tk.Button(app, text='/', width=10, command=lambda: add_button_to_field('/'))
buttonEqu = tk.Button(app, text='=', width=10, command=lambda: add_button_to_field('='))
buttonDot = tk.Button(app, text='.', width=10, command=lambda: add_button_to_field('.'))
buttonMut = tk.Button(app, text='*', width=10, command=lambda: add_button_to_field('*'))
buttonAdd = tk.Button(app, text='+', width=10, command=lambda: add_button_to_field('+'))

button7.grid(row=1, column=1)
button8.grid(row=1, column=2)
button9.grid(row=1, column=3)
buttonMut.grid(row=1, column=4)
button1.grid(row=2, column=1)
button2.grid(row=2, column=2)
button3.grid(row=2, column=3)
buttonAdd.grid(row=2, column=4)
button4.grid(row=3, column=1)
button5.grid(row=3, column=2)
button6.grid(row=3, column=3)
buttonMinus.grid(row=3, column=4)
button0.grid(row=4, column=1)
buttonDiv.grid(row=4, column=2)
buttonDot.grid(row=4, column=3)
buttonEqu.grid(row=4, column=4)
buttonClear.grid(row=5, column=1)

text_area2 = tk.Text(app, height=1, width=40)
text_area2.grid(columnspan=5)


app.mainloop()



def sentence(name):
    age = 30
    print(f"hello{name}, is {age} years old")
    
sentence(Grace)