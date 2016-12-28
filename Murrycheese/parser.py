import re
import os
import time
import sys
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()

class crawler(object):
    
    def detail(self,args):
        self.driver=webdriver.Chrome()
        self.driver.get(args)
        '''
        try:
	        data  = self.driver.find_element_by_id("mc_embed_close")
	        data = data.get_attribute("innerHTML")
	    except:
	    	data.click()
	    '''
	    	
        #title=self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/ul/li[3]/span")
        #print "title is ::", title.text
        new_data=self.driver.find_element_by_xpath("/html/body")
        url=args.strip()    
        print "######url is ::", url
	
        if new_data:
            new_data=new_data.get_attribute("innerHTML")
            new_data=new_data.replace("\n","").replace("\t","").replace("\r","")
            
            Title=self.driver.find_element_by_class_name('product')
            Title=Title.text
            Title="".join(Title)
            Title=Title.strip()
            Title=Title.replace("<br>",",").strip()
            Title=re.sub("\s*</li>\s*<li.*?>\s*",", ",Title)
            Title=re.sub("<[^>]*>","",Title).strip()
            print "Title is ::", Title

            Country=re.findall(r"Country</th>(.*?)</tr", new_data)
            Country="".join(Country)
            Country=Country.strip()
            Country=Country.replace("<br>",",").strip()
            Country=re.sub("\s*</li>\s*<li.*?>\s*",", ",Country)
            Country=re.sub("<[^>]*>","",Country).strip()
            print "Country is ::", Country
           
            Region=re.findall(r"Region</th>(.*?)</tr", new_data)
            Region="".join(Region)
            Region=Region.strip()
            Region=Region.replace("<br>",",").strip()
            Region=re.sub("\s*</li>\s*<li.*?>\s*",", ",Region)
            Region=re.sub("<[^>]*>","",Region).strip()
            print "Region is ::", Region

            Maker=re.findall(r"Maker</th>(.*?)</tr", new_data)
            Maker="".join(Maker)
            Maker=Maker.strip()
            Maker=Maker.replace("<br>",",").strip()
            Maker=re.sub("\s*</li>\s*<li.*?>\s*",", ",Maker)
            Maker=re.sub("<[^>]*>","",Maker).strip()
            print "Maker is ::", Maker

            Milk_type=re.findall(r"Milk\sType</th>(.*?)</tr", new_data)
            Milk_type="".join(Milk_type)
            Milk_type=Milk_type.strip()
            Milk_type=Milk_type.replace("<br>",",").strip()
            Milk_type=re.sub("\s*</li>\s*<li.*?>\s*",", ",Milk_type)
            Milk_type=re.sub("<[^>]*>","",Milk_type).strip()
            print "Milk_type is ::", Milk_type

            Pasteurization=re.findall(r"Pasteurization</th>(.*?)</tr", new_data)
            Pasteurization="".join(Pasteurization)
            Pasteurization=Pasteurization.strip()
            Pasteurization=Pasteurization.replace("<br>",",").strip()
            Pasteurization=re.sub("\s*</li>\s*<li.*?>\s*",", ",Pasteurization)
            Pasteurization=re.sub("<[^>]*>","",Pasteurization).strip()
            print "Pasteurization is ::", Pasteurization

            Rennet_type=re.findall(r"Rennet\sType</th>(.*?)</tr", new_data)
            Rennet_type="".join(Rennet_type)
            Rennet_type=Rennet_type.strip()
            Rennet_type=Rennet_type.replace("<br>",",").strip()
            Rennet_type=re.sub("\s*</li>\s*<li.*?>\s*",", ",Rennet_type)
            Rennet_type=re.sub("<[^>]*>","",Rennet_type).strip()
            print "Rennet_type is ::", Rennet_type

            Age=re.findall(r"Age</th>(.*?)</tr", new_data)
            Age="".join(Age)
            Age=Age.strip()
            Age=Age.replace("<br>",",").strip()
            Age=re.sub("\s*</li>\s*<li.*?>\s*",", ",Age)
            Age=re.sub("<[^>]*>","",Age).strip()
            print "Age is ::", Age

            Cheese_type=re.findall(r"Cheese\sType</th>(.*?)</tr", new_data)
            Cheese_type="".join(Cheese_type)
            Cheese_type=Cheese_type.strip()
            Cheese_type=Cheese_type.replace("<br>",",").strip()
            Cheese_type=re.sub("\s*</li>\s*<li.*?>\s*",", ",Cheese_type)
            Cheese_type=re.sub("<[^>]*>","",Cheese_type).strip()
            print "Cheese_type is ::", Cheese_type

            Wheel_weight=re.findall(r"Wheel\sWeight</th>(.*?)</tr", new_data)
            Wheel_weight="".join(Wheel_weight)
            Wheel_weight=Wheel_weight.strip()
            Wheel_weight=Wheel_weight.replace("<br>",",").strip()
            Wheel_weight=re.sub("\s*</li>\s*<li.*?>\s*",", ",Wheel_weight)
            Wheel_weight=re.sub("<[^>]*>","",Wheel_weight).strip()
            print "Wheel_weight is ::", Wheel_weight

            Description=self.driver.find_element_by_css_selector("div.short-description")
            Description=Description.text
            Description="".join(Description)
            Description=Description.replace("\n"," ").strip()
            Description=Description.replace("<br>",",").strip()
            Description=re.sub("\s*</li>\s*<li.*?>\s*",", ",Description)
            Description=re.sub("<[^>]*>","",Description).strip()
            print "Description is ::", Description

        time.sleep(3)       

        with open("Data_updated.csv","ab") as fp:
            #try:
            fp.write(Title.encode('utf-8')+'\t')
            fp.write(url.encode('utf-8')+'\t')
            fp.write(Country.encode('utf-8')+'\t')
            fp.write(Region.encode('utf-8')+'\t')
            fp.write(Maker.encode('utf-8')+'\t')
            fp.write(Milk_type.encode('utf-8')+'\t')
            fp.write(Pasteurization.encode('utf-8')+'\t')
            fp.write(Rennet_type.encode('utf-8')+'\t')
            fp.write(Age.encode('utf-8')+'\t')
            fp.write(Cheese_type.encode('utf-8')+'\t')
            fp.write(Wheel_weight.encode('utf-8')+'\t')
            fp.write(Description.encode('utf-8')+'\n')
            #except:
            #  print url
            
        self.driver.quit()      
     
    def main(self):
        self.url_li=[]
        self.li=[]
        self.fetch()
                
    def fetch(self):
        with open('URLpending') as fp:
            for line in fp.readlines():
                if line.strip():
                    self.detail(line)
                    
    
if __name__=="__main__":
    crawler().main()
import csv