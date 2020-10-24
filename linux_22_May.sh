#!/bin/bash
read input
char_count=$(echo $input | wc -m)
word_count=$(echo $input | wc -w)
avg=$((char_count/word_count))
echo $avg