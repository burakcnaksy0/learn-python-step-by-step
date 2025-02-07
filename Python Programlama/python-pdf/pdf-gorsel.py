import fitz#PyMuPDF

#pdf dosyasini at
pdf_document=fitz.open('python_programlama.pdf')

#pdf dosyasini gorsele donusturelim
for page_number in range(len(pdf_document)):
    page=pdf_document.load_page(page_number)#bulundugu sayfayi yukler
    pix=page.get_pixmap()#pixel pixel goruntuye cevirme islemi
    pix.save(f'page_{page_number+1}.png')

print("PDF basarili bir sekilde gorsele donusturuldu Tebrikler.")    