#! /bin/bash
#!/bin/bash/
pkill -f csv_read.py 
python csv_read.py



#while 1>0
#do
#ps -A | grep python3 > /dev/null
#if [ $? = "1" ] 
#then python3 csv_read.py > /dev/null &
#fi
#sleep 5
#done
