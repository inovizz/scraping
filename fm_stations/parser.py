#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import urllib2
import csv
import re
import time
from random import randint
from time import sleep

with open("URLs", 'r') as f:
	for line in f:
		response=urllib2.urlopen(line)
		data=response.read()

		url = line
		url="".join(url)
		url=re.sub("\n","",url)
		print "url is ::", url

		title=re.findall(r'<h1.*>(.*?)</h1',data)
		title="".join(title)
		title=re.sub("\s*</li>\s*<li.*?>\s*",", ",title)
		title=re.sub("<[^>]*>","",title).strip()
		print "title is ::", title

		city_of_license=re.findall(r'City\sof\slicense</a></th>([\s\S]*?)</tr>',data)
		city_of_license="".join(city_of_license)
		city_of_license=re.sub("\s*</li>\s*<li.*?>\s*",", ",city_of_license)
		city_of_license=re.sub("<[^>]*>","",city_of_license).strip()
		city_of_license=city_of_license.replace('\n', "")
		print "city_of_license is ::", city_of_license

		broadcast_area=re.findall(r'Broadcast\sarea</th>([\s\S]*?)</tr>',data)
		broadcast_area="".join(broadcast_area)
		broadcast_area=re.sub("\s*</li>\s*<li.*?>\s*",", ",broadcast_area)
		broadcast_area=re.sub("<[^>]*>","",broadcast_area).strip()
		broadcast_area=broadcast_area.replace('\n', "")
		print "broadcast_area is ::", broadcast_area

		branding=re.findall(r'Branding</th>([\s\S]*?)</tr>',data)
		branding="".join(branding)
		branding=re.sub("\s*</li>\s*<li.*?>\s*",", ",branding)
		branding=re.sub("<[^>]*>","",branding).strip()
		branding=branding.replace('\n', "")
		print "branding is ::", branding

		slogan=re.findall(r'Slogan</a>([\s\S]*?)</tr>',data)
		slogan="".join(slogan)
		slogan=re.sub("\s*</li>\s*<li.*?>\s*",", ",slogan)
		slogan=re.sub("<[^>]*>","",slogan).strip()
		slogan=slogan.replace('\n', "")
		print "slogan is ::", slogan

		frequency=re.findall(r'Frequency</a>([\s\S]*?)</tr>',data)
		frequency="".join(frequency)
		frequency=re.sub("\s*</li>\s*<li.*?>\s*",", ",frequency)
		frequency=re.sub("<[^>]*>","",frequency).strip()
		frequency=frequency.replace('\n', "")
		print "frequency is ::", frequency

		first_air_date=re.findall(r'First\sair\sdate</th>([\s\S]*?)</tr>',data)
		first_air_date="".join(first_air_date)
		first_air_date=re.sub("\s*</li>\s*<li.*?>\s*",", ",first_air_date)
		first_air_date=re.sub("<[^>]*>","",first_air_date).strip()
		first_air_date=first_air_date.replace('\n', "")
		print "first_air_date is ::", first_air_date

		owner=re.findall(r'Owner</th>([\s\S]*?)</tr>',data)
		owner="".join(owner)
		owner=re.sub("\s*</li>\s*<li.*?>\s*",", ",owner)
		owner=re.sub("<[^>]*>","",owner).strip()
		owner=owner.replace('\n', "")
		print "owner is ::", owner

		broadcast_areaa=re.findall(r'Broadcast\sarea</th>([\s\S]*?)</tr>',data)
		broadcast_areaa="".join(broadcast_areaa)
		broadcast_areaa=re.sub("\s*</li>\s*<li.*?>\s*",", ",broadcast_areaa)
		broadcast_areaa=re.sub("<[^>]*>","",broadcast_areaa).strip()
		broadcast_areaa=broadcast_areaa.replace('\n', "")
		print "broadcast_areaa is ::", broadcast_areaa

		website=re.findall(r'Website</th>([\s\S]*?)</tr>',data)
		website="".join(website)
		website=re.sub("\s*</li>\s*<li.*?>\s*",", ",website)
		website=re.sub("<[^>]*>","",website).strip()
		website=website.replace('\n', "")
		print "website is ::", website

		webcast=re.findall(r'Webcast</a></th>([\s\S]*?)</tr>',data)
		webcast="".join(webcast)
		webcast=re.sub("\s*</li>\s*<li.*?>\s*",", ",webcast)
		webcast=re.sub("<[^>]*>","",webcast).strip()
		webcast=webcast.replace('\n', "")
		print "webcast is ::", webcast

		with open("data_pending2.csv","ab") as fp:
			fp.write(title+'\t')
			fp.write(url+'\t')
			fp.write(city_of_license+'\t')
			fp.write(broadcast_area+'\t')
			fp.write(branding+'\t')
			fp.write(slogan+'\t')
			fp.write(frequency+'\t')
			fp.write(first_air_date+'\t')
			fp.write(owner+'\t')
			fp.write(broadcast_areaa+'\t')
			fp.write(website+'\t')
			fp.write(webcast+'\n')
		time.sleep(randint(1,5))
		response.close()    
	response.close()