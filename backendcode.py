import json
import sys
import time
import threading
filekey={}
lock = threading.Lock()    #Thread safety (By locking)
#To create file
def create(filename,content,timeofexpiry):
    try:
        with lock:
            json_content=json.dumps(content)    #Converting File content into Json format
            if filename in filekey:
                print("File already exists.Please give another name")
            elif sys.getsizeof(json_content)> 16*1000 :  #checking the File Content Size
                print("Content should be less than 16KB")
            elif sys.getsizeof(json.dumps(filekey))> (10**9):
                print("Memory limit exceeded")
            else:
                if timeofexpiry == 0:
                    l=[json_content,timeofexpiry]     #creating the file content and timeofexpiry as a list
                else:
                    l=[json_content, time.time() + timeofexpiry]     #creating the file content and timeofexpiry as a list
                filekey[filename]=l                #proving the list as value to the file key
    except Exception as e:
            print(e)
#To read file
def read(filename):
    try:
        with lock:
            if filename not in filekey:
                print("File doesnot exists")
                return
            file_details=filekey[filename]
            if file_details[1]!=0:
                if time.time()<file_details[1]:            #Comparing the current time with expiry time
                    print(str(filename) + ':' + str(file_details[0]))  #printing the file content
                else :
                    print("File was expired")
                    return
            else:
                file_details=filekey[filename]             #Comparing the current time with expiry time
                print(str(filename) + ':' + str(file_details[0]))      #printing the file content
    except Exception as e:
        print(e)

# To delete file        
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
