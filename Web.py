from helper import fetch
import re
from bs4 import BeautifulSoup
from helper import tag
class Web:
    def __init__(self,url,class_id,list_id,content_id):             #url is the list url , class_id and list_id is used to find news url and content id is used to find the news
        self.class_id=class_id
        self.list_id=list_id
        self.url=url
        self.content_id=content_id
        self.soup=BeautifulSoup(fetch(url))

    def getlist(self):
        self.list=Web.__getlist(self.soup,self.class_id,self.list_id)

    def addlist(self,list):
        self.list=list

    def fetch(url):  # To fetch the web page, it was used in a lot of file
        req = request.urlopen(url)
        page = req.read()
        page = page.decode('utf-8')
        return page
    
    def process(self):                # to fetch n news
        for i in self.list:
            #print(i)                   #for test only,this is no longer useful
            soup = BeautifulSoup(fetch(i),'html.parser')
            yield Web.__process(soup,self.content_id)

    def map(self,f):
        self.list=map(f,self.list)

    @staticmethod
    def __process(soup, content_id):
        # general processing for event
        title = soup.find('title').text
        soup = soup.find(class_=content_id)
        newsoup = soup.find_all('p')
        s = ''
        for i in newsoup:  # to generate the content needed to post
            if i.text is '':
                result = re.findall('src="(.*?)"', str(i))  # use the re to find the url
                if len(result) is 0:
                    print(i)
                else:
                    s += tag(result[0], '[img]', '[/img]')
            else:
                s += tag(i.text, '[align=left][color=#666666][font=微软雅黑][size=14px]', '[/size][/font][/color][/align]')
        return (title,s)

    @staticmethod
    def __getlist(soup, class_id, list_id):
        return_list = list()
        newsoup = soup.find(class_=class_id)
        newsoup = newsoup.find_all(class_=list_id)
        for i in newsoup:
            result = re.findall('href="(.*?)"', str(i))
            if not len(result) is 0:  # to rule out the empty list
                append(return_list,result)
        return return_list


def append(a,b):
    if len(b) is 0:
        return a
    else:
        a.append(b[0])
        append(a,b[1:])
