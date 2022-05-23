import threading
import requests
import sys

length = len(url)
quantity=0
alive = []
die = []
threadLock = threading.Lock()
threads = []
exitFlag = 0


class pr(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # self.i = i

    def run(self):
        threadLock.acquire()
        funn()
        threadLock.release()


def fun(i):
    try:
        state = requests.get(i, timeout=5)
    except:
        print('die ' + i)
        alive.append(i)
    if state.status_code == 200:
        print('alive ' + i)
        alive.append(i)

a = 0
http = 'http://'
https = 'https://'
def funn():
    global a
    while a<quantity:
        if c[a].find(http) < 0:
            if c[a].find(https) < 0:
                c[a] = http + c[a]
        try:
            fun(c[a])
            print(c[a])
        except:
            print('die ' + c[a])
        a = a + 1


def run():
    t1 = pr()
    t2 = pr()
    t1.start()
    t2.start()
    threads.append(t1)
    threads.append(t2)
    for t in threads:
        t.join(timeout=10)


with open(sys.argv[1], 'r', encoding='utf-8') as f1:
    with open(sys.argv[2], 'w', encoding='utf-8') as f2:
        c = f1.readlines()
        for i in c:
            i = i.replace('\n', '')
            #global quantity
            quantity=len(c)
            run()
            f2.write('alive\n')
            for j in alive:
                f2.write(j+'\n')
            f2.write('\ndie\n')
            for j in die:
                f2.write(j+'\n')

