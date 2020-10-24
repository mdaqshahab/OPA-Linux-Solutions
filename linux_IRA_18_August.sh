#!/bin/bash
cat $1 > file
grep -v "^I" file |
awk 'BEGIN{FS = "\n" ; RS = "" ; OFS = "    " ; ORS = "\n"; print "Name\t\tHouse No\t\tPhone";}{
    print $1, $2, $3 ;
}'