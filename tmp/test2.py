from multiprocessing import Process, Manager
a=[1,2,3,4,5,6,7,8,9]
def pr(i):
    print(i)
def func(dt, lt):
    for i in range(5):
        key = 'arg' + str(i)
        dt[key] = i * i
        lt += range(11, 16)
if __name__ == "__main__":
    p3 = Process(target=pr, args=(a))
    p4 = Process(target=pr, args=(a))
    p3.start()
    p4.start()
    p3.join(timeout=3)
    p4.join(timeout=3)
    manager = Manager()
    dt = manager.dict()
    lt = manager.list()
    p1 = Process(target=func, args=(dt, lt))
    p2 = Process(target=func, args=(dt, lt))
    p1.start()
    p2.start()
    p1.join(timeout=3)
    p2.join(timeout=3)
    print(dt)
    print(lt)