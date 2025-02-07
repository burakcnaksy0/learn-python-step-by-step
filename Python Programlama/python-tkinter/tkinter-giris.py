#Python'da Tkinter Nedir ?
#GUI yani Grafiksel Kullanici Arayüzü Uygulamari gelistirmek icin kutuphanedir
import tkinter as tk
#pencere window olusturma
root=tk.Tk()
root.title("Tkinter'e Giris")
#basit bir etiket olusturma
label=tk.Label(root,text="Tkinter ile ilk adim !")
label.pack()
root.mainloop()