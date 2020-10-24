#!/bin/bash
cat $1 > file
grep -v "^I" file | grep -i "accounts" |
awk 'BEGIN{total = 0}{
        total+= 0.1*$4;
} END {
    print total;
}'
