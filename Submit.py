from urllib import request
from urllib import parse
from http import cookiejar
import re

loginurl = 'https://www.bike.so/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
data = {
    'fastloginfield': 'username',
    'username': 'hardtosay',
    'password': 'asd123!@#',
    'quickforward': 'yes',
    'handlekey': 'ls'
}
data = parse.urlencode(data).encode('utf-8')
cookie = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
response = opener.open(loginurl, data=data)

#print(response.read().decode('utf-8'))

def process(str):
    str = str.split('\n')
    data = dict()
    for i in str:
        i = i.split(':')
        s1 = i[0]
        if len(i) is 2:
            s2 = i[1]
        else:
            s2 = ''
        data[s1] = s2
    return data


def post(subject,message,n):
    threadurl = 'https://www.bike.so/forum.php?mod=post&action=newthread&fid=95'
    response = opener.open(threadurl)
    result = response.read().decode('utf-8')
    result0 = re.findall('id="formhash" value="(.+?)"', result)[0]
    result1 = re.findall('id="posttime" value="(.+?)"', result)[0]

    posturl = 'https://www.bike.so/forum.php?mod=post&action=newthread&fid=95&extra=&topicsubmit=yes'

    data = """
    wysiwyg: 1
    sortid: 4
    subject: this is a test,ignore it
    selectsortid: 4
    message: this is a test
    replycredit_extcredits: 0
    replycredit_times: 1
    replycredit_membertimes: 1
    replycredit_random: 100
    readperm:
    price:
    tags:
    allownoticeauthor: 1
    usesig: 1
    save:
    """

    data=process(data)
    data['formhash']=result0
    data['posttime']=result1
    data['subject']=subject
    data['message']=message
    data = parse.urlencode(data).encode('utf-8')
    response=opener.open(posturl,data=data)
    #print('start\n')
    #print(response.read().decode('utf-8'))
    puburl='https://www.bike.so/forum.php?mod=misc&action=pubsave&tid='

    opener.open(puburl+str(n))
