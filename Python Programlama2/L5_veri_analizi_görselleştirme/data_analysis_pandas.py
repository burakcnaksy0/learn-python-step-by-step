import pandas as pd
import numpy as np
import seaborn as sns

np_array = np.arange(10)
np_array1 = np.arange(10, 20)

tuple_array = {"column1": np_array, "column2": np_array1}
pd_frame = pd.DataFrame(tuple_array)
# print(pd_frame)

pd_frame["total"] = pd_frame["column1"] + pd_frame["column2"]  # dataframe'e yeni sütun ekleme
# print(pd_frame)

pd_frame.drop("total", axis=1, inplace=True)  # dataframeden silme işlemi
# print(pd_frame)


np_Random_array = np.random.randint(1, 30, (5, 3))
pdata_frame = pd.DataFrame(np_Random_array, columns=["columns1", "columns2", "columns3"])
# print(pdata_frame)

# print(pdata_frame.iloc[0:3])
# print(pdata_frame.loc[0:3])

df9 = sns.load_dataset("planets")
'''
print(df9)
print(df9['method'].unique())
print(df9['year'].max())

print(df9.groupby("method")["orbital_period"].aggregate([min,np.mean,max]))
'''
df10 = pd.DataFrame([100, 500, 250, 400, 200], columns=["Prices"])
print(df10)
print("************************")


def coupon(price):
    return price - price * 0.05


print(df10["Prices"].apply(coupon))  # apply fonk. kullanımı
print("************************")
print(df10["Prices"].apply(lambda fiyat: fiyat - fiyat * 0.1))
