import pandas as pd
import copy

cases = pd.read_csv('../given_files/COVID_Dataset.csv')
pop = pd.read_csv('../given_files/Population.csv')

def write_ages():

    ages = []

    empty = {
        'total': [0, 0],

        'db': [0, 0],

        'ri': [0, 0],

        'bp': [0, 0],

        'time_infected': [],
        'zones': []
    }

    for i in range(239):
        empty['time_infected'].append({
            'total': [0, 0],

            'db': [0, 0],

            'ri': [0, 0],

            'bp': [0, 0],
        })

    for i in range(400):
        empty['zones'].append({
            'total': [0, 0],

            'db': [0, 0],

            'ri': [0, 0],

            'bp': [0, 0],
        })

    for i in range(90):
        ages.append(copy.deepcopy(empty))

    for i in cases.iloc:
        age = i['Age']
        db = int(i['Diabetes'])
        ri = int(i['Respiratory Illnesses'])
        bp = int(i['Abnormal Blood Pressure'])
        dead = i['Outcome'] == 'Dead'

        x = i['x location']
        y = i['y location']
        zone = 20*y + x - 21

        time = i['Time of Infection']

        ages[age]['total'][0] += 1
        ages[age]['time_infected'][time]['total'][0] += 1
        ages[age]['zones'][zone]['total'][0] += 1
        
        ages[age]['db'][0] += db
        ages[age]['time_infected'][time]['db'][0] += db
        ages[age]['zones'][zone]['db'][0] += db
        
        ages[age]['ri'][0] += ri
        ages[age]['time_infected'][time]['ri'][0] += ri
        ages[age]['zones'][zone]['ri'][0] += ri
        
        ages[age]['bp'][0] += bp
        ages[age]['time_infected'][time]['bp'][0] += bp
        ages[age]['zones'][zone]['bp'][0] += bp

        if dead: 
            ages[age]['total'][1] += 1
            ages[age]['time_infected'][time]['total'][1] += 1
            ages[age]['zones'][zone]['total'][1] += 1
            
            ages[age]['db'][1] += db
            ages[age]['time_infected'][time]['db'][1] += db
            ages[age]['zones'][zone]['db'][1] += db

            ages[age]['ri'][1] += ri
            ages[age]['time_infected'][time]['ri'][1] += ri
            ages[age]['zones'][zone]['ri'][1] += ri
        
            ages[age]['bp'][1] += bp
            ages[age]['time_infected'][time]['bp'][1] += bp
            ages[age]['zones'][zone]['bp'][1] += bp


    with open('ages.py', 'w') as f:
        f.write('ages = ')
        f.write(str(ages))

def write_time_affected():
    pass

def write_zones():
    pass
    

write_ages()