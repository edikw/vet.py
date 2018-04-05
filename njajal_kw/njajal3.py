import Tkinter as tk
master = tk.Tk()

edi = "asuuu koe daaaaap"
msg = tk.Message(master, text = edi)
msg.config(bg="lightblue", font=("arial", 50, "italic"))
msg.pack()

tk.mainloop()
