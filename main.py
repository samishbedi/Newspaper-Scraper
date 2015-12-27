from url_gen_extract_year_month import *
from store_db import *

year=raw_input("Enter the Archive's year:")
month_s=raw_input("Enter the Archive's starting month:")
month_e=raw_input("Enter the Archive's ending month:")
d_s=raw_input("Enter the Archive's starting date:")

for i in range(int(month_s),int(month_e)+1):
  month=i
  extract_data=extract_month(int(d_s),int(month),int(year),"business")
  d_s=1

connection.close()



