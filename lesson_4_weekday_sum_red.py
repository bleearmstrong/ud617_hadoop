#!/usr/bin/python
import sys

def reducer():
    total = 0
    count = 0

    weekday_total = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
    
    for line in sys.stdin:
        
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        day, sale = data
        weekday_total[day] += float(sale)
    for key in weekday_total:
        print "Sales for ", key, ": ", weekday_total[key]
    
def main():
	import StringIO
        sys.stdin = sys.__stdin__
	reducer()
	

main()
