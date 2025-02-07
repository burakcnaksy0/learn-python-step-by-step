import PyPDF2

# Birleştirilmek istenen PDF dosyalarını aç
pdf1_file = open('pdf1.pdf', 'rb')
pdf2_file = open('pdf2.pdf', 'rb')

# PyPDF2 ile PDF okuyucuları oluştur
reader1 = PyPDF2.PdfReader(pdf1_file)
reader2 = PyPDF2.PdfReader(pdf2_file)

# Yeni bir PDF yazıcı oluştur
pdf_writer = PyPDF2.PdfWriter()

# İlk PDF'den tüm sayfaları ekle
for page in reader1.pages:
    pdf_writer.add_page(page)

# İkinci PDF'den tüm sayfaları ekle
for page in reader2.pages:
    pdf_writer.add_page(page)

# Yeni bir PDF dosyasına kaydet
with open('birlesik.pdf', 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

pdf1_file.close()
pdf2_file.close()

print("PDF dosyaları başarıyla birleştirildi.")
