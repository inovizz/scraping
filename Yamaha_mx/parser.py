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
		print type(data)

		url = line
		url="".join(url)
		url=re.sub("\n","",url)
		print "url is ::", url

		title=re.findall(r'maincontent-right">[\s\S]*?<h3>([\s\S]*?)</h3',data)
		title="".join(title)
		title=re.sub("\s*</li>\s*<li.*?>\s*",", ",title)
		title=re.sub("<[^>]*>","",title).strip()
		print "title is ::", title

		Description=re.findall(r'class="maincontent-right">([\s\S]*?)<div\sclass="line_2',data)
		Description="".join(Description)
		Description=re.sub("\s*</li>\s*<li.*?>\s*",", ",Description)
		Description=re.sub("<[^>]*>","",Description).rstrip()
		Description.replace('\n', "").replace('\r', "").replace('\t', " ")
		Description=re.sub("\s\s+"," ",Description)
		print "Description is ::" + Description + "<EOL>"

		'''
		Engine_type=re.findall(r'Motor</strong>([\s\S]*?)</tr',data)
		Engine_type="".join(Engine_type)
		Engine_type=re.sub("\s*</li>\s*<li.*?>\s*",", ",Engine_type)
		Engine_type=re.sub("<[^>]*>","",Engine_type).strip()
		Engine_type=re.sub("\n","",Engine_type)
		Description=re.sub("\n\n","",Description)
		Description=re.sub("\t","",Description)
		print "Engine_type is ::", Engine_type

		Engine_capacity=re.findall(r'Cilindrada</strong>([\s\S]*?)</tr',data)
		Engine_capacity="".join(Engine_capacity)
		Engine_capacity=re.sub("\s*</li>\s*<li.*?>\s*",", ",Engine_capacity)
		Engine_capacity=re.sub("<[^>]*>","",Engine_capacity).strip()
		Engine_capacity=re.sub("\n","",Engine_capacity)
		print "Engine_capacity is ::", Engine_capacity

		Fuel_capacity=re.findall(r'de\scombustible\s</strong>([\s\S]*?)</tr',data)
		Fuel_capacity="".join(Fuel_capacity)
		Fuel_capacity=re.sub("\s*</li>\s*<li.*?>\s*",", ",Fuel_capacity)
		Fuel_capacity=re.sub("<[^>]*>","",Fuel_capacity).strip()
		Fuel_capacity=re.sub("\n","",Fuel_capacity)
		print "Fuel_capacity is ::", Fuel_capacity

		Transmission=re.findall(r'Transmisi&oacute;n</strong>([\s\S]*?)</tr',data)
		Transmission="".join(Transmission)
		Transmission=re.sub("\s*</li>\s*<li.*?>\s*",", ",Transmission)
		Transmission=re.sub("<[^>]*>","",Transmission).strip()
		Transmission=re.sub("\n","",Transmission)
		print "Transmission is ::", Transmission

		Weight=re.findall(r'l&iacute;quidos\s</strong>([\s\S]*?)</tr',data)
		Weight="".join(Weight)
		Weight=re.sub("\s*</li>\s*<li.*?>\s*",", ",Weight)
		Weight=re.sub("<[^>]*>","",Weight).strip()
		Weight=re.sub("\n","",Weight)
		print "Weight is ::", Weight
		'''

		with open("data_description.csv","ab") as fp:
			fp.write(title+'\t')
			fp.write(url+'\t')
			fp.write(Description+'\n')
			'''
			fp.write(Engine_type+'\t')
			fp.write(Engine_capacity+'\t')
			fp.write(Fuel_capacity+'\t')
			fp.write(Transmission+'\t')
			fp.write(Weight+'\n')
			'''
		
		time.sleep(randint(1,5))
		response.close()    
	response.close()