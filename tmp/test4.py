from multiprocessing.pool import ThreadPool
import sys
import re
from urllib.parse import urlencode

import requests
c=[]
alive = []
die = []
http = 'http://'
https = 'https://'

def testurl(i):
    j = re.findall(r"^[a-zA-Z0-9:./]*", i)
    jj=''
    for k in j:
        i=k
    if i.find(http) < 0:
        if i.find(https) < 0:
            i = http+i
    #print(urlencode(i))
    try:
        requests.get(i,timeout=5)
    except:
        print('die ' + i)
        die.append(i)
    if requests.get(i,timeout=5).status_code == 200:
        print('alive '+i)
        alive.append(i)

with open(sys.argv[1], 'r', encoding='utf-8') as f1:
    with open(sys.argv[2], 'w+', encoding='utf-8') as f2:
        c = f1.readlines()
        print(len(c))
        #for i in c:
            #print(i.replace('\n', ''))
        with ThreadPool(processes=100) as pool:
            try:
                pool.map(testurl, c)
            except:
                pass
        f2.write('alive\n')
        for j in alive:
            f2.write(j+'\n')
        f2.write('\ndie\n')
        for j in die:
            f2.write(j+'\n')

