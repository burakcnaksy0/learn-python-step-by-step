import tkinter as tk 

root=tk.Tk()
root.title("Pencere Bicimlendirme")

#penceremizin boyutlarini ayarlama
root.geometry("400x300")
label=tk.Label(root,text="Tkinter ile Arkaplan rengi Acik Mavi 400x300 boyutunda bir form ekrani")
label.pack()
root.config(bg="lightblue")

root.mainloop()