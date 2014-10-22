from ftplib import FTP
import queue as q
import threading as t

sites =['ftp.ceag.ch','ftp.astro.ch','ftp.fourmilab.ch','ftp.fastnet.ch','ftp.imp.ch','ftp.ifor.math.ethz.ch','ftp.inf.ethz.ch','ftp.math.ethz.ch','root.cern.ch','ftp.cc.ac.cn','ftp.aopen.com.cn','ftp.pku.edu.cn']

def worker(s,n):
    print('Thread {} Connecting with {}'.format(n,addr))
    ftp=FTP(addr)
    ftp.login()
    print(80*'*')
    print(addr)
    ftp.retrlines('LIST')
    print('\n')

i=0
for addr in sites:
     i+=1
     th = t.Thread(target=worker(addr,i))
     th.daemon = True
     th.start()
     
