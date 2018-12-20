import pandas
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import seaborn as sns

data = pandas.read_csv("../Data/Bike_Data.csv", sep=",")

# print(data.dtypes)
# print(data.Start_Time[1])
# data.Start_Time = pandas.to_datetime(data.Start_Time, format='%m/%d/%y %H:%M')
# print(data.Start_Time[1])
# data["YEAR"] = data.Start_Time.dt.year
# data["HOUR"] = data.Start_Time.dt.hour
# header_list = ['Subscriber_ID', 'Member_Type', 'Unique', 'Trip_Duration', 'Bike_BC',
#  'Start_Time', 'Start_Station_Name', 'Start_Station_ID',
#  'End_Time', 'End_Station_Name', 'End_Station_ID', 'AC_Members', 'AM_PM', 'HOUR', 'DAY', 'MONTH', 'YEAR']
# data = data.reindex(columns=header_list)
# print(data.dtypes)
# data.to_csv("../Data/Bike_Data.csv", sep=",")

def graph_monthyear():
    monthyear = pandas.crosstab(data.MONTH,data.YEAR)
    ax = monthyear.plot(kind='line', linewidth=4, cmap='Set3')
    plt.xlabel("Month")
    plt.ylabel("Rentals")
    ticks = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    plt.xticks(range(1,len(ticks)), ticks)
    leg = ax.legend()
    for line in leg.get_lines():
        line.set_linewidth(10.0)
    ax.set_facecolor('grey')
    plt.title("Monthly Bike Rentals by Year")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def graph_monthday():

    monthyear = pandas.crosstab(data.WEEKDAY,data.MONTH)
    ax = monthyear.plot(kind='line', linewidth=4, cmap='Paired')
    leg = ax.legend(labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] )
    for line in leg.get_lines():
        line.set_linewidth(10.0)
    ax.set_facecolor('grey')
    plt.xlabel("Day")
    plt.ylabel("Rentals")
    ticks = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday']
    plt.xticks(range(1,len(ticks)+1), ticks)
    plt.title("Daily Bike Rentals by Month")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

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

graph_monthyear()
# graph_topten("Start_Station_Name")
# graph_topten("End_Station_Name")
# graph_time("WEEKDAY", ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday'])
# graph_time("MONTH", ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
# graph_time("AM_PM", ['PM', 'AM'])
# graph_time('HOUR', [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23] )
# graph_time('YEAR', [2012,2013,2014,2015,2016,2017])
# graph_time('Member_Type', ['Customer', 'Subscriber', '24 Hour', 'Annual - Exp 5 Sep', 'Annual', 'Dependent', 'UTC Students', 'Test'])

# bus8 = pandas.read_excel("../Data/Bus/route8.xlsx")
# print(bus8.columns.values)




# print(data.AC_Members.unique())
# print(data.AC_Members.value_counts())
# print(len(data.AC_Members))
# print(data.DAY.value_counts())
# print(data.Start_Station_Name.value_counts())
# print(data.Start_Station_ID.value_counts())
# print(data.Unique.value_counts())


