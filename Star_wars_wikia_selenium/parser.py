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

		title=re.findall(r'header-column header-title">\s*<h1>([\s\S]*?)</h',data)
		if title:
			title=title[0]
			title="".join(title)
			title=re.sub("<[^>]*>","",title).strip()
			print "title is ::", title
		else:
			title="".join(title)

		model=re.findall(r'Model[\s\S]*?</td>([\s\S]*?)</tr',data)
		if model:
			model=model[0]
			model="".join(model)
			model=re.sub("<[^>]*>","",model).strip()
			model=re.sub("\n","",model)
			print "model is ::", model
		else:
			model="".join(model)

		Arament=re.findall(r'Armament[\s\S]*?</td>([\s\S]*?)</tr',data)
		if Arament:
			Arament=Arament[0]
			Arament="".join(Arament)
			Arament=re.sub("<[^>]*>","",Arament).strip()
			Arament=re.sub("\n","",Arament)
			Arament=re.sub("\s\s+"," ",Arament)
			print "Arament is ::", Arament
		else:
			Arament="".join(Arament)

		Passengers=re.findall(r'Passengers[\s\S]*?</td>([\s\S]*?)</tr',data)
		if Passengers:
			Passengers=Passengers[0]
			Passengers="".join(Passengers)
			Passengers=re.sub("<[^>]*>","",Passengers).strip()
			Passengers=re.sub("\n","",Passengers)
			Passengers=re.sub("\s\s+"," ",Passengers)
			print "Passengers is ::", Passengers
		else:
			Passengers="".join(Passengers)

		Role=re.findall(r'Role[\s\S]*?</td>([\s\S]*?)</tr',data)

		if Role:
			Role=Role[0]
			Role="".join(Role)
			Role=re.sub("<[^>]*>","",Role).strip()
			Role=re.sub("\n","",Role)
			Role=re.sub("\s\s+"," ",Role)
			print "Role is ::", Role
		else:
			Role="".join(Role)

		Era=re.findall(r'Era[(]s[)][\s\S]*?</td>([\s\S]*?)</tr',data)
		if Era:
			Era=Era[0]
			Era="".join(Era)
			Era=re.sub("<[^>]*>","",Era).strip()
			Era=re.sub("\n","",Era)
			Era=re.sub("\s\s+"," ",Era)
			print "Era is ::", Era
		else:
			Era="".join(Era)

		Affiliation=re.findall(r'Affiliatio[\s\S]*?</td>([\s\S]*?)</tr',data)
		if Affiliation:
			Affiliation=Affiliation[0]
			Affiliation="".join(Affiliation)
			Affiliation=re.sub("<[^>]*>","",Affiliation).strip()
			Affiliation=re.sub("\n","",Affiliation)
			Affiliation=re.sub("\s\s+"," ",Affiliation)
			print "Affiliation is ::", Affiliation
		else:
			Affiliation="".join(Affiliation)


		Year_introduced=re.findall(r'Year\sintroduced[\s\S]*?</td>([\s\S]*?)</tr',data)
		if Year_introduced:
			Year_introduced=Year_introduced[0]
			Year_introduced="".join(Year_introduced)
			Year_introduced=re.sub("<[^>]*>","",Year_introduced).strip()
			Year_introduced=re.sub("\n","",Year_introduced)
			Year_introduced=re.sub("\s\s+"," ",Year_introduced)
			print "Year_introduced is ::", Year_introduced
		else:
			Year_introduced="".join(Year_introduced)

		with open("data1.csv","ab") as fp:
			fp.write(url+'\t')
			fp.write(title+'\t')
			fp.write(model+'\t')
			fp.write(Arament+'\t')
			fp.write(Passengers+'\t')
			fp.write(Role+'\t')
			fp.write(Era+'\t')
			fp.write(Year_introduced+'\t')
			fp.write(Affiliation+'\n')
		
		time.sleep(randint(1,5))
		response.close()    
	response.close()