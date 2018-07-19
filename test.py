#!/usr/bin/env python
import sys 
import os
from time import gmtime, strftime

def backgroundSleep(sec):
    s = str(sec)
    os.system("sleep "+s+" &")

def max_mem_cpu():
    max_mem = os.system('ps -eo pid,ppid,cmd,%mem --sort=-%mem | head -n 2 >> mem_cpu.log') 
    max_cpu = os.system('ps -eo pid,ppid,cmd,%cpu --sort=-%cpu | head -n 2 >> mem_cpu.log')

def tcpList():
    tcp_l = os.popen('netstat -at | tail -n +5 | sort -k 6,6')
    tcp_list = tcp_l.read()
    print(tcp_list)

def sleepCheck():
     print("Checking for sleeping processes...")
     cmd = "ps -e -o s | grep -o 'S\|D' -c "
     num = os.popen(cmd)
     outp = num.read()
     if outp > 0:
        print("Some processes are still in sleep state")
        sys.exit(1)

t = strftime("%H:%M", gmtime())
list = ["01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00","24:00"]

for each in list:
    if each == t:
        seconds = input("Enter the number of seconds: ")
        backgroundSleep(seconds)
        max_mem_cpu()
        tcpList()
        sleepCheck()



