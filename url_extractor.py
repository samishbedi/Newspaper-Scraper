#Extracts archives of a given url

import mechanize
from bs4 import BeautifulSoup
import newspaper
from newspaper import Article
import sys
reload(sys)  
sys.setdefaultencoding('UTF8')
import lxml
from newspaper import parsers
import lxml.etree
import lxml.html
import lxml.html.clean
from article_scraper import *


bad_list=[]
def archive_extract(url,category):
  #print url
  archive_day=[]
  br =  mechanize.Browser()
  br.set_handle_robots(False)
  

  htmltext = br.open(url).read()

  soup = BeautifulSoup(htmltext)
  numt=0
  num1=0
  num2=0
  
  #j=0
  for tag in soup.findAll('td', attrs={"width":"49%"}):
    #print tag
    num1=len(tag.findAll('a'))
    num2=len(soup.findAll('td', attrs={"width":"49%"}))  
    
    #if j>3:
      #break
    
    for link in tag.findAll('a'):
      #j+=1
      #print j
      art_link=link.get('href') 
      numt+=1
      try:
        srt_art_link=art_link.split("//")
        srt_art_link=(srt_art_link[2].split("/"))[0]
      except:
        continue
      if category != str(srt_art_link):
        continue
      
      print art_link
      

      flag=False
      i=0
      
      while not flag and i<8:
        artic=art_scrape(art_link)
        if artic==-1:
          bad_list.append(art_link)
          break
        if artic==-2:
          i+=1
          continue
        if not artic:
          i+=1
          if i==8:
            bad_list.append(art_link)
          continue
        flag=True
        #i+=1
        archive_day.append(artic)   
        size_str="Articles extracted: "+(str(numt*100.0/(num1*num2)))[0:4]+"%"
        sys.stdout.write('%s\r' % size_str)
        sys.stdout.flush()
      #if j>3:
        #break
  return archive_day

  
    
