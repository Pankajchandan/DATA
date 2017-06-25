
# coding: utf-8

# In[88]:

import sys
import re

with open('ann.txt', 'r') as my_file:
    content=my_file.read()
    #print(content)
    objNum = re.findall('\"([0-9]*)\":{\"shape_attributes\"', content)
    objNum = [ int(x) for x in objNum ]
    #print(objNum)
    fileName = re.findall('\"filename\":\"(.*)\",\"base64_img_data\":', content)
    #print(fileName)
    objName = re.findall('\"region_attributes\":{\"name":\"([a-z]*[A-z]*_*)\"}', content)
    #print(objName)
    dimension = re.findall('{\"name\":\"[a-zA-z]*\",\"x\":([0-9]*),\"y\":([0-9]*),\"width\":([0-9]*),\"height\":([0-9]*)}', content)
    #dimension = [ int(x) for x in dimension ]
    #print(dimension)
    file=open('res.txt', 'w')
    
    objNumber=[]
    for x in range(0, len(objNum)-1): 
        if(objNum[x]>=objNum[x+1]):
            objNumber.append(objNum[x])
    objNumber.append(objNum[x+1])
    
    objIndex=0
    
    for i in range(0, len(objNumber)):
        file.write(fileName[i])
        file.write("\n")
        
        for i in range(0,objNumber[i]+1):
            file.write(objName[objIndex])
            file.write(" ")
            
            for j in range(0,4):
                if(j==2):
                    file.write(str(int(dimension[objIndex][j])+int(dimension[objIndex][0])))
                elif(j==3):
                    file.write(str(int(dimension[objIndex][j])+int(dimension[objIndex][1])))
                else:
                    file.write(dimension[objIndex][j])
                if(j<3):
                    file.write(" ")
            
            objIndex=objIndex+1
            file.write("\n")
        file.write("\n")
            
    file.close()
        
    print("conversion completed....data stored in res.txt")


# In[ ]:



