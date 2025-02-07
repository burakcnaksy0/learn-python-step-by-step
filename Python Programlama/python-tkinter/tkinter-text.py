import tkinter as tk 

root=tk.Tk()
root.title("Text Kullanimi")

#Text Widget Olusturalim
text_widget=tk.Text(root,height=10,width=50)
text_widget.pack(pady=20)

root.mainloop()