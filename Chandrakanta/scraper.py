import re
import os
import time
import sys
import csv
import json
import itertools
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class crawler(object):
    def __init__(self):
        self.file_name = "data_new.txt"
        self.file_type = "indian_raga"        
        self.driver= webdriver.Firefox()
    
    def detail(self,args):
        self.driver.get(args)
        data=self.driver.find_elements_by_xpath("//*[@id='Content']/table/tbody/tr")
        
        for i in xrange(len(data)):
            self.__file_writer_st(args)
            details = data[i].text.split("\n")
            self.__file_writer("song_name", details[0].encode("utf-8"))
            for j in xrange(1,len(details)):
                detail = details[j].split(" - ",1)
                if len(detail)>1:
                    self.__file_writer(detail[0].encode("utf-8"), detail[1].encode("utf-8"))
        
        
    def __file_writer_st(self,data):
        f = open(self.file_name,"a")
        f.write("----------------------------------------\nFilms_"+self.file_type+":000000001:"+data+"\n")
        f.close()

    def __file_writer(self,key,value):
        f = open(self.file_name,"a")
        f.write("  extractions:"+key+"                              @ 2014/12/11-14:16:06.134909:\n    '"+value+"'\n")
        f.close()

    def main(self):
            self.url_li=[]
            self.li=[]
            self.fetch()        
    
    def fetch(self):
        with open('Links') as fp:
            for line in fp:
                print line
                self.detail(line)
                time.sleep(10)
        self.driver.quit()
    
if __name__=="__main__":
    crawler().main()