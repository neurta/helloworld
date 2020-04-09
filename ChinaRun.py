from Web import Web

cnrun=Web('http://www.chinarun.com/html/event_k_%20%E8%87%AA%E8%A1%8C%E8%BD%A6%E8%B5%9B_0_.html#cnt',
                     'ulHdList',
                     'n',
                     'divCnt divHA'
                     )

cnrun.getlist()

def p(L):
    return 'http://www.chinarun.com'+L

cnrun.map(p)

def getGen():
    return cnrun.process()

if __name__=="__main__":
    #this is for test only
    for i in getGen():
        print(i[0])


