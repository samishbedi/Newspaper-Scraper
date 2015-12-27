#extracts urls for given month and year
from url_extractor import *
import datetime, calendar
from calendar import monthrange
from datetime import date
from urllib2 import urlopen, HTTPError, URLError
from store_db import *


def extract_month(day,month,year,category):
  art_month={}
  
  x=monthrange(year,month)
  for i in range(day,(x[1]+1)):
    no=((date(year,month,i)-date(1900,1,1)).days)+2
    url = "http://timesofindia.indiatimes.com/"+str(year)+"/"+"/"+str(month)+"/"+str(i)+"/archivelist/year-"+str(year)+",month-"+str(month)+",starttime-"+ str(no) + ".cms"
    
    flag=False
    nc=0
    while not flag:
      try:
        req = urllib2.Request(url)
        resp = urllib2.urlopen(req)  
        flag=True      
      except HTTPError:
        print "bad url"
        bad_list.append(url)
        break
      except URLError:
        if nc==0:
          print "Network connection error...trying again"
          nc+=1
        continue
      
    
    if url not in bad_list:  
      print url 
      print "Extracting",category,"for", date(year,month,i).strftime("%A, %B %d, %Y")
      art_day=archive_extract(url,category)
      data_store(art_day,date(year,month,i).strftime("%d%m%Y"),category)
      

