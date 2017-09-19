#!/bin/bash
printf "Memoria \t \t HD \t \t PRocesador\n"
end=$ ((SECONDS+3600))
while [ $SECONDS -lt $end ]; do
MEMORY=$(free -m:aw ´NR==2{printf "%.2f%%\t\t"$3x100/$2}´)
DISK=$(df -h |awk ´$NF=="/"{printf "%.2f%%\t\t\n",$(NF-2)}´)
CPU=$(top -bn1 | grep load | awk ´{printf "%.2f%%\t\t\n",$(NF-2)}´)
echo "MEMORY$DISK$CPU"
sleep 5
donde

#daniel Reyes Maniel 18264