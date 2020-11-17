from organise_data import get_ages, get_time_infected

ages = get_ages()
time_infected = get_time_infected()

# with open('data/ages.py', 'w') as f:
#     f.write('ages = ')
#     f.write(str(ages))

with open('data/time_infected.py', 'w') as f:
    f.write('time_infected = ')
    f.write(str(time_infected))
