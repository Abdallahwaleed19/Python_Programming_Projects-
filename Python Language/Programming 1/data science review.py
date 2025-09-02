import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sn
# data = {
#     "first score": [20, 23, np.nan, 34, 34],
#     "second score": [22, 45, 12, 13, np.nan],
#     "third score": [34, 23, 45, 67, np.nan],
#     "fourth score": [np.nan, np.nan, np.nan, np.nan, 89]
# }
# df = pd.DataFrame(data)
# print("Original DataFrame:")
# print(df)
# print("="*50)
# df["first score"].fillna(df["first score"].mean(), inplace=True)
# df["second score"].fillna(0, inplace=True)
# df["third score"].fillna(df["third score"].median(), inplace=True)
# df.dropna(subset=["fourth score"], inplace=True)
# print("Modified DataFrame:")
# print(df)
# df["Average score"] = df[["first score" , 'second score' , 'third score']].mean(axis=1).fillna(0)
# print(df) 


# data_prices = {'Price': [4, 8, 9, 15, 21, 21, 24, 25, 26, 28, 29, 34]}
# df_prices = pd.DataFrame(data_prices)
# print("\nOriginal prices:\n",df_prices)
# df_prices = df_prices.sort_values(by='Price').reset_index(drop=True)
# bins = pd.qcut(df_prices['Price'], 3, labels=False)
# df_prices['Price_Mean_Smooth'] = df_prices.groupby(bins)['Price'].transform('mean')
# print("\nSmoothing by bin means:\n",df_prices)
# df_prices['Price_Boundary_Smooth'] = df_prices.groupby(bins)['Price'].transform(lambda x: pd.Series([x.min() if value <= x.median() else x.max() for value in x]))
# print("\nSmoothing by bin boundaries:\n", df_prices)


# employee_data = {
#     'Name': ['Donna', 'Lois', 'Matthew', 'Joshua', np.nan, 'John'],
#     'Gender': ['Female', np.nan, 'Male', np.nan, 'Male', 'Male'],
#     'Date': ['7/22/2010', '4/22/1995', '9/5/1995', '3/8/2012', '6/14/2012', '7/1/1992'],
#     'Time': ['3:48 AM', '7:18 PM', '2:12 AM', '1:58 AM', '4:19 PM', '10:08 PM'],
#     'Salary': [81014, 64714, 100612, 90816, 125792, 97950],
#     'Bonus': [1.894, 4.934, 13.645, 18.816, 5.042, 13.873],
#     'Active': [False, True, False, True, np.nan, False],
#     'Department': ['Product', 'Legal', 'Marketing', 'Client Services', np.nan, 'Client Services']
# }
# df = pd.DataFrame(employee_data)
# print(df) 
# print('='*100)
# df["Gender"].fillna("No Gender" , inplace=True)
# df.dropna(inplace=True)
# print(df)

# df = pd.read_csv("اسم الملف .csv")
# plt.figure(figsize=(10,6))
# plt.scatter(df["x"] , df["y"] , alpha= 0.5)
# plt.title("اي عنوان بقا ")
# plt.xlabel("اسم المحور الاول ")
# plt.ylabel("اسم المحور الثاني ")
# plt.show()

# df = pd.read_csv("اسم الملف .csv")
# df_num = df["t" , "y" , "u" , "r"]
# corr = df_num.corr()
# plt.figure(figsize=(10,6))
# sn.heatmap(corr , annot=True , cmap="coolwarm" , vmin= -1 , vmax= 1)


# df = pd.read_csv("اسم الملف .csv")
# plt.figure(figsize = (10,6))
# plt.scatter(df["income"] , df["age"] , alpha= 0.5)
# plt.title("اي عنوان بقا ")
# plt.xlabel("اسم المحور الاول ")
# plt.ylabel("اسم المحور الثاني ")
# plt.show()


# df = pd.read_csv("اسم الملف .csv")
# plt.figure(figsize = (10,6))
# plt.scatter(df["Temp"] , df["ice cream sales"] , alpha = 0.5)
# plt.title("اي عنوان بقا ")
# plt.xlabel("اسم المحور الاول ")
# plt.ylabel("اسم المحور الثاني ")
# plt.show()


