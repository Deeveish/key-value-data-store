import threading
try:
    def CRD():
        details=["Name", "Age" ,"Languages known","Preferred Role" , "Years Of Experience"]
        print(" To Create Event Enter : 1 \n To Read Event Enter 2\n To Delete Event enter : 3")
        n=int(input()) #getting desired input from user 
        if(n==1):
            content={}
            filename=input("Enter file name")
            if len(filename)<=32:
                content={i:input("enter {}".format(i)) for i in details} #storing content in dictionary
                print(content)
            else:
                print("Error : Enter Valid Key name")
            print("Enter Time of Expiry for the file (in seconds)")
            timeofexpiry=int(input())
            create(filename,content,timeofexpiry)
        if(n==2):
            filename=input("Enter File Name")
            read(filename)
        if(n==4):
            filename=input("Enetr File name")
            delete(filename)
    
try:
    t1 = threading.Thread(target=CRD(), args=(5,))  #creating  multithread  
    t2=threading.Thread(target=CRD(), args=(5,))

    t1.start()  #starting each thread
    t2.start()

    t1.join()  # wait until thread 1 is completely executed
    t2.join()  # wait until thread 2 is completely executed
except Exemption as e:
    print(e)




