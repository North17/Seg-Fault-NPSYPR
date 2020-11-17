from organise_data import get_ages

ages = get_ages()

with open('data/ages.py', 'w') as f:
    f.write('ages = ')
    f.write(str(ages))
