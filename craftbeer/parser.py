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
        title=self.driver.find_element_by_class_name('entry-title')
        print "title is ::", title.text
        new_data=self.driver.find_element_by_xpath("//*[@id='main']")
        url=args.strip()    
        print "url is ::", url
	
        if new_data:
            new_data=new_data.get_attribute("innerHTML")
            new_data=new_data.replace("\n","").replace("\t","").replace("\r","")
            
            IBU=self.driver.find_element_by_xpath("//*[@id='sliders']/div[2]/label[3]/a/span")
            IBU="".join(IBU.text)
            IBU=re.sub("<br>",", ",IBU)
            IBU=re.sub("<[^>]*>","",IBU)
            print "IBU is ::", IBU
            
            SRM=self.driver.find_element_by_xpath("//*[@id='srm']/span ")
            SRM="".join(SRM.text)
            SRM=re.sub("<br>",", ",SRM)
            SRM=re.sub("<[^>]*>","",SRM)
            print "SRM is ::", SRM
            
            ABV=self.driver.find_element_by_xpath("//*[@id='sliders']/div[3]/label[3]/a/span")
            ABV="".join(ABV.text)
            ABV=re.sub("<br>",", ",ABV)
            ABV=re.sub("<[^>]*>","",ABV)
            print "ABV is ::", ABV
            
            Alchohal=self.driver.find_element_by_xpath("//*[@id='flavor']/p[1]")
            Alchohal="".join(Alchohal.text)
            Alchohal=re.sub("<br>",", ",Alchohal)
            Alchohal=re.sub("<[^>]*>","",Alchohal)
            print "Alchohal is ::", Alchohal
            
            Hop=self.driver.find_element_by_xpath("//*[@id='flavor']/p[2]")
            Hop="".join(Hop.text)
            Hop=re.sub("<br>",", ",Hop)
            Hop=re.sub("<[^>]*>","",Hop)
            print "Hop is ::", Hop
            
            
            Malt=self.driver.find_element_by_xpath("//*[@id='flavor']/p[3]")
            Malt="".join(Malt.text)
            Malt=re.sub("<br>",", ",Malt)
            Malt=re.sub("<[^>]*>","",Malt)
            print "Malt is ::", Malt
            
            
            Esters=self.driver.find_element_by_xpath("//*[@id='flavor']/p[4]")
            Esters="".join(Esters.text)
            Esters=Esters.replace("<br>",",").strip()
            Esters=re.sub("<[^>]*>","",Esters)	
            print "Esters is ::", Esters
            
            
            PHENOLS=self.driver.find_element_by_xpath("//*[@id='flavor']/p[5]")
            PHENOLS="".join(PHENOLS.text)
            PHENOLS=PHENOLS.replace("<br>",",").strip()
            PHENOLS=re.sub("<[^>]*>","",PHENOLS)	
            print "PHENOLS is ::", PHENOLS
            
            Color=self.driver.find_element_by_xpath("//*[@id='appearance']/p[1]")
            Color="".join(Color.text)
            Color=Color.replace("<br>",",").strip()
            Color=re.sub("<[^>]*>","",Color)	
            print "Color is ::", Color
            
            
            ingredient_hops=self.driver.find_element_by_xpath("//*[@id='process']/p[1]")
            ingredient_hops="".join(ingredient_hops.text)
            ingredient_hops=ingredient_hops.replace("<br>","").strip()
            ingredient_hops=re.sub("<[^>]*>","",ingredient_hops)	
            print "ingredient_hops are ::", ingredient_hops
            
            ingredient_malts=self.driver.find_element_by_xpath("//*[@id='process']/p[2]")
            ingredient_malts="".join(ingredient_malts.text)
            ingredient_malts=ingredient_malts.replace("<br>",",").strip()
            ingredient_malts=re.sub("<[^>]*>","",ingredient_malts)	
            print "ingredient_malts is ::", ingredient_malts
            
            try:
                ingredient_yeast=self.driver.find_element_by_xpath("//*[@id='process']/p[4]")
            except Exception:
                ingredient_yeast = "Null"
            else:                
                ingredient_yeast="".join(ingredient_yeast.text)   
            ingredient_yeast=ingredient_yeast.replace("<br>",",").strip()
            ingredient_yeast=re.sub("<[^>]*>","",ingredient_yeast)	
            print "ingredient_yeast are ::", ingredient_yeast
            
            Pairings=re.findall(r"Pairings<\/h3>.*?<ul>(.*?)<\/ul",new_data)
            Pairings="".join(Pairings)
            #Pairings=Pairings.replace("<br>",",").strip()
            Pairings=re.sub("\s*</li>\s*<li.*?>\s*",", ",Pairings)
            Pairings=re.sub("<[^>]*>","",Pairings).strip()
            print "Pairings is ::", Pairings
            
            Glassware=re.findall(r"Serving\sTemperature.*?<\/h3>(.*?)</p",new_data)
            Glassware="".join(Glassware)
            Glassware=Glassware.replace("(\s*<br>\s*|\s*</li>\s*<li.*?>\s*)",", ").strip()
            Glassware=re.sub("\s*<p>\s*","",Glassware)
            Glassware=re.sub("\s*<span\sclass='temp'>","",Glassware)
            Glassware=re.sub("<br\s/>","",Glassware)
            Glassware=re.sub("<[^>]*>","",Glassware)
            print "Glassware are ::", Glassware
            
            Commercial_examples=re.findall(r"Examples<\/h3>.*?<ul\sclass=['\"]winners['\"]>(.*?)<\/ul",new_data)
            Commercial_examples="".join(Commercial_examples)
            Commercial_examples=re.sub("\s*</li>\s*<li.*?>\s*",", ",Commercial_examples)
            Commercial_examples=re.sub("<[^>]*>","",Commercial_examples).strip()	
            print "Commercial_examples is ::", Commercial_examples
                  
        with open("data_new.csv","ab") as fp:
            fp.write(title.text.encode('utf-8')+'\t')
            fp.write(url.encode('utf-8')+'\t')
            fp.write(IBU.encode('utf-8')+'\t')
            fp.write(SRM.encode('utf-8')+'\t')
            fp.write(ABV.encode('utf-8')+'\t')
            fp.write(Alchohal.encode('utf-8')+'\t')
            fp.write(Hop.encode('utf-8')+'\t')
            fp.write(Malt.encode('utf-8')+'\t')
            fp.write(Esters.encode('utf-8')+'\t')
            fp.write(PHENOLS.encode('utf-8')+'\t')
            fp.write(Color.encode('utf-8')+'\t')
            fp.write(ingredient_hops.encode('utf-8')+'\t')
            fp.write(ingredient_malts.encode('utf-8')+'\t')    
            fp.write(ingredient_yeast.encode('utf-8')+'\t')
            fp.write(Glassware.encode('utf-8')+'\t')
            fp.write(Commercial_examples.encode('utf-8')+'\t')
            fp.write(Pairings.encode('utf-8')+'\n')
            
        time.sleep(3)
        
        self.driver.quit()      
     
    def main(self):
        self.url_li=[]
        self.li=[]
        self.fetch()
                
    def fetch(self):
        with open('URLs','r') as fp:
            for line in fp.readlines():
                #print "readline value :==> "+line
                if line.strip():
                    print line.strip()
                    self.detail(line)
                    
    
if __name__=="__main__":
    crawler().main()
    