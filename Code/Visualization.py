import pandas

data = pandas.read_csv("../Data/BC MASTER DATA ONLY_Updated OCT 2017.csv")

print(data.columns.values)

print(data.DAY.unique())

print(data.AC_Members.unique())

print(data.AC_Members.value_counts())

print(data.DAY.value_counts())

print(data.Start_Station_Name.value_counts())

print(data.Unique.value_counts())