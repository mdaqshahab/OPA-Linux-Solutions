#!/bin/bash
cat $1 > file
grep -v "^I" file |
awk -F "," '{
    s=$3+$4;
    if(s>99) {print $1,$2,s}
}' | sort -k 3rn | cut -d ' ' -f 1,2