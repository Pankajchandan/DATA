
# coding: utf-8

# In[1]:


import os
import sys


# In[28]:


empty_label=0
bad_label=0
good_label=0
file_out=open('nvidia-labels.txt', 'w')
directory="/datasets/aic1080/train/labels"
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        s=open(os.path.join(directory, filename)).read()
        if not s:
            empty_label=empty_label+1
        else:
            if any(c.isalpha() for c in s) is False:
                bad_label=bad_label+1
            else:
                file_out.write("https://github.com/shadySource/DATA/raw/master/datasets/aic1080/train/images/"+filename+"\n"+s+"\n"+"\n")
                good_label=good_label+1
file_out.close()
print("Done")
print("empty labels: ",empty_label )
print("bad labels: ",bad_label )
print("good labels: ",good_label)

