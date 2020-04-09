from helper import fetch
import helper
from json import loads
from helper import process
#from bs4 import BeautifulSoup                  use only for test

class AdvanceWeb:
	def __init__(self,url,data,list,f,content,desc):							#to process responsive kind of website , 
		L=fetch(url)
		if list:													#url is used for get list,data is used to extract data item from result json
			L=loads(L)[data][list]
		else:
			L=loads(L)[data]												# f is a function used to generate data,content is extract data from news and desc is to extract news item
		self.list=map(f,L)				#use map to enumerate
		self.content=content			#save state
		self.desc=desc 					#save state

	def process(self):												#process have been changed to get the news , process function in helper.py then
		for url in self.list:										#process it into format that bikeso can accept
			resultPage = fetch(url)
			result=loads(resultPage)[self.content]
			yield (result['title'],helper.process(result[self.desc]))

#for test only 
if __name__=='__main__':
	url='http://www.imxingzhe.com/api/v4/get_competitions?page=0&limit=500'
	def f(id):
		return 'http://www.imxingzhe.com/api/v4/competition_detail?competition_id='+str(id['id'])
	tmp=AdvanceWeb(url,'data',f,'data','description')
	result=tmp.process()
	for i in result:
		print(process(BeautifulSoup(i,'html.parser')))
