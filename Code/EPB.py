from datetime import datetime
import pandas
import numpy

dataset = pandas.ExcelFile("../Data/EPB_trips.xlsx")
Coolidge = pandas.read_excel(dataset, 'Coolidge')
# Pearl = pandas.read_excel(dataset, 'Pearl')
# Smokey = pandas.read_excel(dataset, 'Smokey')

# print(Coolidge.dtypes)

temp = pandas.DatetimeIndex(Coolidge['Date'])
Coolidge['Pickup_Date'] = temp.date
Coolidge['Pickup_Time'] = temp.time

print(Coolidge['Pickup_Date'][0])
print(Coolidge['Pickup_Time'][0])

Coolidge['Duration'] = pandas.to_timedelta(Coolidge['Duration'].astype(str))

# exit()

# Coolidge.rename(columns={'Date': 'Pickup_Date'}, inplace=True)
# header_list = ('TripId', 'Pickup_Date', 'Pickup_Time', 'Drop_Date','Drop_Time',
#     'Duration', 'Trip_Distance', 'Start_Odometer',
#     'End_Odometer', 'Electricity_Consumed', 'Total_Energy_Consumption', 'Start_SOC', 
#     'End_SOC', 'Ambient_Temperature', 'Average_Speed', 'Max_Speed', 'Auxiliary_Load',
#     '%_Hard_Acceleration', '%_Hard_Braking', '%_Time_Idle', 'Idle_Events')
# Coolidge = Coolidge.reindex(columns=header_list)

for i, value in enumerate(Coolidge.values[0:5]):
    # next three lines are a necessary workaround due to pandas error
    # print(Coolidge.columns.values)
    print(i)
    # endtime = Coolidge.Pickup_Date.values[i] + Coolidge.Duration.values[i]
    # endtime = endtime.astype(str)
    # print(endtime)
    # dateisthen = endtime.split('T',1)[0]
    # timeisthen = endtime.split('T',1)[1]
    # print(dateisthen, timeisthen)

    a = Coolidge.Date.values[i]
    endtime = Coolidge.Date.values[i] + Coolidge.Duration.values[i] # days, seconds, then other fields.
    # print(endtime)

    endtime = endtime.astype('str')
    dateisthen = endtime.split('T',1)[0]
    timeisthen = endtime.split('T',1)[1]
    timeisthen = timeisthen.split('.',1)[0]
    print(Coolidge.Pickup_Date.values[i], Coolidge.Pickup_Time.values[i])
    print(dateisthen, timeisthen)

# # endtime = (numpy.datetime64(endtime)).astype(datetime.datetime)

# ts = int(endtime)
# string_time = str(datetime.utcfromtimestamp(ts).strftime('%Y/%m/%d %H:%M'))

# print(string_time)
# print(a)
# print(b.time())
