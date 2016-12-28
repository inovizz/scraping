import re
import os
import time
import sys
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class crawler(object):
    
    def detail(self,args):
        self.driver=webdriver.Firefox()
        self.driver.get(args)
        title=self.driver.find_element_by_class_name('titleBar')
        print "title is ::", title.text
        new_data=self.driver.find_element_by_xpath("//*[@id='content']/div/div")
        url=args.strip()    
        print "url is ::", url
	
        if new_data:
            new_data=new_data.get_attribute("innerHTML")
            new_data=new_data.replace("\n","").replace("\t","").replace("\r","")

            Pairings=re.findall(r"<h3>Food\sPairings</h3>\s*(.*?)\s*<a", new_data)
            Pairings="".join(Pairings)
            Pairings=Pairings.replace("<br>",",").strip()
            #Pairings=re.sub("\s*</li>\s*<li.*?>\s*",", ",Pairings)
            Pairings=re.sub("<[^>]*>","",Pairings).strip()
            print "Pairings is ::", Pairings
    
            ABV=re.findall(r"\s*range:\s*(.*?)\s*</b",new_data)
            ABV="".join(ABV)
            ABV=ABV.replace("<br>",",").strip()
            #ABV=re.sub("\s*</li>\s*<li.*?>\s*",", ",ABV)
            ABV=re.sub("<[^>]*>","",ABV).strip()
            print "ABV is ::", ABV
            
            Glassware=re.findall(r"<h3>Glassware</h3>\s*(.*?)\s*<a",new_data)
            Glassware="".join(Glassware)
            #Glassware=Glassware.replace("(\s*<br>\s*|\s*</li>\s*<li.*?>\s*)",", ").strip()
            #Glassware=re.sub("\s*<p>\s*","",Glassware)
            #Glassware=re.sub("\s*<span\sclass='temp'>","",Glassware)
            Glassware=re.sub("<br\s/>","",Glassware)
            Glassware=re.sub("<[^>]*>","",Glassware)
            print "Glassware are ::", Glassware
            
            
            
        with open("data.csv","ab") as fp:
            fp.write(title.text.encode('utf-8')+'\t')
            fp.write(url.encode('utf-8')+'\t')
            fp.write(Pairings.encode('utf-8')+'\t')
            fp.write(ABV.encode('utf-8')+'\t')
            fp.write(Glassware.encode('utf-8')+'\n')

        
            
        time.sleep(3)
        
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
    try:
            data  = self.driver.find_element_by_id("mc_embed_close")
            data = data.get_attribute("innerHTML")
        except:
            data.click()