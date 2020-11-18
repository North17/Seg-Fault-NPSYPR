import pandas as pd 
from matplotlib import pyplot as plt 
from data import get_data

ctrstr = "0-2-0-189-2040-050101"

params = ctrstr.split('-')

x = int(params[0])                      #x

y = int(params[1])                      #y

cond = int(params[2])                   #conditions

zone = int(params[3])                   #zone

age_start = int(params[4][:2])          #ages
age_end = int(params[4][2:])

age_start = int(params[5][:3])         #times
time_end = int(params[5][3:])   


x_axis = []
y_axis = []
num = []
denom = []


reqlist = get_data.get(x, zone )

if x == 0:
    x_axis = range(age_start, age_end)
elif x == 1:
    x_axis = range(time_start, time_end)
elif x == 2:
    for i in range(len(reqlist)):
        x_axis.append(reqlist[i]['population'])

sum =  0
num = []
denom = []

# Ages as x axis

if x == 0:
    if y == 0:
        for i in x_axis:
            for j in range(time_start, time_end):
                sum += reqlist[i]['time_infected'][j]['total'][0]
            y_axis.append(sum)
            sum = 0
    elif y == 1:
        for i in x_axis:
            for j in range(time_start, time_end):
                sum += reqlist[i]['time_infected'][j]['total'][1]
            y_axis.append(sum)
            sum = 0
    elif y == 2:
        for i in x_axis:
            for j in range(time_start, time_end):
                sum += reqlist[i]['time_infected'][j]['total'][1]
            num.append(sum)
            sum = 0
        for i in x_axis:
            for j in range(time_start, time_end):
                sum += reqlist[i]['time_infected'][j]['total'][0]
            denom.append(sum)
            sum = 0
        for i in range(len(x_axis)):
            y_axis.append((num[i]/denom[i])*100)

    elif y == 4:
        for i in x_axis:
            for j in range(time_start, time_end):
                sum += (reqlist[i]['time_infected'][j]['total'][0] - reqlist[i]['time_infected'][j]['total'][1]]
            num.append(sum)
            sum = 0
        for i in x_axis:
            for j in range(time_start, time_end):
                sum += reqlist[i]['time_infected'][j]['total'][0]
            denom.append(sum)
            sum = 0
        for i in range(len(x_axis)):
            y_axis.append((num[i]/denom[i])*100)

# Time Infected as X Axis

if x ==1:
     if y == 0:
        for i in x_axis:
            for j in range(age_start, age_end):
                sum += reqlist[i]['time_infected'][j]['total'][0]
            y_axis.append(sum)
            sum = 0
    elif y == 1:
        for i in x_axis:
            for j in range(age_start, age_end):
                sum += reqlist[i]['time_infected'][j]['total'][1]
            y_axis.append(sum)
            sum = 0
    elif y == 2:
        for i in x_axis:
            for j in range(age_start, age_end):
                sum += reqlist[i]['time_infected'][j]['total'][1]
            num.append(sum)
            sum = 0
        for i in x_axis:
            for j in range(age_start, age_end):
                sum += reqlist[i]['time_infected'][j]['total'][0]
            denom.append(sum)
            sum = 0
        for i in range(len(x_axis)):
            y_axis.append((num[i]/denom[i])*100)

    elif y == 4:
        for i in x_axis:
            for j in range(age_start, age_end):
                sum += (reqlist[i]['time_infected'][j]['total'][0] - reqlist[i]['time_infected'][j]['total'][1]]
            num.append(sum)
            sum = 0
        for i in x_axis:
            for j in range(age_start, age_end):
                sum += reqlist[i]['time_infected'][j]['total'][0]
            denom.append(sum)
            sum = 0
        for i in range(len(x_axis)):
            y_axis.append((num[i]/denom[i])*100)










