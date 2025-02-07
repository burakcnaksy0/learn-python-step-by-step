import sqlite3

# Veritabanı bağlantısı oluştur
conn = sqlite3.connect('veritabani.db')

# Bir cursor (imleç) oluştur
cursor = conn.cursor()

# Tablo oluşturma SQL sorgusu
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tablo (
        s1 TEXT,
        s2 TEXT,
        s3 TEXT,
        s4 TEXT,
        s5 TEXT
    )
''')

# Veritabanı bağlantısını kaydet (commit)
conn.commit()

# SQL sorgusu: Veritabanındaki "tablo" adlı tabloya veri ekleyelim
cursor.execute('INSERT INTO tablo (s1, s2, s3,s4,s5) VALUES (?, ?, ?,?,?)', ('python', 'java', 'flutter','node.js','linux'))

# Veritabanı bağlantısını kaydet (commit)
conn.commit()

# Veritabanı bağlantısını kapat
conn.close()