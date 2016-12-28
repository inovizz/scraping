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
        title=self.driver.find_elements_by_xpath("/html/body/div[2]/section[1]/div[2]/div")
        #title2=self.driver.find_elements_by_xpath("//*[@id='deity-titleblock']/div/h2")
        Description=self.driver.find_element_by_xpath("/html/body/div[2]/section[3]/div[2]/div/div[1]/p[2]")
        Description=Description.get_attribute("innerHTML").strip()
        Description="".join(Description)
        Description=re.sub("\n",", ",Description)
        Description=re.sub("<[^>]*>","",Description)
        print "Description is::",Description
        url=args.strip()    
        print "url is ::", url
    
        
        if title:
            title_main=title[0].get_attribute('textContent').replace("\n","\t").strip()
            title_main="".join(title_main)
            print "title is::", title_main
        else:
            title_main="".join(title)
            print "text is ::", title_main

   
        with open("data_pending2.csv","ab") as fp:
            fp.write(title_main.encode('utf-8')+'\t')
            fp.write(url.encode('utf-8')+'\t')
            fp.write(Description.encode('utf-8')+'\n')
            
        #time.sleep(3)
        
        self.driver.quit()      
    
     
    def main(self):
        self.url_li=[]
        self.li=[]
        self.fetch()
                
    def fetch(self):
        with open('URL') as fp:
            for line in fp:
                print line
                self.detail(line)
    
if __name__=="__main__":
    crawler().main()