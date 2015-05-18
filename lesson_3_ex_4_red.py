#!/usr/bin/python
import sys
def reducer():
    hit_count = 0
 
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 1:
            continue
        if data[0] == "/assets/js/the-associates.js":
            hit_count += 1
 
    print "Total hits to /assets/js/the-associates.js: ", hit_count

def main():
	import StringIO
        sys.stdin = sys.__stdin__
	reducer()
	

main()
