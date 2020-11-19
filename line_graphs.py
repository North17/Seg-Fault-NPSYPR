import pandas as pd 
from matplotlib import pyplot as plt 
from data import get_data

ctrstr = "2-3-0-400-0090-000239"

params = ctrstr.split('-')

x = int(params[0])                      #x

y = int(params[1])                      #y

cond = int(params[2])                   #conditions

zone = int(params[3])                   #zone

age_start = int(params[4][:2])          #ages
age_end = int(params[4][2:])

time_start = int(params[5][:3])         #times
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

if cond == 0:
    cond = 'total'
elif cond == 1:
    cond = 'db'
elif cond == 2:
    cond = 'ri'
elif cond == 3:
    cond = 'bp'
elif cond == 4:
    cond = 'two'
elif cond == 5:
    cond = 'three'

#X Labels
if x == 0:
    xl = "Ages"
elif x == 1:
    xl = "Time Infected"
elif x == 2:
    xl = "Population Density"

#Y Labels
if y == 0:
    yl = "Cases"
elif y == 1:
    yl = "Deaths"
elif y == 2:
    yl = 'Fatality Rate'
elif y == 3:
    yl = 'Infection Rate'
elif y == 4:
    yl = "Recovery Rate"


sum =  0
num = []
denom = []

try:
    # Ages as x axis
    if x == 0:
        if y == 0:
            for i in x_axis:
                for j in range(time_start, time_end):
                    sum += reqlist[i]['time_infected'][j][cond][0]
                y_axis.append(sum)
                sum = 0
        elif y == 1:
            for i in x_axis:
                for j in range(time_start, time_end):
                    sum += reqlist[i]['time_infected'][j][cond][1]
                y_axis.append(sum)
                sum = 0
        elif y == 2:
            for i in x_axis:
                for j in range(time_start, time_end):
                    sum += reqlist[i]['time_infected'][j][cond][1]
                num.append(sum)
                sum = 0
            for i in x_axis:
                for j in range(time_start, time_end):
                    sum += reqlist[i]['time_infected'][j][cond][0]
                denom.append(sum)
                sum = 0
            for i in range(len(x_axis)):
                y_axis.append((num[i]/denom[i])*100)

        elif y == 4:
            for i in x_axis:
                for j in range(time_start, time_end):
                    sum += (reqlist[i]['time_infected'][j][cond][0] - reqlist[i]['time_infected'][j][cond][1])
                num.append(sum)
                sum = 0
            for i in x_axis:
                for j in range(time_start, time_end):
                    sum += reqlist[i]['time_infected'][j][cond][0]
                denom.append(sum)
                sum = 0
            for i in range(len(x_axis)):
                y_axis.append((num[i]/denom[i])*100)

    # Time Infected as X Axis

    if x ==1:
        if y == 0:
            for i in x_axis:
                for j in range(age_start, age_end):
                    sum += reqlist[i]['ages'][j][cond][0]
                y_axis.append(sum)
                sum = 0
        elif y == 1:    
            for i in x_axis:
                for j in range(age_start, age_end):
                    sum += reqlist[i]['ages'][j][cond][1]
                y_axis.append(sum)
                sum = 0
        elif y == 2:
            for i in x_axis:
                for j in range(age_start, age_end):
                    sum += reqlist[i]['ages'][j][cond][1]
                num.append(sum)
                sum = 0
            for i in x_axis:
                for j in range(age_start, age_end):
                    sum += reqlist[i]['ages'][j][cond][0]
                denom.append(sum)
                sum = 0
            for i in range(len(x_axis)):
                y_axis.append((num[i]/denom[i])*100)

        elif y == 4:
            for i in x_axis:
                for j in range(age_start, age_end):
                    sum += (reqlist[i]['ages'][j][cond][0] - reqlist[i]['ages'][j][cond][1])
                num.append(sum)
                sum = 0
            for i in x_axis:
                for j in range(age_start, age_end):
                    sum += reqlist[i]['ages'][j][cond][0]
                denom.append(sum)
                sum = 0
            for i in range(len(x_axis)):
                y_axis.append((num[i]/denom[i])*100)

    # Population Density as X Axis

    filter_by, filterl, filteru = 'ages', age_start, age_end

    if time_start != 0 or time_end != 239:
        filter_by, filterl, filteru = 'time_infected', time_start, time_end

    pop_index = list(range(len(x_axis)))
    if x == 2:
        if y == 0:
            for i in pop_index:
                for j in range(filterl, filteru):
                    sum += reqlist[i][filter_by][j][cond][0]
                y_axis.append(sum)
                sum = 0
        elif y == 1:
            for i in pop_index:
                for j in range(filterl, filteru):
                    sum += reqlist[i][filter_by][j][cond][1]
                y_axis.append(sum)
                sum = 0
        elif y == 2:
            for i in pop_index:
                for j in range(filterl, filteru):
                    sum += reqlist[i][filter_by][j][cond][1]
                num.append(sum)
                sum = 0
            for i in pop_index:
                for j in range(filterl, filteru):
                    sum += reqlist[i][filter_by][j][cond][0]
                denom.append(sum)
            for i in pop_index:    
                y_axis.append((num[i]/denom[i])*100)
                
        elif y == 3:
            for i in pop_index:
                for j in range(filterl, filteru):
                    sum += reqlist[i][filter_by][j][cond][0]
                num.append(sum)
                sum = 0
            for i in pop_index:
                denom.append(reqlist[i]['population'])
            for i in pop_index:
                y_axis.append(num[i]/denom[i])
        elif y == 4:
            for i in pop_index:
                for j in range(filterl, filteru):
                    sum += (reqlist[i][filter_by][j][cond][0] - reqlist[i][filter_by][j][cond][1])
                num.append(sum)
                sum = 0
            for i in pop_index:
                for j in range(filterl, filteru):
                    sum += reqlist[i][filter_by][j][cond][0]
                denom.append(sum)
                sum = 0
            for i in pop_index:
                y_axis.append((num[i]/denom[i])*100)
    
    
    # Finally Plotting:
    
    plt.plot(x_axis, y_axis, color = '#5D001E')

    plt.xlabel(xl)
    plt.ylabel(yl)

    plt.savefig("InfectionVsPopDensity")
    plt.show()
except:
    print("lol idk")

    