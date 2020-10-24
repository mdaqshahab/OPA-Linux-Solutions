#!/bin/bash
read num
e=0
o=0
while [ "$num" -gt 0 ]
do
        read var
        rem=$(( var %2 ))
        if [ "$rem" -eq 0 ]
        then
                e=$(( e + var * var ))
        else
                o=$(( o + var * var ))
        fi
        (( num-- ))
done
r=$(( e - o))
echo $r