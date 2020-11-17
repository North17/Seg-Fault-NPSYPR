import pandas as pd 
from matplotlib import pyplot as plt 
from data import ages

ctrstr = "0-01d00-189-2040-050101"

params = ctrstr.split('-')

x = int(params[0])                      #x

percbool = False
if 'd' in params[1]:                    #2 ys
    params[1] = params[1].split('d')
    y1q = int(params[1][0][0])
    y1c = int(params[1][0][1])
    y2q = int(params[1][1][0])
    y2c = int(params[1][1][1])
    percbool = True
else:
    yq = int(params[1][0])              #single y
    yc = int(params[1][1])
    percbool = False

zone = int(params[2])                   #zone
if zone == 400:
    allzones = True
else:
    allzones = False

age_start = int(params[3][:2])          #ages
age_end = int(params[3][2:])

time_start = int(params[4][:3])         #times
time_end = int(params[4][3:])           



if x == 0:
    agekey = ages.ages
    x_axis = range(age_start, age_end)


y_axis = []
num = []
denom = []
#for single parameter:
if percbool == False:
    for i in x_axis:
        if yc == 0:
            y_axis.append(ages.ages[i]['total'][yq])
        if yc == 1:
            y_axis.append(ages.ages[i]['db'][yq])
        if yc == 2:
            y_axis.append(ages.ages[i]['ri'][yq])
        if yc == 3:
            y_axis.append(ages.ages[i]['bp'][yq])
        if yc == 4:
            y_axis.append(ages.ages[i]['two'][yq])
        if yc == 5:
            y_axis.append(ages.ages[i]['three'][yq])
       
else:
    for i in x_axis:
        if y1c == 0:
            num.append(ages.ages[i]['total'][y1q])
        if y1c == 1:
            num.append(ages.ages[i]['db'][y1q])
        if y1c == 2:
            num.append(ages.ages[i]['ri'][y1q])
        if y1c == 3:
            num.append(ages.ages[i]['bp'][y1q])
        if y1c == 4:
            num.append(ages.ages[i]['two'][y1q])
        if y1c == 5:
            num.append(ages.ages[i]['three'][y1q])
    for i in x_axis:
        if y2c == 0:
            denom.append(ages.ages[i]['total'][y2q])
        if y2c == 1:
            denom.append(ages.ages[i]['db'][y2q])
        if y2c == 2:
            denom.append(ages.ages[i]['ri'][y2q])
        if y2c == 3:
            denom.append(ages.ages[i]['bp'][y2q])
        if y2c == 4:
            denom.append(ages.ages[i]['two'][y2q])
        if y2c == 5:
            denom.append(ages.ages[i]['three'][y2q])
        

#finding list for percentage
for i in range(len(x_axis)):
    y_axis.append((num[i]/denom[i])*100)

print(y_axis)
plt.plot(x_axis,y_axis)
plt.show()