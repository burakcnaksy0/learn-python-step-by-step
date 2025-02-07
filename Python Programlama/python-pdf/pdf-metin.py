import PyPDF2

#pdf dosyasini acalim
with open('python_programlama.pdf','rb') as pdf_file:
    reader=PyPDF2.PdfReader(pdf_file)
    
    #ilk sayfayi alalim
    page=reader.pages[0]
    page_text=page.extract_text()
    
    print("PDF'nin ilk sayfasindan alinan metin:",page_text)
    #print(page_text)