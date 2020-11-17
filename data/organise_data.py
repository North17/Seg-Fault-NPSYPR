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

        'two': [0, 0],
        'three': [0, 0],

        'time_infected': [],
        # 'zones': []
    }

    for i in range(239):
        empty['time_infected'].append({
            'total': [0, 0],

            'db': [0, 0],

            'ri': [0, 0],

            'bp': [0, 0],
                
            'two': [0, 0],
            'three': [0, 0],
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
        
        age = i['Age']
        db = int(i['Diabetes'])
        ri = int(i['Respiratory Illnesses'])
        bp = int(i['Abnormal Blood Pressure'])
        dead = i['Outcome'] == 'Dead'

        two = int((db and ri) or (ri and bp) or (db and bp))
        three = int(db and ri and bp)

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
        
        ages[age]['three'][0] += three
        ages[age]['time_infected'][time]['three'][0] += three
        # ages[age]['zones'][zone]['bp'][0] += bp

        
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
            
            ages[age]['two'][1] += two
            ages[age]['time_infected'][time]['two'][1] += two
            # ages[age]['zones'][zone]['bp'][1] += bp
            
            ages[age]['three'][1] += three
            ages[age]['time_infected'][time]['three'][1] += three
            # ages[age]['zones'][zone]['bp'][1] += bp

    
    return ages
    

    # with open('ages.py', 'w') as f:
    #     f.write('ages = ')
    #     f.write(str(ages))

def get_time_infected(x = False, y = False):

    cases = cases_csv

    if x and y:
        cases = cases[cases['x location'] == x]
        cases = cases[cases['y location'] == y]

    time_infected = []

    empty = {
        'total': [0, 0],

        'db': [0, 0],

        'ri': [0, 0],

        'bp': [0, 0],

        'two': [0, 0],
        'three': [0, 0],

        'ages': [],
    }

    for i in range(90):
        empty['ages'].append({
            'total': [0, 0],
            'db': [0, 0],
            'ri': [0, 0], 
            'bp': [0, 0],
            'two': [0, 0],
            'three': [0, 0],
        })

    for i in range(239):
        time_infected.append(copy.deepcopy(empty))

    for i in cases.iloc:

        age = i['Age']
        time = i['Time of Infection']
        db = int(i['Diabetes'])
        ri = int(i['Respiratory Illnesses'])
        bp = int(i['Abnormal Blood Pressure'])
        dead = i['Outcome'] == 'Dead'
        
        two = int((db and ri) or (ri and bp) or (db and bp))
        three = int(db and ri and bp)

        time_infected[time]['total'][0] += 1
        time_infected[time]['ages'][age]['total'][0] += 1

        time_infected[time]['db'][0] += db
        time_infected[time]['ages'][age]['db'][0] += db

        time_infected[time]['ri'][0] += ri
        time_infected[time]['ages'][age]['ri'][0] += ri

        time_infected[time]['bp'][0] += bp
        time_infected[time]['ages'][age]['bp'][0] += bp
        
        time_infected[time]['two'][0] += two
        time_infected[time]['ages'][age]['two'][0] += two
        
        time_infected[time]['three'][0] += bp
        time_infected[time]['ages'][age]['three'][0] += three


        if dead:
            time_infected[time]['total'][1] += 1
            time_infected[time]['ages'][age]['total'][1] += 1

            time_infected[time]['db'][1] += db
            time_infected[time]['ages'][age]['db'][1] += db

            time_infected[time]['ri'][1] += ri
            time_infected[time]['ages'][age]['ri'][1] += ri

            time_infected[time]['bp'][1] += bp
            time_infected[time]['ages'][age]['bp'][1] += bp

            time_infected[time]['two'][1] += two
            time_infected[time]['ages'][age]['two'][1] += two

            time_infected[time]['three'][1] += three
            time_infected[time]['ages'][age]['three'][1] += three

    
    return time_infected

        






def get_population_density ():

    cases = cases_csv

    density = []
    population_density = []

    empty = {
        'population': None,

        'total': [0, 0],
        'db': [0, 0],
        'ri': [0, 0],
        'bp': [0, 0],

        'two': [0, 0],
        'three': [0, 0],

        'time_infected': [],
        'ages': [],
    }

    for i in range(90):
        empty['ages'].append({
            'total': [0, 0],
            'db': [0, 0],
            'ri': [0, 0], 
            'bp': [0, 0],
            'two': [0, 0],
            'three': [0, 0],
        })

    for i in range(239):
        empty['time_infected'].append({
            'total': [0, 0],

            'db': [0, 0],

            'ri': [0, 0],

            'bp': [0, 0],
            
            'two': [0, 0],
            'three': [0, 0],
        })

    for i in cases.iloc:
        x = i['x location']
        y = i['y location']
        pd = pop_csv.iloc[20*(x-1) + y-1]['Population']

        try:
            ind = density.index(pd)
        except:
            ind = len(density)
            density.append(pd)
            population_density.append(copy.deepcopy(empty))
            population_density[ind]['population'] = pd

        age = i['Age']
        time = i['Time of Infection']
        db = int(i['Diabetes'])
        ri = int(i['Respiratory Illnesses'])
        bp = int(i['Abnormal Blood Pressure'])
        dead = i['Outcome'] == 'Dead'
        
        two = int((db and ri) or (ri and bp) or (db and bp))
        three = int(db and ri and bp)

        population_density[ind]['total'][0] += 1
        population_density[ind]['time_infected'][time]['total'][0] += 1
        population_density[ind]['ages'][age]['total'][0] += 1
        
        population_density[ind]['db'][0] += db
        population_density[ind]['time_infected'][time]['db'][0] += db
        population_density[ind]['ages'][age]['db'][0] += db
        
        population_density[ind]['ri'][0] += ri
        population_density[ind]['time_infected'][time]['ri'][0] += ri
        population_density[ind]['ages'][age]['ri'][0] += ri

        population_density[ind]['bp'][0] += bp
        population_density[ind]['time_infected'][time]['bp'][0] += bp
        population_density[ind]['ages'][age]['bp'][0] += bp

        population_density[ind]['two'][0] += two
        population_density[ind]['time_infected'][time]['two'][0] += two
        population_density[ind]['ages'][age]['two'][0] += two

        population_density[ind]['three'][0] += three
        population_density[ind]['time_infected'][time]['three'][0] += three
        population_density[ind]['ages'][age]['three'][0] += three

        if dead:
            population_density[ind]['total'][1] += 1
            population_density[ind]['time_infected'][time]['total'][1] += 1
            population_density[ind]['ages'][age]['total'][1] += 1
            
            population_density[ind]['db'][1] += db
            population_density[ind]['time_infected'][time]['db'][1] += db
            population_density[ind]['ages'][age]['db'][1] += db
            
            population_density[ind]['ri'][1] += ri
            population_density[ind]['time_infected'][time]['ri'][1] += ri
            population_density[ind]['ages'][age]['ri'][1] += ri

            population_density[ind]['bp'][1] += bp
            population_density[ind]['time_infected'][time]['bp'][1] += bp
            population_density[ind]['ages'][age]['bp'][1] += bp

            population_density[ind]['two'][1] += two
            population_density[ind]['time_infected'][time]['two'][1] += two
            population_density[ind]['ages'][age]['two'][1] += two

            population_density[ind]['three'][1] += three
            population_density[ind]['time_infected'][time]['three'][1] += three
            population_density[ind]['ages'][age]['three'][1] += three

    sorting_func = lambda x: x['population']
    population_density.sort(key=sorting_func)

    return population_density