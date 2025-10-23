import subprocess
subprocess.call("free -m | grep Mem | awk {'print $3'} > file1", shell=True)
file = open('file1','r')
memory = int(file.read())

if memory >= 100 and memory <= 200:
    subprocess.call("docker service scale webserver=2", shell=True)
elif memory >= 400 and memory <= 600:
    subprocess.call("docker service scale webserver=4", shell=True)
else:
    subprocess.call("docker service scale webserver=6", shell=True)
~
