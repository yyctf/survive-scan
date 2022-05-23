import threading
import time
exitFlag = 0
class prr (threading.Thread):
    def __init__(self,i, name):
        threading.Thread.__init__(self)
        #self.threadID = threadID
        self.i=i
        self.name = name
        #self.delay = delay

    def run(self):
        print("开始线程：" + self.name)
        threadLock.acquire()
        pr(self.i,self.name)
        print("退出线程：" + self.name)
        threadLock.release()


with open(sys.argv[1], 'r', encoding='utf-8') as f1:
    with open(sys.argv[2], 'w', encoding='utf-8') as f2:
        c = f1.readlines()
        for i in c:
            i = i.replace('\n', '')
a=[1,2,3,4,5,6,7,8,9]
b=0
def pr(i,name):
    global b
    try:
        for j in range(5):
            print(str(i)+' '+str(a[b]))
            b=b+1
    except:
        pass


threadLock = threading.Lock()
threads = []
t1=prr(1,'a')
t2=prr(2,'b')
t1.start()
t2.start()

threads.append(t1)
threads.append(t2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
a=[1,2,3,4]
print(len(a))
