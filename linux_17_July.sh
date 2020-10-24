#!/bin/bash
cat $1 > file
grep -v "^I" file |
awk 'BEGIN {FS=","}
    {
        if($3 == "Python" && $4 == "Oracle")
        {
            print $1"&"$2"&"$3"&"$4
        }
    }' | sort -k 2 -t "&"