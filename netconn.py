from cbapi.response import *
from datetime import datetime, timedelta
yesterday = datetime.utcnow() - timedelta(days=2)      # Get "yesterday" in GMT

def netconns_script():
    
    c = CbEnterpriseResponseAPI()
    process_obj = c.select(Process).where('hostname:C02VG0TLHV2R AND process_name:"vmnet-natd"').min_last_update(yesterday)
    for i in process_obj:
        for netconn in i.netconns:
            print(netconn.timestamp,i.hostname,netconn.remote_ip,netconn.remote_port,netconn.domain)        
    return;

netconns_script()
