import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = sns.load_dataset('titanic')

print(df.head(10))
print(df.info())

# bar plot -> Çubukların yüksekliği, belirli bir kategorinin değerini veya ortalamasını gösterir.

mean = df.groupby("class", observed=True)["fare"].mean()
print(mean)

mean1 = df[(df["class"] == "First") & (df["who"] == "woman")]["fare"].mean()
print(mean1)

bar_plot = sns.barplot(x="class", y="fare", hue="who", data=df, palette="Reds")
# plt.show()

# count plot -> Kategorik değişkenlerin frekansını gösterir.

count_class = df.groupby("class", observed=True).count()
print(count_class)

count_who = df[(df["class"] == "Second") & (df["who"] == "man")]["fare"].count()
print(count_who)

cnt_plot = sns.countplot(x="class", hue="who", data=df, palette="Set3")
plt.show()

# box plot -> Veri setinin dağılımını, medyanını, çeyrek değerlerini ve uç değerlerini gösterir.

descr = df[(df["class"] == "First") & (df["who"] == "woman")]["fare"].describe()
print(descr)
box_plot = sns.boxplot(x="class", y="fare", hue="who", data=df)
plt.show()

# swarm plot -> Veri yoğunluğunu anlamak için kullanılır.

swarm_plot = sns.swarmplot(x="who", y="fare", hue="class", data=df)
plt.show()

# joint plot -> İki değişken arasındaki ilişkiyi ve dağılımı gösterir.

joint_plot = sns.jointplot(x="age", y="fare", kind="hex", data=df)
plt.show()

# point plot -> Kategorik değişkenlerin ortalamalarını noktalar halinde gösterir.

mean2 = df.groupby("who")["fare"].mean()
print(mean2)
point_plot = sns.pointplot(x="who", y="fare", data=df)
plt.show()

# LM plot -> İki değişken arasındaki doğrusal ilişkiyi göstermek için kullanılır.

lm_plot = sns.lmplot(x="age", y="fare", hue="class", col="who", row="alone", data=df)
plt.show()

# KDE plot -> Veri setinin yoğunluk dağılımını gösterir. sayısal

kde_plot = sns.kdeplot(x="fare", hue="class", data=df, multiple="stack")
plt.show()

# violin plot -> Verinin dağılımını ve yoğunluğunu gösterir.

violin_plot = sns.violinplot(x="class", y="fare", hue="who", data=df)
plt.show()
