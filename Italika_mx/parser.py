#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import urllib2
import csv
import re
import time
from random import randint
from time import sleep

with open("links", 'r') as f:
	for line in f:
		response=urllib2.urlopen(line)
		data=response.read()
		print type(data)

		url = line
		url="".join(url)
		url=re.sub("\n","",url)
		print "url is ::", url

		title=re.findall(r'<h1.*>(.*?)</h1',data)
		title="".join(title)
		title=re.sub("\s*</li>\s*<li.*?>\s*",", ",title)
		title=re.sub("<[^>]*>","",title).strip()
		print "title is ::", title

		Fuel_capacity=re.findall(r'combustible:</p>[\s\S]*?<p>(.*)</p>',data)
		Fuel_capacity="".join(Fuel_capacity)
		Fuel_capacity=re.sub("\s*</li>\s*<li.*?>\s*",", ",Fuel_capacity)
		Fuel_capacity=re.sub("<[^>]*>","",Fuel_capacity).strip()
		print "Fuel_capacity is ::", Fuel_capacity

		Engine_capacity=re.findall(r'Desplazamiento\sde\spistones:</p>[\s\S]*?<p>(.*)</p>',data)
		Engine_capacity="".join(Engine_capacity)
		Engine_capacity=re.sub("\s*</li>\s*<li.*?>\s*",", ",Engine_capacity)
		Engine_capacity=re.sub("<[^>]*>","",Engine_capacity).strip()
		print "Engine_capacity is ::", Engine_capacity

		Power=re.findall(r'Potencia\sMáxima:</p>[\s\S]*?<p>(.*)</p',data)
		Power="".join(Power)
		Power=re.sub("\s*</li>\s*<li.*?>\s*",", ",Power)
		Power=re.sub("<[^>]*>","",Power).strip()
		print "Power is ::", Power

		Torque=re.findall(r'Torque\smáximo:</p>[\s\S]*?<p>(.*)</p',data)
		Torque="".join(Torque)
		Torque=re.sub("\s*</li>\s*<li.*?>\s*",", ",Torque)
		Torque=re.sub("<[^>]*>","",Torque).strip()
		print "Torque is ::", Torque

		Transmission=re.findall(r'Transmisión:</p>[\s\S]*?<p>(.*)</p',data)
		Transmission="".join(Transmission)
		Transmission=re.sub("\s*</li>\s*<li.*?>\s*",", ",Transmission)
		Transmission=re.sub("<[^>]*>","",Transmission).strip()
		print "Transmission is ::", Transmission

		with open("data_complete.csv","ab") as fp:
			fp.write(title+'\t')
			fp.write(url+'\t')
			fp.write(Fuel_capacity+'\t')
			fp.write(Engine_capacity+'\t')
			fp.write(Power+'\t')
			fp.write(Torque+'\t')
			fp.write(Transmission+'\n')
		
		time.sleep(randint(1,5))
		response.close()    
	response.close()