#!/usr/bin/python3
import sys
import calendar
from datetime import datetime, timedelta
from tree import show_tree
from datetime import date
"""
s = '2019/12/25'
date = datetime.strptime(s, "%Y/%m/%d")
modified_date = date 

today = date.today()
d1 = today.strftime("%d")

print (int(datetime.strftime(modified_date, "%d")) - int(today.strftime("%d")), "days before christmas","\n","\n") """

def show_noel(n):
    #
    s = '2019/12/25'
    date = datetime.strptime(s, "%Y/%m/%d")
    modified_date = date 

    today = date.today()
    d1 = today.strftime("%d")

    print (int(datetime.strftime(modified_date, "%d")) - int(today.strftime("%d")), "days before christmas","\n","\n") 
#
    if len(n) > 1:
        date_time_str = n[1]
        datedata = datetime.strptime(date_time_str, '%Y-%m-%d')
        
    else:
        datedata = datetime.now()
          

    var = calendar.TextCalendar(calendar.MONDAY)
    firstCalendar = var.formatmonth(datedata.year, datedata.month, 5, 1)
    firstCalendar = firstCalendar.replace(str(datedata.day), "("+str(datedata.day)+")", 1)
    
    var = calendar.TextCalendar(calendar.MONDAY)
    next = var.formatmonth(datedata.year, 12, 5, 1)
    next = next.replace(" 25 ", "[25]", 1)

    if datedata.strftime('%Y-%m-%d') == datetime.strptime(s, "%Y/%m/%d"):
        return show_tree(10)
    else:
        return firstCalendar+next

if __name__ == "__main__":
    print(show_noel(sys.argv))
