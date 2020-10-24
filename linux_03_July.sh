#!/bin/bash
cat $1 > file
grep -v "^I" file |
awk 'BEGIN{FS=","}
    {
        profit = $4 - $5;
        if(profit>0)
        {
            print $1"|"$2"|"$3"|"$4"|"$5"|"profit
        }
    }' | sort -k 6rn -t "|"