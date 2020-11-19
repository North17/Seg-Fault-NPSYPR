#Population

import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import pandas as pd 

pop = pd.read_csv('given_files\Population.csv')


ppl = []
for i in range(1,21):
    ppl.append(list(pop['Population'][pop['x location'] == i]))

array = np.array(ppl)
ax = sns.heatmap(array, linewidth = 0.5)

plt.title('Heatmap of Population')
#plt.show()

figure = ax.get_figure()
#figure.savefig('population.png')

#Cases 

cases = pd.read_csv('given_files\COVID_Dataset.csv')

cases = cases.sort_values(by = ['x location', 'y location'])
coords_cases = []
for i in range (1,21):
    semi = []
    for j in range (1,21):
        semi.append(len(cases[cases['x location'] == i][cases['y location'] == j]))
    coords_cases.append(semi)
coords_cases

cases_array = np.array(coords_cases)
ax = sns.heatmap(cases_array, linewidth = 0.5,cmap = "Oranges")

plt.title("Heatmap of Cases")
#plt.show()
plt.savefig("cases.png")

figure = ax.get_figure()
#figure.savefig('cases.png')

#Oranges_r
#PuOr_r


#Deaths

deaths = pd.read_csv('given_files\COVID_Dataset.csv')

deaths = deaths.sort_values(by = ['x location', 'y location'])
coords_deaths = []
for i in range (1,21):
    semi = []
    for j in range (1,21):
        semi.append(len(deaths[deaths['x location'] == i][deaths['y location'] == j][deaths['Outcome']== 'Dead']))
    coords_deaths.append(semi)
coords_cases

deaths_array = np.array(coords_deaths)
ax = sns.heatmap(deaths_array, linewidth = 0.5, cmap = 'Reds')
#plt.show()

figure = ax.get_figure()
#figure.savefig('deaths.png')

