import tkinter as tk 

root=tk.Tk()
root.title("Listbox Kullanimi")

listbox=tk.Listbox(root)
listbox.pack()
#for dongusu ile listbox'a veri ekleme islemi
for player in ["Ronaldo","Messi","Mbabpe","M.Salah","R.Lewandowski"]:
    listbox.insert(tk.END,player)

root.mainloop()    