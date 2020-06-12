import os
import socket
import selectors
import threading
import time



class SocketAdapter:

    def __init__(self, local_host, local_port, rxcallback = None):
        self.localAddress = local_host
        self.localPort = local_port
        self.sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sel = selectors.DefaultSelector()
        self.rxTask = threading.Thread(target = self.SoAd_Rx_Task, args=(rxcallback, ))
        
        pass

    def SockFd_Create(self):
        return self.sockfd

    def SockFd_Connect(self, remote_address, remote_port):
        self.remote_addr = (remote_address, remote_port)
        print("Starting connection to", self.remote_addr)
        while self.sockfd.connect_ex(self.remote_addr):
            time.sleep(1)
            pass
        print("Connected to ", self.remote_addr)
        events = selectors.EVENT_READ
        self.sel.register(self.sockfd, events, data=None)
        self.sockfd.setblocking(False)
        
        self.rxTask.start()

    def SockFd_Close(self):
        self.sockfd.close()

    def Get_Sel(self):
        return self.sel

    def SoAd_Rx_Task(self, _callback = None):
        while True:
            events = self.sel.select(timeout=None)
            for key, mask in events:
                if mask & selectors.EVENT_READ: 
                    try:
                        data = self.sockfd.recv(4096)
                    except:
                        pass
                    else:
                        if data:
                            if _callback != None:
                                _callback(data)
                            # print(data)
                            # with open(rxDir, 'a+') as fout:
                            #     fout.writelines(str(data))
                        else:
                            pass

    def SockFd_Send(self, data):
        try:
            self.sockfd.sendall(bytes(data,'utf-8'))
        except:
            print("Disconnected from ",self.remote_addr)
            self.sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            while self.sockfd.connect_ex(self.remote_addr):
                print("Reconnecting...")
                time.sleep(1)
            print("Reconnected to ",self.remote_addr)
            self.sockfd.setblocking(False)
            
# if __name__ == "__main__":
#     SoAd = SocketAdapter(local_host = '192.168.16.104',local_port = 23)
#     SoAd.SockFd_Connect(remote_address = '192.168.16.104',remote_port = 23)
#     while True:
#         if(os.stat(txDir).st_size!=0):
#             with open(txDir, 'r') as fin:
#                 data = fin.read().splitlines(True)
#                 SoAd.SockFd_Send(data[0])
#             with open(txDir, 'w') as fout:
#                 fout.writelines(data[1:]) 

#         time.sleep(0)
