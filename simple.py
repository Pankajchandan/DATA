
# coding: utf-8

# In[1]:


import os
import sys


# In[28]:


file_out=open('nvidia-labels.txt', 'w')
directory="/datasets/aic1080/train/labels"
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        s=open(os.path.join(directory, filename)).read()
        file_out.write("https://github.com/shadySource/DATA/raw/master/datasets/aic1080/train/images/"+filename+"\n"+s+"\n"+"\n")
file_out.close()
print("Done")

