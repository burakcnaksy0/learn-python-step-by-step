import tkinter as tk 

root=tk.Tk()
root.title("Entry ile Veri Girisi")

def goster():
    print(entry.get())

entry=tk.Entry(root)
entry.pack(pady=10)

button=tk.Button(root,text="Goster",command=goster)
button.pack(pady=10)

root.mainloop()    