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
        title=self.driver.find_element_by_xpath("//*[@id='FeatureCopy']/h1")
        print "title is ::", title.text
        new_data=self.driver.find_element_by_xpath("//*[@id='Container']")
        url=args.strip()    
        print "url is ::", url
	
        if new_data:
            new_data=new_data.get_attribute("innerHTML")
            new_data=new_data.replace("\n","").replace("\t","").replace("\r","")
            print type(new_data)
            '''
            Company=re.findall(r"Company:.*?</b>(.*?)</p", new_data)
            Company="".join(Company)
            Company=Company.strip()
            Company=Company.replace("<br>",",").strip()
            Company=re.sub("\s*</li>\s*<li.*?>\s*",", ",Company)
            Company=re.sub("<[^>]*>","",Company).strip()
            print "Company is ::", Company
           
            Cheesemaker=re.findall(r"Cheesemaker:.*?</b>(.*?)</p", new_data)
            Cheesemaker="".join(Cheesemaker)
            Cheesemaker=Cheesemaker.strip()
            Cheesemaker=Cheesemaker.replace("<br>",",").strip()
            Cheesemaker=re.sub("\s*</li>\s*<li.*?>\s*",", ",Cheesemaker)
            Cheesemaker=re.sub("<[^>]*>","",Cheesemaker).strip()
            print "Cheesemaker is ::", Cheesemaker

            Proprietor=re.findall(r"Proprietor:.*?</b>(.*?)</p", new_data)
            Proprietor="".join(Proprietor)
            Proprietor=Proprietor.strip()
            Proprietor=Proprietor.replace("<br>",",").strip()
            Proprietor=re.sub("\s*</li>\s*<li.*?>\s*",", ",Proprietor)
            Proprietor=re.sub("<[^>]*>","",Proprietor).strip()
            print "Proprietor is ::", Proprietor

            Affineur=re.findall(r"Affineur:.*?</b>(.*?)</p", new_data)
            Affineur="".join(Affineur)
            Affineur=Affineur.strip()
            Affineur=Affineur.replace("<br>",",").strip()
            Affineur=re.sub("\s*</li>\s*<li.*?>\s*",", ",Affineur)
            Affineur=re.sub("<[^>]*>","",Affineur).strip()
            print "Affineur is ::", Affineur

            City_State=re.findall(r"City,\sState:.*?</b>(.*?)</p", new_data)
            City_State="".join(City_State)
            City_State=City_State.strip()
            City_State=City_State.replace("<br>",",").strip()
            City_State=re.sub("\s*</li>\s*<li.*?>\s*",", ",City_State)
            City_State=re.sub("<[^>]*>","",City_State).strip()
            print "City_State is ::", City_State

            Region=re.findall(r"Region:.*?</b>(.*?)</p", new_data)
            Region="".join(Region)
            Region=Region.strip()
            Region=Region.replace("<br>",",").strip()
            Region=re.sub("\s*</li>\s*<li.*?>\s*",", ",Region)
            Region=re.sub("<[^>]*>","",Region).strip()
            print "Region is ::", Region

            Country=re.findall(r"Country:.*?</b>(.*?)</p", new_data)
            Country="".join(Country)
            Country=Country.strip()
            Country=Country.replace("<br>",",").strip()
            Country=re.sub("\s*</li>\s*<li.*?>\s*",", ",Country)
            Country=re.sub("<[^>]*>","",Country).strip()
            print "Country is ::", Country

            Milk_type=re.findall(r"Milk\sType:.*?</b>(.*?)</p", new_data)
            Milk_type="".join(Milk_type)
            Milk_type=Milk_type.strip()
            Milk_type=Milk_type.replace("<br>",",").strip()
            Milk_type=re.sub("\s*</li>\s*<li.*?>\s*",", ",Milk_type)
            Milk_type=re.sub("<[^>]*>","",Milk_type).strip()
            print "Milk_type is ::", Milk_type

            '''
            Milk_treatment=re.findall(r"Milk\sTreatment:.*?</b>(.*?)</p", new_data)
            Milk_treatment="".join(Milk_treatment)
            Milk_treatment=Milk_treatment.strip()
            Milk_treatment=Milk_treatment.replace("<br>",",").strip()
            Milk_treatment=re.sub("\s*</li>\s*<li.*?>\s*",", ",Milk_treatment)
            Milk_treatment=re.sub("<[^>]*>","",Milk_treatment).strip()
            print "Milk_treatment is ::", Milk_treatment
            '''

            Rennet=re.findall(r"Rennet:.*?</b>(.*?)</p", new_data)
            Rennet="".join(Rennet)
            Rennet=Rennet.strip()
            Rennet=Rennet.replace("<br>",",").strip()
            Rennet=re.sub("\s*</li>\s*<li.*?>\s*",", ",Rennet)
            Rennet=re.sub("<[^>]*>","",Rennet).strip()
            print "Rennet is ::", Rennet

            Rind=re.findall(r"Rind:.*?</b>(.*?)</p", new_data)
            Rind="".join(Rind)
            Rind=Rind.strip()
            Rind=Rind.replace("<br>",",").strip()
            Rind=re.sub("\s*</li>\s*<li.*?>\s*",", ",Rind)
            Rind=re.sub("<[^>]*>","",Rind).strip()
            print "Rind is ::", Rind

            Texture=re.findall(r"Texture:.*?</b>(.*?)</p", new_data)
            Texture="".join(Texture)
            Texture=Texture.strip()
            Texture=Texture.replace("<br>",",").strip()
            Texture=re.sub("\s*</li>\s*<li.*?>\s*",", ",Texture)
            Texture=re.sub("<[^>]*>","",Texture).strip()
            print "Texture is ::", Texture

            Aging=re.findall(r"Aging:.*?</b>(.*?)</p", new_data)
            Aging="".join(Aging)
            Aging=Aging.strip()
            Aging=Aging.replace("<br>",",").strip()
            Aging=re.sub("\s*</li>\s*<li.*?>\s*",", ",Aging)
            Aging=re.sub("<[^>]*>","",Aging).strip()
            print "Aging is ::", Aging

            Size=re.findall(r"Size[(]s[)]:.*?</b>(.*?)</p", new_data)
            Size="".join(Size)
            Size=Size.strip()
            Size=Size.replace("<br>",",").strip()
            Size=re.sub("\s*</li>\s*<li.*?>\s*",", ",Size)
            Size=re.sub("<[^>]*>","",Size).strip()
            print "Size is ::", Size

            Description=re.findall(r"</h1>(.*?)Farm\s/\sCompany", new_data)
            Description="".join(Description)
            Description=Description.strip()
            Description=Description.replace("<br>",",").strip()
            Description=re.sub("\s*</li>\s*<li.*?>\s*",", ",Description)
            Description=re.sub("<[^>]*>","",Description).strip()
            print "Description is ::", Description
            '''

        with open("Milk1.csv","ab") as fp:
            try:
              fp.write(title.text.encode('utf-8')+'\t')
              fp.write(url.encode('utf-8')+'\t')
              '''
              fp.write(Company.encode('utf-8')+'\t')
              fp.write(Cheesemaker.encode('utf-8')+'\t')
              fp.write(Proprietor.encode('utf-8')+'\t')
              fp.write(Affineur.encode('utf-8')+'\t')
              fp.write(City_State.encode('utf-8')+'\t')
              fp.write(Region.encode('utf-8')+'\t')
              fp.write(Country.encode('utf-8')+'\t')
              fp.write(Milk_type.encode('utf-8')+'\t')
              '''
              fp.write(Milk_treatment.encode('utf-8')+'\n')
              '''
              fp.write(Rennet.encode('utf-8')+'\t')
              fp.write(Rind.encode('utf-8')+'\t')
              fp.write(Texture.encode('utf-8')+'\t')
              fp.write(Aging.encode('utf-8')+'\t')
              fp.write(Size.encode('utf-8')+'\t')
              fp.write(Description.encode('utf-8')+'\n')
              '''
            except:
              print url
            
            
        #time.sleep(3)
        
        self.driver.quit()      
     
    def main(self):
        self.url_li=[]
        self.li=[]
        self.fetch()
                
    def fetch(self):
        with open('URL') as fp:
            for line in fp.readlines():
                if line.strip():
                    self.detail(line)
                    
    
if __name__=="__main__":
    crawler().main()
