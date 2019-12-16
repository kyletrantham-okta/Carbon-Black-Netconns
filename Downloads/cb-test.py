from cbapi.response import *


def hosts():
    cb = CbEnterpriseResponseAPI()
    query = cb.select(Process).where("ipaddr:10.62.73.89 AND -hostname:c02vf18ug8wl AND ipport:445 AND ipport:139").sort("last_update desc")                 
    for i in query:                              # uses the iterator to retrieve all results
        print("{0} {1}".format(i.hostname,i.interface_ip,))
    processes = query[:60]                          # retrieve the first ten results
    len(query) 
    return;

def netconns():
    
    c = CbEnterpriseResponseAPI()

    limit = 1
    while limit < 2:
        process_obj = c.select(Process).where('ipaddr:10.62.73.89 AND -hostname:c02vf18ug8wl AND ipport:445 AND ipport:139')[limit]

        for i in process_obj.netconns:
            print("{0} {1}".format(i.remote_ip,i.local_port,))
            # print(i.remote_ip+":"+str(i.local_port))

        limit += 1
    return;

netconns()
    
#query = cb.select(Process)  

#cb = CbResponseAPI(profile="default")
#query = cb.select(Process) 

#query = "cmdline:*Responder* last_update:['2019-12-01T00:00:00 TO *']"

#X = c.select(Process).where(query)[0]

#for proc in query:                              # uses the iterator to retrieve all results
#     print("{0} {1}".format(proc.username, proc.hostname))




#print(X)
