from multiprocessing.pool import ThreadPool
import sys
import os
import re
import requests
from urllib.parse import urlencode
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-r', type=str)
parser.add_argument('-p', type=str)
parser.add_argument('-t', type=int, default=100)
parser.add_argument('-v', action="store_true")
args = parser.parse_args()
os.system('chcp 65001')
t = args.t
r = args.r
p = args.p
if(args.v):
    print('批量目标快速探活v1.0\n参数说明\n-v 查看帮助信息\n-r 选择网址文件\n-p选择输出文件')
    exit(0)

c = []
alive = []
die = []
http = 'http://'
https = 'https://'


def testurl(i):
    j = re.findall(r"^[a-zA-Z0-9:./]*", i)
    jj = ''
    for k in j:
        i = k
    if i.find(http) < 0:
        if i.find(https) < 0:
            i = http+i
    #print(urlencode(i))
    try:
        requests.get(i, timeout=5)
    except:
        print('die ' + i)
        die.append(i)
    if requests.get(i, timeout=5).status_code == 200:
        print('alive '+i)
        alive.append(i)


def run():
    with open(r, 'r', encoding='utf-8') as f1:
        with open(p, 'w+', encoding='utf-8') as f2:
            c = f1.readlines()
            print('当前文件中存在'+str(len(c))+'个目标,当前线程数'+str(t))
            with ThreadPool(processes=t) as pool:
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


run()
