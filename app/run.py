import os
import logging
import argparse
logging.basicConfig(format=f"%(asctime)s: %(message)s", level=logging.DEBUG)

from http_server import http_server
from rest_server import rest_server
from util.exc_thread import ExcThread
from util import host


parser = argparse.ArgumentParser()

parser.add_argument("-b", "--host", default=None, help="[Optional] Ip address for binding the server", type=str)
parser.add_argument("--save", action="store_true", help="Save for future use.")

args = parser.parse_args()
hostip = args.host

if args.host == None:
    ips = host.get_ex()
    if len(ips) == 1:
        hostip = ips[0]
    else:
        for i, ip in enumerate(ips):
            print(f"{i}. {ip}")
        i_ip = int(input("Select ip: "))

        if i_ip > len(ips):
            hostip = ips[-1]
        else:
            hostip = ips[i_ip]

rest_server_thread = ExcThread(target=rest_server.run,
    kwargs={
        "host": hostip,
        "keyIntHandle": False,
        "msg": False
    })
rest_server_thread.start()

if args.save:
    host.save(hostip)
    
try:
    http_server.run(
        host=hostip,
        dir=os.path.join(os.getcwd(), "web"),
        keyIntHandle=False
    )
except KeyboardInterrupt:
    print("interrupt")
    ExcThread.exit()

print("Stoped!")

