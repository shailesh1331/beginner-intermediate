# with open('weather_data.csv') as file:
#     content=file.readlines()
# data=[]
# for lines in content:
#     data.append(lines.strip())
# print(data)



# csv file reader-------------------------------
# import csv
#
# with open('weather_data.csv') as file:
#     data=csv.reader(file)
#     tempratures=[]
#     x=0
#     for row in data:
#         if x==0:
#             x+=1
#             pass
#         else:
#             tempratures.append(int(row[x]))
#     print(tempratures)

# import pandas
# data=pandas.read_csv('weather_data.csv')
# tempratures=data['temp']
# max=tempratures.max()
# col=data[tempratures==max]
# print(col)
# monday=data[data['day']=='Monday']
# print(monday)
# print(monday['temp']*9/5+32)


# import pandas
#
# data={
#     'students':['amy','loda','lasan'],
#     'scores':[76,45,87]
# }
#
# new_data=pandas.DataFrame(data)
# new_data.to_csv('new_data')

import pandas

data=pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv')
colors=data['Primary Fur Color']
gray=[x for x in colors if x=="Gray"]
cinnamon=[x for x in colors if x=="Cinnamon"]
black=[x for x in colors if x=="Black"]
new_data={
    'COLOR':['Gray','Cinnamon','Yellow'],
    'COUNT':[len(gray),len(cinnamon),len(black)]
}
final_data=pandas.DataFrame(new_data)
final_data.to_csv('final_data')