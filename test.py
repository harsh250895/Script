#!/usr/bin/env python
import subprocess
import sys 
import os
from time import gmtime, strftime

#1: Background sleep for n number of seconds
def backgroundSleep(sec):
    s = str(sec)
    os.system("sleep "+s+" &")

#2: Processes using maximum cpu and memory
def max_mem_cpu():
    max_mem = os.system('ps -eo pid,ppid,cmd,%mem --sort=-%mem | head -n 2 >> mem_cpu.log') 
    max_cpu = os.system('ps -eo pid,ppid,cmd,%cpu --sort=-%cpu | head -n 2 >> mem_cpu.log')

#3: List of open tcp ports sorted by state
def tcpList():
    tcp_l = os.popen('netstat -at | tail -n +5 | sort -k 6,6')
    tcp_list = tcp_l.read()
    print(tcp_list)

#4: Kill all sleeping processes.
#p.s: created a log file to store a list of all sleeping process, killing all of them resulted in a system reboot for unexplained reasons. Hence, for debugging purposes. 
def killSleepingProc():
    CMD = "ps h -eo s,ppid,comm | awk '{ if ($1 == \"S\" || $1 == \"D\") { print $2 } }' > sleep.log"
    output = subprocess.check_output(CMD, shell=True)
#   t = output.split('\n')
#   for each in t:
#       if each.isdigit() == True:
#           print(each)
#           m = "sudo kill -9 "+each
#           os.system(m)

#5: Checing if any processes are in sleep state
def sleepCheck():
     print("Checking for sleeping processes...")
     cmd = "ps -eo s | grep -o 'S\|D' -c "
     num = os.popen(cmd)
     outp = num.read()
     if outp > 0:
        print("Some processes are still in sleep state")
        sys.exit(1)


list = ["01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00","00:00"]

#Call functions if time is on the hour every 10 seconds
while True:
    for each in list:
        t = strftime("%H:%M", gmtime())
        if each == t:
            seconds = input("Enter the number of seconds: ")
            backgroundSleep(1000)
            max_mem_cpu()
            tcpList()
            killSleepingProc()
            sleepCheck()
    os.system("sleep 10")



