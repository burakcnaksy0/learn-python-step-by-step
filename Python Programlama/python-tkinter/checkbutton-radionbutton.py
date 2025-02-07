import tkinter as tk 

root=tk.Tk()
root.title("Checkbutton & Radiobutton")

#checkbutton olusturma
check_var=tk.IntVar()
check_button=tk.Checkbutton(root,text="Sec",variable=check_var)
check_button.pack()

#radiobutton olusturma
radio_var=tk.IntVar()
radio1=tk.Radiobutton(root,text="Secim1",variable=radio_var,value=1)
radio2=tk.Radiobutton(root,text="Secim2",variable=radio_var,value=2)
radio1.pack()
radio2.pack()

root.mainloop()