"""Parser for Winne the pooh wikia website.

Typical usage example:

foo = Crawler()
bar = foo.main()

"""

import re
import os
import time
import sys
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class crawler(object):

    """Main class to Crawl website data.

    Attributes:
      driver: An object of selenium webdriver
      url_li: A list of URLs

    """

    def detail(self, args):
        """Contains the main logic to fetch the details from website."""
        self.driver = webdriver.Firefox()
        self.driver.get(args)
        title = self.driver.find_elementsWikia_by_xpath(
            "//*[@id='WikiaPageHeader']/h1")
        new_data = self.driver.find_element_by_xpath(
            "//*[@id='WikiaMainContent']")
        url = args.strip()
        print 'url is ::', url

        if new_data:
            new_data = new_data.get_attribute('innerHTML')
            new_data = new_data.replace('\n', '').replace(
                '\t', '').replace('\r', '')
            Feature_films = re.findall(
                r"<b>Feature\sfilms</b>(.*?)</tr", new_data)
            Feature_films = ''.join(Feature_films)
            Feature_films = re.sub('<br>', ', ', Feature_films)
            Feature_films = re.sub('<[^>]*>', '', Feature_films)
            print 'Feature_films is ::', Feature_films

            Television_programs = re.findall(
                r"<b>Television\sprograms</b>(.*?)</tr", new_data)
            Television_programs = ''.join(Television_programs)
            # Television_programs=Television_programs.replace("<br>",",").strip()
            Television_programs = re.sub('<br>', ', ', Television_programs)
            Television_programs = re.sub(
                '<[^>]*>', '', Television_programs)
            print 'Television_programs is ::', Television_programs

            Video_games = re.findall(
                r"<b>Video\sgames</b>(.*?)</tr", new_data)
            Video_games = ''.join(Video_games)
            # Video_games=Video_games.replace("<br>",",").strip()
            Video_games = re.sub('<br>', ', ', Video_games)
            Video_games = re.sub('<[^>]*>', '', Video_games)
            print 'Video_games is ::', Video_games

            Park_attractions = re.findall(
                r"<b>Park\sattractions</b>(.*?)</tr", new_data)
            Park_attractions = ''.join(Park_attractions)
            # Video_games=Video_games.replace("<br>",",").strip()
            Park_attractions = re.sub('<br>', ', ', Park_attractions)
            Park_attractions = re.sub('<[^>]*>', '', Park_attractions)
            print 'Park_attractions is ::', Park_attractions

            Animators = re.findall(r"<b>Animators</b>(.*?)</tr", new_data)
            Animators = ''.join(Animators)
            Animators = Animators.replace('<br>', ',').strip()
            Animators = re.sub('<[^>]*>', '', Animators)
            print 'Animators is ::', Animators

            Voice = re.findall(r"<b>Voice</b>(.*?)</tr", new_data)
            Voice = ''.join(Voice)
            Voice = Voice.replace('<br>', ',').strip()
            Voice = re.sub('<[^>]*>', '', Voice)
            print 'Voice is ::', Voice

            Inspiration = re.findall(
                r"<b>Inspiration</b>(.*?)</tr", new_data)
            Inspiration = ''.join(Inspiration)
            Inspiration = Inspiration.replace('<br>', ',').strip()
            Inspiration = re.sub('<[^>]*>', '', Inspiration)
            print 'Inspiration is ::', Inspiration

            Honors_awards = re.findall(
                r"<b>Honors\sand\sawards</b>(.*?)</tr", new_data)
            Honors_awards = ''.join(Honors_awards)
            Honors_awards = Honors_awards.replace('<br>', '').strip()
            Honors_awards = re.sub('<[^>]*>', '', Honors_awards)
            print 'Honors_awards are ::', Honors_awards

            Full_name = re.findall(r"<b>Full\sname</b>(.*?)</tr", new_data)
            Full_name = ''.join(Full_name)
            Full_name = Full_name.replace('<br>', ',').strip()
            Full_name = re.sub('<[^>]*>', '', Full_name)
            print 'Full_name is ::', Full_name

            Other_names = re.findall(
                r"<b>Other\snames</b>(.*?)</tr", new_data)
            Other_names = ''.join(Other_names)
            Other_names = Other_names.replace('<br>', ',').strip()
            Other_names = re.sub('<[^>]*>', '', Other_names)
            print 'Other_names are ::', Other_names

            Personality = re.findall(
                r"<b>Personality</b>(.*?)</tr", new_data)
            Personality = ''.join(Personality)
            Personality = Personality.replace('<br>', ',').strip()
            Personality = re.sub('<[^>]*>', '', Personality)
            print 'Personality is ::', Personality

            Appearances = re.findall(
                r"<b>Appearance</b>(.*?)</tr", new_data)
            Appearances = ''.join(Appearances)
            Appearances = Appearances.replace('<br>', ',').strip()
            Appearances = re.sub('<[^>]*>', '', Appearances)
            print 'Appearances are ::', Appearances

            Birthday = re.findall(r"<b>Birthday</b>(.*?)</tr", new_data)
            Birthday = ''.join(Birthday)
            Birthday = Birthday.replace('<br>', ',').strip()
            Birthday = re.sub('<[^>]*>', '', Birthday)
            print 'Birthday is ::', Birthday

            Occupation = re.findall(
                r"<b>Occupation</b>(.*?)</tr", new_data)
            Occupation = ''.join(Occupation)
            Occupation = Occupation.replace('<br>', ',').strip()
            Occupation = re.sub('<[^>]*>', '', Occupation)
            print 'Occupation is ::', Occupation

            Allignment = re.findall(r"<b>Alignment</b>(.*?)</tr", new_data)
            Allignment = ''.join(Allignment)
            Allignment = Allignment.replace('<br>', ',').strip()
            Allignment = re.sub('<[^>]*>', '', Allignment)
            print 'Allignment is ::', Allignment

            Goal = re.findall(r"<b>Goal</b>(.*?)</tr", new_data)
            Goal = ''.join(Goal)
            Goal = Goal.replace('<br>', ',').strip()
            Goal = re.sub('<[^>]*>', '', Goal)
            print 'Goal is ::', Goal

            Home = re.findall(r"<b>Home</b>(.*?)</tr", new_data)
            Home = ''.join(Home)
            Home = Home.replace('<br>', ',').strip()
            Home = re.sub('<[^>]*>', '', Home)
            print 'Home is ::', Home

            Relatives = re.findall(r"<b>Relatives</b>(.*?)</tr", new_data)
            Relatives = ''.join(Relatives)
            Relatives = Relatives.replace('<br>', ',').strip()
            Relatives = re.sub('<[^>]*>', '', Relatives)
            print 'Relatives is ::', Relatives

            Allies = re.findall(r"<b>Allies</b>(.*?)</tr", new_data)
            Allies = ''.join(Allies)
            Allies = Allies.replace('<br>', ',').strip()
            Allies = re.sub('<[^>]*>', '', Allies)
            print 'Allies is ::', Allies

            Enemies = re.findall(r"<b>Enemies</b>(.*?)</tr", new_data)
            Enemies = ''.join(Enemies)
            Enemies = Enemies.replace('<br>', ',').strip()
            Enemies = re.sub('<[^>]*>', '', Enemies)
            print 'Enemies is ::', Enemies

            Likes = re.findall(r"<b>Likes</b>(.*?)</tr", new_data)
            Likes = ''.join(Likes)
            Likes = Likes.replace('<br>', ',').strip()
            Likes = re.sub('<[^>]*>', '', Likes)
            print 'Likes is ::', Likes

            Dislikes = re.findall(r"<b>Dislikes</b>(.*?)</tr", new_data)
            Dislikes = ''.join(Dislikes)
            Dislikes = Dislikes.replace('<br>', ',').strip()
            Dislikes = re.sub('<[^>]*>', '', Dislikes)
            print 'Dislikes is ::', Dislikes

            Powers = re.findall(
                r"<b>Powers\sand\sabilities</b>(.*?)</tr", new_data)
            Powers = ''.join(Powers)
            Powers = Powers.replace('<br>', ',').strip()
            Powers = re.sub('<[^>]*>', '', Powers)
            print 'Powers is ::', Powers

            Quote = re.findall(r"<b>Quote</b>(.*?)</tr", new_data)
            Quote = ''.join(Quote)
            Quote = Quote.replace('<br>', ',').strip()
            Quote = re.sub('<[^>]*>', '', Quote)
            print 'Quote is ::', Quote

        if title:
            title_main = title[0].get_attribute(
                'textContent').replace('\n', '\t').strip()
            title_main = ''.join(title_main)
            print 'title is::', title_main
        else:
            title_main = ''.join(title)
            print 'text is ::', title_main

        with open('data_new.csv', 'ab') as fp:
            fp.write(title_main.encode('utf-8') + '\t')
            fp.write(url.encode('utf-8') + '\t')
            fp.write(Feature_films.encode('utf-8') + '\t')
            fp.write(Television_programs.encode('utf-8') + '\t')
            fp.write(Video_games.encode('utf-8') + '\t')
            fp.write(Park_attractions.encode('utf-8') + '\t')
            fp.write(Animators.encode('utf-8') + '\t')
            fp.write(Voice.encode('utf-8') + '\t')
            fp.write(Inspiration.encode('utf-8') + '\t')
            fp.write(Honors_awards.encode('utf-8') + '\t')
            fp.write(Full_name.encode('utf-8') + '\t')
            fp.write(Other_names.encode('utf-8') + '\t')
            fp.write(Appearances.encode('utf-8') + '\t')
            fp.write(Birthday.encode('utf-8') + '\t')
            fp.write(Occupation.encode('utf-8') + '\t')
            fp.write(Allignment.encode('utf-8') + '\t')
            fp.write(Personality.encode('utf-8') + '\t')
            fp.write(Goal.encode('utf-8') + '\t')
            fp.write(Home.encode('utf-8') + '\t')
            fp.write(Relatives.encode('utf-8') + '\t')
            fp.write(Allies.encode('utf-8') + '\t')
            fp.write(Enemies.encode('utf-8') + '\t')
            fp.write(Likes.encode('utf-8') + '\t')
            fp.write(Dislikes.encode('utf-8') + '\t')
            fp.write(Powers.encode('utf-8') + '\t')
            fp.write(Quote.encode('utf-8') + '\n')

        time.sleep(3)

        self.driver.quit()

    def main(self):
        self.url_li = []
        # self.li=[]
        self.fetch()

    def fetch(self):
        with open('Links') as fp:
            for line in fp:
                print line
                self.detail(line)

if __name__ == '__main__':
    crawler().main()
