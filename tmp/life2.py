import requests
import sys
import threading
alive = []
die = []
c = []
threadLock = threading.Lock()
threads = []
http = 'http://'
https = 'https://'
quantity=0

exitFlag = 0

class many (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #self.i = i

    def run(self):
        threadLock.acquire()
        test2()
        threadLock.release()

def testurl(i):
    if i.find(http) < 0:
        if i.find(https) < 0:
            i = http+i
    print(i)
    state = requests.get(i,timeout=5)
    if state.status_code == 200:
        print('alive '+i)
        alive.append(i)

aa=0
def test2():
    global c
    global aa
    for i in range(0,quantity):
        try:
            testurl(c[aa])
        except:
            print('die '+c[aa])
            die.append(i)
            pass
        aa=aa+1

def run():
    global threads
    t1 = many()
    t2 = many()
    t1.start()
    t2.start()
    threads.append(t1)
    threads.append(t2)
    for t in threads:
        t.join(timeout=5)

with open(sys.argv[1], 'r', encoding='utf-8') as f1:
    with open(sys.argv[2], 'w', encoding='utf-8') as f2:
        c = f1.readlines()
        for i in c:
            i = i.replace('\n', '')
            quantity=len(c)
            run()
            f2.write('alive\n')
            for j in alive:
                f2.write(j+'\n')
            f2.write('\ndie\n')
            for j in die:
                f2.write(j+'\n')

