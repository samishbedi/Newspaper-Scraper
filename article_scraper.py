#extracts attributes from articles
import newspaper
from newspaper import Article
import mechanize
from bs4 import BeautifulSoup
import re
from datetime import datetime
from dateutil import parser
import urllib2
from urllib2 import urlopen, HTTPError, URLError


article_list=[]


def art_scrape(url):
  try:
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req)           
  except HTTPError:
    return -1
  except URLError:
      print "Network connection error...try again"
      return -2
      

  article = Article(url)
  
  try:
    article.download()
    article.parse()
  except: 
    return -1
  
  

  if not article.is_parsed:
   return False
  li_date= article.publish_date
  li_date=None
  if li_date is None:
    try:
      br =  mechanize.Browser()
      br.set_handle_robots(False)
      htmltext = br.open(url).read()
      soup = BeautifulSoup(htmltext)
      for date_text in soup.findAll():
        #print str(date_text)
        match = re.search(r'(\w{3}|\w{3,})\s(\d{2}|\d),\s\d{4},\s\d{2}.\d{2}(\s\wM|\wM)', str(date_text))
        if match is None:
          continue
        else:
          date_time=str(match.group())
          date_time=date_time.replace(".",":")
          dt = parser.parse(date_time)
          #print dt
          li_date=dt
          break
    except: 
      print "No Date Found" 
      
  
  li_title=article.title
  li_body=article.text
  li_authors=article.authors
  li_images=article.images
  li_videos=article.movies
  article.nlp()
  li_summary=article.summary
  article_list=[li_date,li_title,li_body,li_authors,li_images,li_videos,li_summary]
  return article_list
 

#def art_nlp(article):
  
  
    
  
  
