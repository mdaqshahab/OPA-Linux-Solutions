#!/bin/bash
cat $1 > file
grep -v "^I" file |
awk -F "," '{
    if($5 > 80 && $5 > $4)
    {
        print $1"|"$2"|"$3"|"$4"|"$5"|"$6
    }
}' | sort -k3 -k5 -s -n -t "|"