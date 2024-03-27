
def parse_log(filename, delimiter):

    dicList=[]
    try: 
        with open(filename,"r") as logs:

            for logs in logs.readlines():

                logdic= {}
                data=str(logs).split(delimiter)
                if(len(data)>=6):
                    logdic["sourceIP"]=data[2]
                    logdic["destIP"]=data[4]
                    logdic["destPort"]=data[5]
                    logdic["Message"]=data[6]

                    dicList.append(logdic)
        return dicList
    except Exception as er:
        print(er)   


if __name__=="__main__":
    data=parse_log("sshlog.txt","\t")
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
            if (int(scans[x]["uDst"])>5 or int(scans[x]["uPort"])>5):
                scanners.append(scans[x]["sourceIP"])
    print("Below are list of offenders (potential scanners)") 
    for scanner in scanners:
       
        print(scanner)

