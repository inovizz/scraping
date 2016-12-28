"""Parser for Beeradvocate website.

  Typical usage example:

  foo = Crawler()
  bar = foo.main()
"""

import re
import time

from selenium import webdriver


class Crawler(object):
  """Main class to Crawl website data.

  Attributes:
    driver: An object of selenium webdriver
    url_li: A list of URLs
  """

  def detail(self, args):
    """Contains the main logic to fetch the details from website."""

    self.driver = webdriver.Firefox()
    self.driver.get(args)
    title = self.driver.find_element_by_class_name("titleBar")
    print "title is ::", title.text
    new_data = self.driver.find_element_by_xpath("//*[@id='content']/div/div")
    url = args.strip()
    print "url is ::", url

    if new_data:
      new_data = new_data.get_attribute("innerHTML")
      new_data = new_data.replace("\n", "").replace("\t", "").replace("\r", "")

      pairings = re.findall(r"<h3>Food\sPairings</h3>\s*(.*?)\s*<a", new_data)
      pairings = "".join(pairings)
      pairings = pairings.replace("<br>", ",").strip()
      pairings = re.sub("<[^>]*>", "", pairings).strip()
      print "Pairings is ::", pairings

      abv = re.findall(r"\s*range:\s*(.*?)\s*</b", new_data)
      abv = "".join(abv)
      abv = abv.replace("<br>", ",").strip()
      # ABV=re.sub("\s*</li>\s*<li.*?>\s*",", ",abv)
      abv = re.sub("<[^>]*>", "", abv).strip()
      print "ABV is ::", abv

      glassware = re.findall(r"<h3>Glassware</h3>\s*(.*?)\s*<a", new_data)
      glassware = "".join(glassware)
      glassware = re.sub(r"<br\s/>", "", glassware)
      glassware = re.sub("<[^>]*>", "", glassware)
      print "Glassware are ::", glassware

    with open("data.csv", "ab") as fp:
      fp.write(title.text.encode("utf-8") + "\t")
      fp.write(url.encode("utf-8") + "\t")
      fp.write(pairings.encode("utf-8") + "\t")
      fp.write(abv.encode("utf-8") + "\t")
      fp.write(glassware.encode("utf-8") + "\n")

    time.sleep(3)

    self.driver.quit()

  def main(self):
    self.url_li = []
    self.fetch()

  def fetch(self):
    with open("URLs") as fp:
      for line in fp:
        if line.strip():
          self.detail(line)


if __name__ == "__main__":
  Crawler().main()
