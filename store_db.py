import pymongo
from pymongo import MongoClient
import datetime, calendar
from calendar import monthrange
from datetime import date
from url_extractor import *
from newspaper import nlp

connection = MongoClient()
db=connection.articles.artic_db  
def data_store(articles,date_st,category): 
  print "Storing..." 
  for a in articles:
    try:
      if a[0] is not None:
        a_record={"date_string":a[0].strftime("%d%m%Y"),"date":a[0],"title":a[1],"body":a[2],"authors":a[3],"images":a[4],"videos":a[5],"category":str(category),"summary":a[6],"keywords":nlp.keywords(a[6])}
        db.insert(a_record)
      else:
        a_record={"date_string":date_st,"date":a[0],"title":a[1],"body":a[2],"authors":a[3],"images":a[4],"videos":a[5],"category":str(category),"summary":a[6],"keywords":nlp.keywords(a[6])}
        db.insert(a_record)
    except:
      print "Record not stored"
      bad_list.append(a)
      continue

  return db

def delete_db():
  db.remove()
