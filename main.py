import subprocess
#import psutil

cmd = 'WMIC PROCESS get Caption,Commandline,Processid'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
for line in proc.stdout:
    if line == "Discord.exe":
        print('1')
    else:
        print('0')