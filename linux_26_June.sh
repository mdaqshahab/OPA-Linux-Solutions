#!/bin/bash
cat $1 > file
grep -v "^I" file |
awk 'BEGIN{FS=","}
    {
        if($5 >= 80)
        {
            print $1"|"$2"|"$3"|"$4"|"$5
        }
}' | sort -k 5 -n -t "|"