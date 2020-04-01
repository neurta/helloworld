from advanceWeb import AdvanceWeb
from Web import Web
from helper import fetch

url='http://www.blackbirdsport.com/public/api/activities?activityType=1&pageNum=0&pageSize=50'
def f(id):
	return 'http://www.blackbirdsport.com/public/competitions/'+str(id['activityId'])
tmp=AdvanceWeb(url,'content',f,'content','description')
print(fetch(tmp.list[0]))


#dont forget to use process in helper.py to generate the format that bikeso can accept
