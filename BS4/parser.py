import re
import os
import time
import sys
import csv
from bs4 import BeautifulSoup

class crawler(object):
    def detail(self,args):
        self.soup = BeautifulSoup(args)
        print type(self.soup.prettify())
        x=  self.soup.prettify()
        print dir(x)
        x=x.decode('iso-8859-1').encode('utf8')
        title=self.soup.find_all(re.compile('<\/div.*<h1.*>(.*?)<\/h1'))
        print dir(title)
        print title

        with open("data.csv","ab") as fp:
            fp.write(str(title) +'\t')             
     
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