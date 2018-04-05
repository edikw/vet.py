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
    lembur =(int(entries["Jumlah lembur"].get()))
    gaji = lembur * 100000 * 7
    print "gaji mingguan anda : ", gaji
def gaji_perbulan(entries):
    bulan = gaji * 30
    print "gaji bulanan anda :", bulan

    
Button(master, text="Metu", command=master.quit).grid(row=5, column=0, sticky=W, pady=4)
Button(master, text="dudohno", command=show_entry_fields).grid(row=7, column=1, sticky=W, pady=4)

mainloop()
