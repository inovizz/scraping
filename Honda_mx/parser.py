#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import urllib2
import csv
import re
import time
from random import randint
from time import sleep

with open("Links", 'r') as f:
	for line in f:
		response=urllib2.urlopen(line)
		data=response.read()
		print type(data)

		url = line
		url="".join(url)
		url=re.sub("\n","",url)
		print "url is ::", url

		title=re.findall(r'<title>([\s\S]*?)</title',data)
		title="".join(title)
		title=re.sub("\s*</li>\s*<li.*?>\s*",", ",title)
		title=re.sub("<[^>]*>","",title).strip()
		print "title is ::", title

		Engine_type=re.findall(r'MOTOR\sY\sC.C.</div>([\s\S]*?)</div',data)
		Engine_type="".join(Engine_type)
		Engine_type=re.sub("\s*</li>\s*<li.*?>\s*",", ",Engine_type)
		Engine_type=re.sub("<[^>]*>","",Engine_type).strip()
		Engine_type=re.sub("\n","",Engine_type)
		print "Engine_type is ::", Engine_type

		Engine_capacity=re.findall(r'CILINDRADA</div>([\s\S]*?)</div',data)
		Engine_capacity="".join(Engine_capacity)
		Engine_capacity=re.sub("\s*</li>\s*<li.*?>\s*",", ",Engine_capacity)
		Engine_capacity=re.sub("<[^>]*>","",Engine_capacity).strip()
		Engine_capacity=re.sub("\n","",Engine_capacity)
		print "Engine_capacity is ::", Engine_capacity

		Power=re.findall(r'<div\sclass="titulo">POTENCIA.*?</div>([\s\S]*?)</div',data)
		Power="".join(Power)
		Power=re.sub("\s*</li>\s*<li.*?>\s*",", ",Power)
		Power=re.sub("<[^>]*>","",Power).strip()
		Power=re.sub("\n","",Power)
		print "Power is ::", Power

		Torque=re.findall(r'TORQUE</div>([\s\S]*?)</div',data)
		Torque="".join(Torque)
		Torque=re.sub("\s*</li>\s*<li.*?>\s*",", ",Torque)
		Torque=re.sub("<[^>]*>","",Torque).strip()
		Torque=re.sub("\n","",Torque)
		print "Torque is ::", Torque

		Fuel_capacity=re.findall(r'class="titulo">CAP.\sDE.*?</div>([\s\S]*?)</div',data)
		Fuel_capacity="".join(Fuel_capacity)
		Fuel_capacity=re.sub("\s*</li>\s*<li.*?>\s*",", ",Fuel_capacity)
		Fuel_capacity=re.sub("<[^>]*>","",Fuel_capacity).strip()
		Fuel_capacity=re.sub("\n","",Fuel_capacity)
		print "Fuel_capacity is ::", Fuel_capacity

		Transmission=re.findall(r'class="titulo">TRANSMISIÓN</div>([\s\S]*?)</div',data)
		Transmission="".join(Transmission)
		Transmission=re.sub("\s*</li>\s*<li.*?>\s*",", ",Transmission)
		Transmission=re.sub("<[^>]*>","",Transmission).strip()
		Transmission=re.sub("\n","",Transmission)
		print "Transmission is ::", Transmission

		'''
		Weight=re.findall(r'l&iacute;quidos\s</strong>([\s\S]*?)</tr',data)
		Weight="".join(Weight)
		Weight=re.sub("\s*</li>\s*<li.*?>\s*",", ",Weight)
		Weight=re.sub("<[^>]*>","",Weight).strip()
		Weight=re.sub("\n","",Weight)
		print "Weight is ::", Weight
		'''


		with open("data_description.csv","ab") as fp:
			fp.write(url+'\t')
			fp.write(title+'\t')
			fp.write(Engine_type+'\t')
			fp.write(Engine_capacity+'\t')
			fp.write(Power+'\t')
			fp.write(Torque+'\t')
			fp.write(Fuel_capacity+'\t')
			fp.write(Transmission+'\n')
		
		time.sleep(randint(1,5))
		response.close()    
	response.close()