from lib.SocketAdapter import libSoAd
import os
import time

txDir = '/opt/mgw_BBAI/apps/TCP_PF/input/dataUp.csv'
rxDir = '/opt/mgw_BBAI/apps/TCP_PF/output/dataDown.csv'
cfgDir = '/opt/mgw_BBAI/apps/TCP_PF/input/config.txt' 
def RxCallback(data):
    print(data)
    with open(rxDir, 'a+') as fout:
        fout.writelines(str(data))

if __name__ == "__main__":
    rmAddr = 0
    rmPort = 0

    with open(cfgDir, 'r') as fin:
        data = fin.read().splitlines(True)
        rmAddr = data[0][:-1]
        rmPort = data[1]

    SoAd = libSoAd.SocketAdapter(local_host = '192.168.16.104',local_port = 23, rxcallback = RxCallback)
    SoAd.SockFd_Connect(remote_address = str(rmAddr),remote_port = int(rmPort))
    while True:
        if(os.stat(txDir).st_size!=0):
            with open(txDir, 'r') as fin:
                data = fin.read().splitlines(True)
                SoAd.SockFd_Send(data[0])
            with open(txDir, 'w') as fout:
                fout.writelines(data[1:]) 

        time.sleep(1)