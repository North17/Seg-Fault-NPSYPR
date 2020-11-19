#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np 
import matplotlib.pyplot as plt 
  
  

aggrp = ['1', '2', '3', '4', '5', '6', '7'] 
  
data = [65992, 66158, 66205, 65962, 66265, 66312, 65988] 
  

explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1) 
  

colors = ( "palevioletred", "lightpink", "mediumvioletred", 
          "darkred", "orchid", "crimson", "hotpink") 
  
 
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
          title ="Number Of Days", 
          loc ="center left", 
          bbox_to_anchor =(1, 0, 0.5, 1)) 
  
plt.setp(autotexts, size = 8, weight ="bold") 
ax.set_title("Time taken (in days) ") 
  
plt.show() 


# In[ ]:




