import tkinter as tk

root=tk.Tk()
root.title("Yazi Bicimlendirme")

#etiket yazisini bicimlendir
label=tk.Label(root,text="Bicimlendir Yazi",font=("Arial",18,"bold"),fg="red")
label.pack(pady=20)

root.mainloop()