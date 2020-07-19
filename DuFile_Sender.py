import socket
import time
import datetime
import os

class DuFile_Sender():
    def __init__(self):

        self.__server_client__()
        

    def __server_client__(self):
        x = int(input('1-Server or 2-Client: '))

        if x==1:
            self.__server__()
        if x==2:
            self.__client__()

    def __server__(self):
        
        d = r'' + str(input('Filename: '))

        if d == '':
            quit()
        
        content = None

        PORT = 12345

        data_counter = []
        timer = []

        lst = []

        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ss.connect(("8.8.8.8", 80))

        local_ip = (ss.getsockname()[0])
        print(local_ip)

        s.bind((local_ip, PORT))#LOCAL IP ADDRESS
        ss.close()
        s.listen(10)
        c, addr = s.accept()
        print('{} connected.'.format(addr))

        f = open(r''+d, 'rb')

        datas = f.read(1024)
        while datas:

            timer.append(time.time())
            
            data_counter.append(1024)
            
            if(timer[-1] - timer[0] >= 1.0):
                
                content = (str(round(sum(data_counter) / pow(1024,2),2)) + ' MB/s')

                print(content)

                data_counter.clear()
                timer.clear()
            
            c.send(datas)
            datas = f.read(1024)

        f.close()
        print('Done sending...')


    def __client__(self):
        x = input('LOCAL IP: ')
        d = r'' + input('Filename: ')

        PORT = 12345
        data_counter = []
        timer = []
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('' + str(x), PORT))

        f = open(r''+d, 'wb')

        while True:
            datas = s.recv(1024)

            while datas:
                f.write(datas)
                datas = s.recv(1024)

                data_counter.append(1024)
                timer.append(time.time())
                
                if(timer[-1] - timer[0] >= 1.0):
                    content = (str(round(sum(data_counter) / pow(1024,2),2)) + ' MB/s')
                    
                    print(content)

                    data_counter.clear()
                    timer.clear()
                
            f.close()
            break
        
        print("Done receiving")


DuFile_Sender()
