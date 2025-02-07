import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")
df = df.iloc[:, 1:]
print(df['Value'].head())

# fiyat önişleme

df['Value'] = df['Value'].str.replace('€', '').str.replace('M', ' 1000000').str.replace('K', ' 1000')
# print(df['Value'].head())

df['Value'] = df['Value'].str.split(' ', expand=True)[0].astype(float) * df['Value'].str.split(' ', expand=True)[1].astype(float)

# print(df['Value'].head())

df['Value'] = df['Value'].fillna(0).astype(np.float32)

# oyuncu pozisyon dağılımı (kategorik dağılım)

f, ax = plt.subplots(figsize=(12, 6))
count_plot1 = sns.countplot(x=df['Position'])
count_plot1.set_xlabel = ("Position")

# oyuncu yaş dağılımı (sayısal daağılım)

f1, ax1 = plt.subplots(figsize=(12, 6))
kde1_plot = sns.kdeplot(x=df['Age'])
kde1_plot.set_xlabel = ("Age")
# plt.show()

# oyuncuların kullandığı ayak bilgisine göre fiyata etkisi

print(df['Preferred Foot'].value_counts())

f2, ax2 = plt.subplots(figsize=(6,6))
bar_plot = sns.barplot(x=df['Preferred Foot'], y=df['Value'], data=df)
count_plot2 = sns.countplot(x=df['Preferred Foot'], data=df)
#plt.show()

# Oyuncuların Kullandıkları Ayak Bilgisi ve Oynadıkları Pozisyonun Fiyata Etkisi

f3,ax3 = plt.subplots(figsize = (6,6))
count1_plot1 = sns.countplot(x=df['Position'], hue=df['Preferred Foot'], data=df)
#plt.show()


# Uluslararası İtibar ve Oyuncu Potansiyel İlişkisi

f4,ax4 = plt.subplots(figsize = (6,6))
strip_plot = sns.stripplot(x=df['International Reputation'] ,y=df['Potential'],data=df)
#plt.show()

# Uluslararası İtibar ile Oyuncu Potansiyeli- Kullandığı Ayak Bilgisi İlişkisi

f5,ax5 = plt.subplots(figsize = (6,6))
strip1_plot = sns.stripplot(x=df['International Reputation'] ,y=df['Potential'],hue=df['Preferred Foot'],data=df)
#plt.show()

# Oyuncuların Potansiyelleri ve Güçleri Arasındaki İlişki

f6,ax6 = plt.subplots(figsize = (12,6))
line_1plot = sns.lineplot(x="Potential", y="Strength", data=df)
plt.show()

# Oyuncuların Potansiyelleri ile Kullandıkları Ayak Bilgisi Arasındaki İlişki








