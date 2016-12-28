import urllib2
import csv
import re
import time
from random import randint
from time import sleep

with open("URLsp", 'r') as f:
	for line in f:
		response=urllib2.urlopen(line)
		data=response.read()

		url = line
		url="".join(url)
		url=re.sub("\n","",url)
		print "url is ::", url

		title=re.findall(r'<h3>(.*?)</h3',data)[0]
		title="".join(title)
		title=re.sub("\s*</li>\s*<li.*?>\s*",", ",title)
		title=re.sub("<[^>]*>","",title).strip()
		print "title is ::", title

		with open("data.csv","ab") as fp:
			fp.write(url.encode('utf-16')+'\t')
			fp.write(title.encode('utf-16')+'\n')
		time.sleep(randint(1,5))
		response.close()    
	response.close()


'''		
i=0
li=[]
for i in range(1,1800,15):
	response = urllib2.urlopen("http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=2oq%2Cc1r&filterNone=true&start="+str(i)+"&ajax=true&_=1434642957147")
	data=response.read()
	links=re.findall(r'href="(.*?)["]\stitle', data)
	print len(links)
	for i in xrange(len(links)):
		#print links[i]
		try:
			page=urllib2.urlopen("http://www.flipkart.com"+str(links[i]))
		except SocketError as e:
			if e.errno != errno.ECONNRESET:
				raise # Not error we are looking for
		pass # Handle error here.
		page=page.read()
		#print page
		url = "http://www.flipkart.com"+str(links[i])
		url="".join(url)
		print "url is ::", url
		title=re.findall(r'<h1.*>(.*?)</h1',page)
		title="".join(title)
		title=re.sub("\s*</li>\s*<li.*?>\s*",", ",title)
		title=re.sub("<[^>]*>","",title).strip()
		print "title is ::", title
		
		engine_type = re.findall(r'.*?selling-engine_type\somniture-field.*>(.*?)</span>', page)
		engine_type="".join(engine_type)
		engine_type=re.sub("\s*</li>\s*<li.*?>\s*",", ",engine_type)
		engine_type=re.sub("<[^>]*>","",engine_type).strip()
		print "engine_type is ::", engine_type
		randint(10,100)
		with open("data.csv","ab") as fp:
			fp.write(title.encode('utf-8')+'\t')
			fp.write(url.encode('utf-8')+'\t')
			fp.write(engine_type.encode('utf-8')+'\n')
		time.sleep(randint(1,5))
		response.close()    
	response.close()
'''	
