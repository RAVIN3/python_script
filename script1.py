import subprocess
subprocess.call("docker  network create --driver bridge intelliqit",shell=True)
subprocess.call("docker run --name mydb -d -e MYSQL_ROOT_PASSWORD=ravin1234 --network intelliqit mysql", shell=True)
subprocess.call("docker run --name mywordpress -d -p 8888:80 --network intelliqit wordpress", shell=True)
