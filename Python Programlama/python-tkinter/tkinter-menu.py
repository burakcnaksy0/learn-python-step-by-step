import tkinter as tk 

root=tk.Tk()
root.title("Menu Kullanimi")

def yeni_dosya():
    print("Yeni Dosya Acildi")

#menu olusturalim
menu_bar=tk.Menu(root)
root.config(menu=menu_bar) 

dosya_menu=tk.Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Dosya",menu=dosya_menu) 

dosya_menu.add_command(label="Yeni",command=yeni_dosya)

root.mainloop()  