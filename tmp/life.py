import requests
import sys
import threading
alive=[]
die=[]
c = []
http='http://'
https = 'https://'
def testurl(i):
    if i.find(http) < 0:
        if i.find(https) < 0:
            i = http+i
        state=0
        try:
            state = requests.get(i, timeout=5).status_code
        except:
            print('die '+i)
            die.append(i)
            pass
        if state == 200:
            print('alive '+i)
            alive.append(i+' '+str(state))
def many():

with open(sys.argv[1], 'r', encoding='utf-8') as f1:
    with open(sys.argv[2], 'w+', encoding='utf-8') as f2:
        c = f1.readlines()
        for i in c:
            i = i.replace('\n', '')  # 去掉一个\n不然会回车两次
            fun = threading.Thread(target=testurl, args=(i,))
            fun.start()
        f2.write('alive\n')
        for j in alive:
            f2.write(j+'\n')
        f2.write('\ndie\n')
        for j in die:
            f2.write(j+'\n')