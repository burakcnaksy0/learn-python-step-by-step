import tkinter as tk
from tkinter import messagebox

# Pencere oluşturma
root = tk.Tk()
root.title("Basit Masaüstü Uygulaması")
root.geometry("300x200")  # Pencere boyutu

# Etiket (Label) oluşturma
label = tk.Label(root, text="İsminizi girin:")
label.pack(pady=10)  # Pencereye yerleştirme

# Metin giriş kutusu (Entry) oluşturma
entry = tk.Entry(root)
entry.pack(pady=10)

# Buton tıklama fonksiyonu
def on_button_click():
    name = entry.get()  # Kullanıcının girdiği metni al
    if name:  # Eğer metin girilmişse
        messagebox.showinfo("Merhaba", f"Merhaba, {name}!")
    else:  # Eğer metin girilmemişse
        messagebox.showwarning("Uyarı", "Lütfen bir isim girin!")

# Buton oluşturma
button = tk.Button(root, text="Tıkla", command=on_button_click)
button.pack(pady=10)

# Pencereyi çalıştırma
root.mainloop()