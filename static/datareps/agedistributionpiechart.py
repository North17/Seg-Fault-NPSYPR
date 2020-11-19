#!/usr/bin/env python
# coding: utf-8

# In[23]:



import numpy as np 
import matplotlib.pyplot as plt 
  
  

aggrp = ['0-15', '16-30', '31-45', '46-60', '61-75', '76-89'] 
  
data = [45503, 96874, 125120, 107643, 63096, 24647] 
  

explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1) 
  

colors = ( "palevioletred", "lightpink", "mediumvioletred", 
          "darkred", "orchid", "crimson") 
  
 
wp = { 'linewidth' : 1, 'edgecolor' : "gainsboro" } 
  

def func(pct, allvalues): 
    absolute = int(pct / 100.*np.sum(allvalues)) 
    return "{:.1f}%\n({:d})".format(pct, absolute) 
  

fig, ax = plt.subplots(figsize =(10, 7)) 
wedges, texts, autotexts = ax.pie(data,  
                                  autopct = lambda pct: func(pct, data), 
                                  explode = explode,  
                    
                                  shadow = True, 
                                  colors = colors, 
                                  startangle = 90, 
                                  wedgeprops = wp, 
                                  textprops = dict(color ="ivory")) 
  

ax.legend(wedges, aggrp, 
          title ="Age Groups", 
          loc ="center left", 
          bbox_to_anchor =(1, 0, 0.5, 1)) 
  
plt.setp(autotexts, size = 8, weight ="bold") 
ax.set_title("Distribution of Cases by Age") 
  
plt.show() 


# In[ ]:




