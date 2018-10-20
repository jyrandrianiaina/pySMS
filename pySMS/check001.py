import pyping
import gammu.smsd
import sys
def checkpabxalmerys():
    my_server = ["8.8.8.8"]
    s1 = []
    for myip in my_server:
        response = pyping.ping(myip,count=20,timeout=10000)
        if response.ret_code == 0:
            sms = "20 pings to "+myip +" : min:"+response.min_rtt+"ms /max: "+response.max_rtt+"ms /moyenne:" +response.avg_rtt+ "ms"
        else:
            response.max_rtt = " "
            response.avg_rtt = "OFFLINE"
            sms = myip +" : " +response.avg_rtt
        s1.append(sms)
    return s1

def sending_sms(requester):
    message = {
        'Text': checkpabxalmerys() ,
        'SMSC': {'Location': 1},
        'Number': requester
    }
    smsd.InjectSMS([message])    
sending_sms(sys.argv[1])

