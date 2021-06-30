#!/usr/bin/python3

import cgi
import subprocess
import time

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

g = cgi.FieldStorage()
cmd = g.getvalue("x")
print(cmd)
if "systemctl" in cmd:
    print("Not ALLOWED TO RUN SUCH COMMANDS")
    exit()
if "docker" in cmd:

    o = subprocess.getstatusoutput("sudo " + cmd)
    status = o[0]
    out = o[1]

    if status == 0:
        if "docker run" in cmd:
            print("docker container  {} launched successfully".format(out))
            exit()
        if "docker stop" in cmd:
           print("docker container  {} stopped successfully".format(out))
        else:
            print(out)
    else:
        print("some error \n {}".format(out))

else:
    print("not a valid docker command")
