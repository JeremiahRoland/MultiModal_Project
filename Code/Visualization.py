import pandas
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import seaborn as sns

data = pandas.read_csv("../Data/BC MASTER DATA ONLY_Updated OCT 2017.csv", sep=",")
print(data.dtypes)
print(data.Start_Time[1])
data.Start_Time = pandas.to_datetime(data.Start_Time, format='%m/%d/%y %H:%M')
print(data.Start_Time[1])
data["YEAR"] = data.Start_Time.dt.year
data["HOUR"] = data.Start_Time.dt.hour

header_list = ['Subscriber_ID', 'Member_Type', 'Unique', 'Trip_Duration', 'Bike_BC',
 'Start_Time', 'Start_Station_Name', 'Start_Station_ID',
 'End_Time', 'End_Station_Name', 'End_Station_ID', 'AC_Members', 'AM_PM', 'HOUR', 'DAY', 'MONTH', 'YEAR']

data = data.reindex(columns=header_list)
print(data.dtypes)

data.to_csv("../Data/Bike_Data.csv", sep=",")

print(data[0:1])

def graph_topten(column):
    stations = data[column].value_counts()
    top_ten_stations = stations[:10,]
    plt.figure()
    sns.barplot(top_ten_stations.index, top_ten_stations.values, alpha=0.8)
    plt.title("Top Ten Stations in Use: "+column)
    plt.ylabel("Number of Uses", fontsize=15)
    plt.xlabel("Station Name", fontsize=15)
    plt.xticks(rotation=90)
    plt.show()

def graph_time(column, xticks):
    time = data[column].value_counts()
    plt.figure()
    sns.barplot(time.index, time.values, alpha=0.8)
    plt.title("Bike Usage By: "+column)
    plt.ylabel("Number of Uses", fontsize=15)
    plt.xlabel(column, fontsize=15)
    xticks = xticks
    plt.xticks(range(0,len(xticks)), xticks)
    plt.show()

# graph_topten("Start_Station_Name")
# # graph_topten("End_Station_Name")
# graph_time("DAY", ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday'])
# graph_time("MONTH", ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
# graph_time("AM_PM", ['PM', 'AM'])

# print(data.MONTH.value_counts())
# bus8 = pandas.read_excel("../Data/Bus/route8.xlsx")
# print(bus8.columns.values)
# print(data.columns.values)

# print(data.DAY.unique())

# print(data.AC_Members.unique())

# print(data.AC_Members.value_counts())

# print(data.DAY.value_counts())

# print(data.Start_Station_Name.value_counts())

# print(data.Unique.value_counts())


