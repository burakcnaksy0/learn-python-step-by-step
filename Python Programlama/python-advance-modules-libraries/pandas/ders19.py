import pandas as pd
# Bir DataFrame oluşturun

data = {
    'Öğrenci': ['Ali', 'Ayşe', 'Mehmet', 'Zeynep', 'Ahmet'],
    'Not': [85, 90, 78, 92, 88],
    'Sınıf': [10, 11, 10, 12, 11]
}

df = pd.DataFrame(data)
# DataFrame'i ekrana yazdırın
print("Öğrenci Bilgileri:")
print(df)
# Sadece belirli bir sütunu seçin ve sıralayın
sorted_df = df[['Öğrenci', 'Not']].sort_values(by='Not', ascending=False)
# Sıralanmış DataFrame'i ekrana yazdırın
print("\nNotlara Göre Sıralanmış Öğrenci Bilgileri:")
print(sorted_df)