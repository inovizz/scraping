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
        title=self.driver.find_element_by_xpath("//*[@id='firstHeading']/span")
        print "title is ::", title.text
        new_data=self.driver.find_element_by_xpath("//*[@id='mw-content-text']/table[3]")
        url=args.strip()    
        print "url is ::", url
	
        if new_data:
            new_data=new_data.text
            #new_data=new_data.replace("\n","").replace("\t","").replace("\r","")

            Hidden_ability=re.findall(r"(.*)\nHidden\sAbility", new_data)
            Hidden_ability="".join(Hidden_ability)
            Hidden_ability=Hidden_ability.strip()
            #Hidden_ability=Hidden_ability.replace("<br>",",").strip()
            #Hidden_ability=re.sub("\s*</li>\s*<li.*?>\s*",", ",Hidden_ability)
            #Hidden_ability=re.sub("<[^>]*>","",Hidden_ability).strip()
            print "Hidden_ability is ::", Hidden_ability
    		
            
        with open("Final.csv","ab") as fp:
            try:
              fp.write(title.text.encode('utf-8')+'\t')
              fp.write(url.encode('utf-8')+'\t')
              fp.write(Hidden_ability.encode('utf-8')+'\n')
            except:
              print url
            
            
        #time.sleep(3)
        
        self.driver.quit()      
     
    def main(self):
        self.url_li=[]
        self.li=[]
        self.fetch()
                
    def fetch(self):
        with open('URLs') as fp:
            for line in fp.readlines():
                if line.strip():
                    self.detail(line)
                    
    
if __name__=="__main__":
    crawler().main()
    
