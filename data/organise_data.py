import pandas as pd
import copy

cases = pd.read_csv('../given_files/COVID_Dataset.csv')
pop = pd.read_csv('../given_files/Population.csv')

def write_ages():

    ages = []

    empty = {
        'cases': 0,
        'deaths': 0,

        'db': {
            'cases': 0,
            'deaths': 0,
        },

        'ri': {
            'cases': 0,
            'deaths': 0,
        },

        'bp': {
            'cases': 0,
            'deaths': 0,
        },

        'time_infected': [],
        'zones': []
    }

    for i in range(239):
        empty['time_infected'].append({
            'cases': 0,
            'deaths': 0,

            'db': {
                'cases': 0,
                'deaths': 0,
            },

            'ri': {
                'cases': 0,
                'deaths': 0,
            },

            'bp': {
                'cases': 0,
                'deaths': 0,
            },
        })

    for i in range(400):
        empty['zones'].append({
            'cases': 0,
            'deaths': 0,

            'db': {
                'cases': 0,
                'deaths': 0,
            },

            'ri': {
                'cases': 0,
                'deaths': 0,
            },

            'bp': {
                'cases': 0,
                'deaths': 0,
            },
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

        ages[age]['cases'] += 1
        ages[age]['time_infected'][time]['cases'] += 1
        ages[age]['zones'][zone]['cases'] += 1
        
        ages[age]['db']['cases'] += db
        ages[age]['time_infected'][time]['db']['cases'] += db
        ages[age]['zones'][zone]['db']['cases'] += db
        
        ages[age]['ri']['cases'] += ri
        ages[age]['time_infected'][time]['ri']['cases'] += ri
        ages[age]['zones'][zone]['ri']['cases'] += ri
        
        ages[age]['bp']['cases'] += bp
        ages[age]['time_infected'][time]['bp']['cases'] += bp
        ages[age]['zones'][zone]['bp']['cases'] += bp

        if dead: 
            ages[age]['deaths'] += 1
            ages[age]['time_infected'][time]['deaths'] += 1
            ages[age]['zones'][zone]['deaths'] += 1
            
            ages[age]['db']['deaths'] += db
            ages[age]['time_infected'][time]['db']['deaths'] += db
            ages[age]['zones'][zone]['db']['deaths'] += db

            ages[age]['ri']['deaths'] += ri
            ages[age]['time_infected'][time]['ri']['deaths'] += ri
            ages[age]['zones'][zone]['ri']['deaths'] += ri
        
            ages[age]['bp']['deaths'] += bp
            ages[age]['time_infected'][time]['bp']['deaths'] += bp
            ages[age]['zones'][zone]['bp']['deaths'] += bp


    with open('ages.py', 'w') as f:
        f.write('ages = ')
        f.write(str(ages))

def write_time_affected():
    pass

def write_zones():
    pass
    

write_ages()