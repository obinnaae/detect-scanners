# This function takes a log file and parse it and return a dictionary containing sourceIP, Destination IP and Destination Port.
# Limitations: This function can only parse the logfile attached to this project. You can modify to suite your need.
def parse_log(filename):

    dicList=[]
    try: 
        with open(filename,"r") as logs:

            fields=["time_stamp","Id","sourceIP","sourcePort","destIP","destPort","message"]
            for log in logs.readlines():
            
                logdict=dict(zip(fields,log.split()))
               
                dicList.append(logdict)
        return dicList
    except Exception as er:
        print(er)   

def find_offenders(log_file):
    
    data=parse_log(log_file)
    sourceIP=[]
    scanners=[]
    scans=[]
    for i in range(len(data)):

        if(sourceIP.count(data[i]["sourceIP"])==0):
            sourceIP.append(data[i]["sourceIP"])
    for ip in sourceIP:
        destIP=[]
        destPort=[]
        for j in range(len(data)):
            if(data[j]["sourceIP"]==ip and destIP.count(data[j]["destIP"])==0):

                destIP.append(data[j]["destIP"])

            if(data[j]["sourceIP"]==ip and destPort.count(data[j]["destPort"])==0):
                destPort.append(data[j]["destPort"])
        scans.append({"sourceIP":ip,"uDst":len(destIP), "uPort":len(destPort)})   
    for x in range(len(scans)):
            if (int(scans[x]["uDst"])>20 or int(scans[x]["uPort"])>20): # a sourceIP targeting more than 10 unique destinationsIP or 10 unique ports 
                scanners.append(scans[x]["sourceIP"])
    
    return scanners
    
    

if __name__=="__main__":
    
        offenders=find_offenders("sshlog.txt")
        
        if(len(offenders)>0):
            print("Below are list of offenders (potential scanners)") 
            for offender in offenders:
       
                print(offender)
        else:
            print("No offenders found, please make sure logs are in the format compatible with this code")
       
    
