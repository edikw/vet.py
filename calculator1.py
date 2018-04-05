import Tkinter
import tkMessageBox

def do_plus():
    plus = float(number_input1.get())+float(number_input2.get())
    tkMessageBox.showinfo("Plus = ", plus)

def do_minus():
    minus = float(number_input1.get())-float(number_input2.get())
    tkMessageBox.showinfo("Minus = ", minus)

def do_multiple():
    multiple = float(number_input1.get())*float(number_input2.get())
    tkMessageBox.showinfo("Multiple = ", multiple)

def do_divide():
    divide = float(number_input1.get())/float(number_input2.get())
    tkMessageBox.showinfo("Divide = ", divide)
    
def do_sqrt():
    root = float(number_input1.get())**0.5
    tkMessageBox.showinfo("Square Root = ", root)

def do_square():
    square = float(number_input1.get())**2
    tkMessageBox.showinfo("Square = ", square)

main_window = Tkinter.Tk()
main_window.title("Simple Calc")
number_input1 = Tkinter.Entry(main_window)
number_input2 = Tkinter.Entry(main_window)
button_sqrt = Tkinter.Button(main_window, text="Plus", command=do_plus)
button_sqrt.pack()
button_sqrt = Tkinter.Button(main_window, text="Minus", command=do_minus)
button_sqrt.pack()
button_sqrt = Tkinter.Button(main_window, text="Multiple", command=do_multiple)
button_sqrt.pack()
button_sqrt = Tkinter.Button(main_window, text="Divide", command=do_divide)
button_sqrt.pack()
button_sqrt = Tkinter.Button(main_window, text="Square Root", command=do_sqrt)
button_sqrt.pack()
button_square = Tkinter.Button(main_window, text="Square", command=do_square)
button_square.pack()
number_input1.pack()
number_input2.pack()

main_window.mainloop()
