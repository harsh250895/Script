#!/bin/bash
#while loop to run script every 10 seconds
while [ 1 ]; do
	for each in { 00:00 01:00 02:00 03:00 04:00 05:00 06:00 07:00 08:00 09:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00 18:00 19:00 20:00 21:00 22:00 23:00}
	do
		d=$(date +%R)
		if [ $each = $d ]
		then
			#1: background sleeps for n seconds		
			sleep 1000s &
			
			#2: Find processes using maximum cpu and memory
			ps -eo pid,ppid,cmd,%mem --sort=-%mem | head -n 2 >> mem_cpu.log
			ps -eo pid,ppid,cmd,%mem --sort=-%cpu | head -n 2 >> mem_cpu.log
			
			#3: Print all open tcp ports sorted by state
			netstat -at |tail -n +5 | sort -k 6,6
			
			#4: Killing all sleeping process
			#Executing the below command causes the system to reboot hence commented out for debugging
			#ps h -eo s,pid | awk '{ if ($1 == "S" || $1 == "D") { print $2 } }' | xargs -r kill -9
			
			#5: Check if any process are still in sleep state and exit
			sleepCheck=$(ps -eo s | grep -o 'S\|D' -c)
			if [ $sleepCheck > 0 ]
			then
				echo Some processes are still in sleep state
				exit 1
			fi
		fi
	done
	sleep 10s
done
