import tkinter as tk 
from tkinter import messagebox

root=tk.Tk()
root.title("Messagebox Kullanimi")

def uyar():
    messagebox.showinfo("Bilgi","Bu bir Python Programalama bildirim mesajidir")

#buton ile mesaj kutusu acma
button=tk.Button(root,text="Mesaj Goster",command=uyar)
button.pack(pady=20)

root.mainloop()