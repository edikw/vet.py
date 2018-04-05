from Tkinter import *
master = Tk()

fields = ("Nama :","Alamat :","Pekerjaan :","Jabatan :","jumlah lembur : ","Gaji perminggu : ","Gajiperbulan : ")

Label(master, text="Nama : ").grid(row=0)
Label(master, text="Alamat : ").grid(row=1)
Label(master, text="Pekerjaan : ").grid(row=2)
Label(master, text="Jabatan : ").grid(row=3)
Label(master, text="jumlah lembur :").grid(row=4)
Label(master, text="Gaji perminggu :").grid(row=5)
Label(master, text="Gaji perbulan :").grid(row=6)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)
e6.grid(row=5,column=1)
e7.grid(row=6,column=1)

def gaji_mingguan(entries):
    lembur =(float(entries["Jumlah lembur"].get()))
    gaji = lembur * 100000 * 7
    print "gaji mingguan anda : ", gaji
    return gaji
def gaji_perbulan(entries):
    bulan = gaji * 30
    print "gaji bulanan anda :", bulan
    return bulan
def tampilan(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field, anchor="w")
        ent = Entry(row)
        ent.insert(0,"0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field]= ent
    
if__name__='__main__'
root = Tk()
ents = tampilan(root,fields)
root.bind("<Return>", (lambda event, e=ents: feetch(e)))
b1 = Button (root, text ="Gaji perminggu", command=(lambda e=ents:gaji_mingguan(e)))
b1.pack(side=LEFT, padx=30, pady=30)
b2 = Button (root, text = "Gaji perbualan" ,command =(lambda e=ents:gaji_perbulan(e)))
b2.pack(side=LEFT ,padx=5,pady=5)



mainloop()
