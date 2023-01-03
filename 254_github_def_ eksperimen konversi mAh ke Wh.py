from tkinter import *
from tkinter import LEFT, RIGHT
 
window = Tk(className="")
window.title("Konversi Baterai")
window.geometry('350x200')

jud = Label(window, text="Konversi Baterai", font=('Arial',14))
jud.grid(column=1, row=0, columnspan=1)
des = Label(window, text="Perhitungan Konversi mAh ke Wh")
des.grid(column=1, row=1, columnspan=1)

lbl = Label(window, text="Arus Jam (Ah): ",anchor="e",width=20)
lbl.grid(column=0, row=2)
nilai1 = Entry(window,width=10)
nilai1.grid(column=1,row=2)

lbl = Label(window, text="Tegangan (V): ",anchor="e",width=20)
lbl.grid(column=0, row=3)
nilai2 = Entry(window,width=10)
nilai2.grid(column=1,row=3)
 
def kali():
    hasil.configure(text=(float(nilai1.get())*float(nilai2.get())))

btn3 = Button(window, text="Hitung", command=kali)
btn3.grid(column=1, row=4)

lbl3 = Label(window, text="Daya Jam (Wh) : ",anchor="e",width=20)
lbl3.grid(column=0, row=5)

hasil = Label(window, text="0",anchor="w",width=10)
hasil.grid(column=1, row=5)
 
 
window.mainloop()
 
