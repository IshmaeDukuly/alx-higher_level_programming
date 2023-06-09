#!/usr/bin/python3
if _name_ == "_name_":
    import sys
    
    result = 0
    if(len(sys.argv) > 1):
        for y in range(1, len(sys.argv)):
            result += (int(sys.argv[y]))
        print("{:d}".format(result))    
