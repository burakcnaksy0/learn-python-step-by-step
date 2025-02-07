import tkinter as tk

root=tk.Tk()
root.title("Buton Olusturma")

def tiklandi():
    print("Butona tiklandi !")
#buton ekleme islemi
button=tk.Button(root,text="Click",command=tiklandi)
button.pack(pady=20)
root.mainloop()
    