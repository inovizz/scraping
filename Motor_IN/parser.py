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

		engine_type=re.findall(r'<span>Type</span>([\s\S]*?)</tr>',data)
		engine_type="".join(engine_type)
		engine_type=re.sub("\s*</li>\s*<li.*?>\s*",", ",engine_type)
		engine_type=re.sub("<[^>]*>","",engine_type).strip()
		engine_type=engine_type.replace('\n', "")
		print "engine_type is ::", engine_type

		max_power=re.findall(r'Max[.]\sPower</span>([\s\S]*?)</tr>',data)
		max_power="".join(max_power)
		max_power=re.sub("\s*</li>\s*<li.*?>\s*",", ",max_power)
		max_power=re.sub("<[^>]*>","",max_power).strip()
		max_power=max_power.replace('\n', "")
		print "max_power is ::", max_power

		displacement=re.findall(r'Displacement</span>([\s\S]*?)</tr>',data)
		displacement="".join(displacement)
		displacement=re.sub("\s*</li>\s*<li.*?>\s*",", ",displacement)
		displacement=re.sub("<[^>]*>","",displacement).strip()
		displacement=displacement.replace('\n', "")
		print "displacement is ::", displacement

		tank_capacity=re.findall(r'Tank\sCapacity</span>([\s\S]*?)</tr>',data)
		tank_capacity="".join(tank_capacity)
		tank_capacity=re.sub("\s*</li>\s*<li.*?>\s*",", ",tank_capacity)
		tank_capacity=re.sub("<[^>]*>","",tank_capacity).strip()
		tank_capacity=tank_capacity.replace('\n', "")
		print "tank_capacity is ::", tank_capacity

		weight=re.findall(r'Kerb\sWeight</span>([\s\S]*?)</tr>',data)
		weight="".join(weight)
		weight=re.sub("\s*</li>\s*<li.*?>\s*",", ",weight)
		weight=re.sub("<[^>]*>","",weight).strip()
		weight=weight.replace('\n', "")
		print "weight is ::", weight

		fuel_metering=re.findall(r'Fuel\sMetering</span>([\s\S]*?)</tr>',data)
		fuel_metering="".join(fuel_metering)
		fuel_metering=re.sub("\s*</li>\s*<li.*?>\s*",", ",fuel_metering)
		fuel_metering=re.sub("<[^>]*>","",fuel_metering).strip()
		fuel_metering=fuel_metering.replace('\n', "")
		print "fuel_metering is ::", fuel_metering

		length=re.findall(r'<span>Length</span>([\s\S]*?)</tr>',data)
		length="".join(length)
		length=re.sub("\s*</li>\s*<li.*?>\s*",", ",length)
		length=re.sub("<[^>]*>","",length).strip()
		length=length.replace('\n', "")
		print "length is ::", length

		width=re.findall(r'<span>Width</span>([\s\S]*?)</tr>',data)
		width="".join(width)
		width=re.sub("\s*</li>\s*<li.*?>\s*",", ",width)
		width=re.sub("<[^>]*>","",width).strip()
		width=width.replace('\n', "")
		print "width is ::", width

		height=re.findall(r'<span>Height</span>([\s\S]*?)</tr>',data)
		height="".join(height)
		height=re.sub("\s*</li>\s*<li.*?>\s*",", ",height)
		height=re.sub("<[^>]*>","",height).strip()
		height=height.replace('\n', "")
		print "height is ::", height

		starting=re.findall(r'<span>Starting</span>([\s\S]*?)</tr>',data)
		starting="".join(starting)
		starting=re.sub("\s*</li>\s*<li.*?>\s*",", ",starting)
		starting=re.sub("<[^>]*>","",starting).strip()
		starting=starting.replace('\n', "")
		print "starting is ::", starting

		ignition=re.findall(r'<span>Ignition</span>([\s\S]*?)</tr>',data)
		ignition="".join(ignition)
		ignition=re.sub("\s*</li>\s*<li.*?>\s*",", ",ignition)
		ignition=re.sub("<[^>]*>","",ignition).strip()
		ignition=ignition.replace('\n', "")
		print "ignition is ::", ignition


		with open("data.csv","ab") as fp:
			fp.write(title+'\t')
			fp.write(url+'\t')
			fp.write(engine_type+'\t')
			fp.write(max_power+'\t')
			fp.write(displacement+'\t')
			fp.write(tank_capacity+'\t')
			fp.write(fuel_metering+'\t')
			fp.write(length+'\t')
			fp.write(width+'\t')
			fp.write(weight+'\t')
			fp.write(height+'\t')
			fp.write(starting+'\t')
			fp.write(ignition+'\n')
		#time.sleep(randint(1,3))
		response.close()    
	response.close()