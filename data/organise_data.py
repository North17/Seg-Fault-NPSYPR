import pandas as pd
import copy

cases_csv = pd.read_csv('./given_files/COVID_Dataset.csv')
pop_csv = pd.read_csv('./given_files/Population.csv')

def get_ages(x = False, y = False):

    cases = cases_csv

    if x and y:
        cases = cases[cases['x location'] == x]
        cases = cases[cases['y location'] == y]
        
    #     for i in cases_csv.iloc:
    #         if i['x location'] == x and i['y location'] == y:
    #             cases.append(i)
    # else:
    #     cases = cases_csv.iloc

    ages = []

    empty = {
        'total': [0, 0],

        'db': [0, 0],

        'ri': [0, 0],

        'bp': [0, 0],

        'time_infected': [],
        # 'zones': []
    }

    for i in range(239):
        empty['time_infected'].append({
            'total': [0, 0],

            'db': [0, 0],

            'ri': [0, 0],

            'bp': [0, 0],
        })

    
    # for i in range(400):
    #     empty['zones'].append({
    #         'total': [0, 0],

    #         'db': [0, 0],

    #         'ri': [0, 0],

    #         'bp': [0, 0],
    #     })
    

    for i in range(90):
        ages.append(copy.deepcopy(empty))

    for i in cases.iloc:
        if x and y and not(i['x location'] == x and i['y location'] == y):
            continue
        
        age = i['Age']
        db = int(i['Diabetes'])
        ri = int(i['Respiratory Illnesses'])
        bp = int(i['Abnormal Blood Pressure'])
        dead = i['Outcome'] == 'Dead'

        # x = i['x location']
        # y = i['y location']
        # zone = 20*y + x - 21

        time = i['Time of Infection']

        ages[age]['total'][0] += 1
        ages[age]['time_infected'][time]['total'][0] += 1
        # ages[age]['zones'][zone]['total'][0] += 1
        
        ages[age]['db'][0] += db
        ages[age]['time_infected'][time]['db'][0] += db
        # ages[age]['zones'][zone]['db'][0] += db
        
        ages[age]['ri'][0] += ri
        ages[age]['time_infected'][time]['ri'][0] += ri
        # ages[age]['zones'][zone]['ri'][0] += ri
        
        ages[age]['bp'][0] += bp
        ages[age]['time_infected'][time]['bp'][0] += bp
        # ages[age]['zones'][zone]['bp'][0] += bp

        if dead: 
            ages[age]['total'][1] += 1
            ages[age]['time_infected'][time]['total'][1] += 1
            # ages[age]['zones'][zone]['total'][1] += 1
            
            ages[age]['db'][1] += db
            ages[age]['time_infected'][time]['db'][1] += db
            # ages[age]['zones'][zone]['db'][1] += db

            ages[age]['ri'][1] += ri
            ages[age]['time_infected'][time]['ri'][1] += ri
            # ages[age]['zones'][zone]['ri'][1] += ri
        
            ages[age]['bp'][1] += bp
            ages[age]['time_infected'][time]['bp'][1] += bp
            # ages[age]['zones'][zone]['bp'][1] += bp

    
    return ages
    

    # with open('ages.py', 'w') as f:
    #     f.write('ages = ')
    #     f.write(str(ages))

def get_time_infected():
    pass

def get_zones():
    pass
