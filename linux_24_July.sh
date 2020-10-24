#!/bin/bash
cat $1 > file
grep -v "^I" file |
awk 'BEGIN{FS=","}{
    if($4 < 60)
    {
        array[$1]+=1;
    }
} END {
    for(ind in array)
    {
        if(array[ind] == 1)
        {
            print ind;
        }
    }
}'