#!/bin/bash
cat $1 > file
grep -v "^I" file |
awk -F "," '{
    avg=($3 + $4)/2;
    if($3 > 50 && $4 > 50 && avg >= 75)
    {
        print $1,$2,avg;
    }
}' | sort -k 3rn