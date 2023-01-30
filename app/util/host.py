from os import path
import socket

saved_path = path.join(path.dirname(__file__), "ip.dat")

def save(ip):
    older = get_from_saved()
    with open(saved_path, "w") as f:
        f.write(f"{ip}\n")
        for i in older:
            f.write(f"{i}\n")

def get_from_saved():
    if path.exists(saved_path):
        with open(saved_path, "r") as f:
            return list(map(lambda e: e.replace("\n", ""), f.readlines()))
    return []

def get_ex():
    host = socket.gethostname()
    return socket.gethostbyname_ex(host)[-1] + get_from_saved()