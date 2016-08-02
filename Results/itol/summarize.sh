#!/bin/bash

l="00 05 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95"

for e in $l
do
for f in *_09${e}/*/${1}.txt
do 
sed -n "2,$"p $f >> ${1}_${e}
done
done
