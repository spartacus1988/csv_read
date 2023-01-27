#! /bin/bash

python3 csv_read.py > /dev/null &

while 1>0
do
ps -A | grep python3 > /dev/null
if [ $? = "1" ]; then kill -9 $!; python3 csv_read.py > /dev/null &
fi
sleep 5
done
