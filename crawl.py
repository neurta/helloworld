from bs4 import BeautifulSoup
import Submit
from helper import fetch,tag

#code below are helper function write specfic for wildto.com

def findSoup(things):
    soup = BeautifulSoup(things,'html.parser')
    return soup

def findStuff(soup):
    return BeautifulSoup(str(soup.find(id='cmptNote')),'html.parser')

def findText(soup):
    return soup.get_text()

def findImg(soup):
    return soup.find_all('img')



def process(url,n):
    print("go")
    data = fetch(url)
    print("ok")
    soup = findSoup(data)
    soup = findStuff(soup)

    s=str()
    subject=str()
    for i in findText(soup).split('\n'):
        if not subject:
            subject = str(i);
        if i:
            s+=tag(str(i),'[align=left][color=#666666][font=微软雅黑][size=14px]','[/size][/font][/color][/align]')

    for i in findImg(soup):
        if i:
            s+=tag(str(i),'[img]','[/img]')
    Submit.post(subject,s,n)
#helper functions end

if __name__ == '__main__':             # write this in order to make this module reusable
    n=6031
    for i in range(3501,3572):
        url=tag(str(i),'http://www.wildto.com/event/','.html')
        print("start processing ")
        print(url)
        process(url,n)
        n+=1
