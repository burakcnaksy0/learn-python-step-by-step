import tkinter as tk 

root=tk.Tk()
root.title("Scrollbar Kullanimi")

#text widget ve scrollbar ekleme islemi
text_widget=tk.Text(root,height=20,width=10)
text_widget.pack(side=tk.LEFT)

scrollbar=tk.Scrollbar(root,command=text_widget.yview)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

text_widget.config(yscrollcommand=scrollbar.set)

root.mainloop()
