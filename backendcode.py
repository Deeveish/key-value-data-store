#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import sys
import time
import threading
filekey={}
lock = threading.Lock()

def create(filename,content,timeofexpiry):
    try:
        with lock:
            json_content=json.dumps(content)
            if filename in filekey:
                print("File already exists.Please give another name")
            elif len(filename)>32:
                print("Length should be within 32 Characters")
            elif sys.getsizeof(json_content)> 16*1000 :
                print("Content should be less than 16KB")
            elif sys.getsizeof(json.dumps(filekey))> (10**9):
                print("Memory limit exceeded")
            else:
                if timeofexpiry == 0:
                    l=[json_content,timeofexpiry]
                else:
                    l=[json_content, time.time() + timeofexpiry]
                filekey[filename]=l
    except Exception as e:
            print(e)
def read(filename):
    try:
        with lock:
            if filename not in filekey:
                print("File doesnot exists")
                return
            file_details=filekey[filename]
            if file_details[1]!=0:
                if time.time()<file_details[1]:
                    print(str(filename) + ':' + str(file_details[0]))
                else :
                    print("File was expired")
                    return
            else:
                file_details=filekey[filename]
                print(str(filename) + ':' + str(file_details[0]))
    except Exception as e:
        print(e)

            
def delete(filename):
    try:
        with lock:
            if filename not in filekey:
                print("File doesnot exists")
                return
            file_details=filekey[filename]
            if file_details[1]!=0: 
                if time.time()<file_details[1]:
                    del filekey[filename]
                    print("File  sucessfully deleted")
                else :
                    print("File was expired")
            else:
                del filekey[filename]
                print("File  sucessfully deleted")            
    except Exception as e:
        print(e)    


# In[ ]:





# In[ ]:





# In[37]:





# In[39]:





# In[ ]:




