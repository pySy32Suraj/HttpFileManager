from __future__ import annotations
import os
import psutil
import logging

class Desktop:
    WIN = psutil.WINDOWS
    LINUX = psutil.LINUX

    def get_partitions(self) -> list[dict]:
        partitions = []

        for p in psutil.disk_partitions():
            partitions.append({
                "name": p.device,
                "mountpoint": p.mountpoint.replace("\\", "/") if self.WIN else p.mountpoint,
                "fstype": p.fstype,
                "opts": p.opts,
                "details": self.getDriveInfo(p.mountpoint)
            })
        
        if self.LINUX and len(partitions) == 0:
            partitions.append({
                "name": "/",
                "mountpoint": "/",
                "fstype": "unknown",
                "details": self.getDriveInfo("/")
            })

        return partitions
    
    def get_from_mnt(self) -> list[dict]:
        # only for linux
        partitions = []
        for i in os.listdir("/mnt/"):
                f = os.path.join("/mnt/", i)
                if os.path.ismount(f): partitions.append({
                    "name": i,
                    "mountpoint": f,
                    "fstype": "unknown",
                    "details": self.getDriveInfo(f)
                })
        return partitions


    def getDriveInfo(self, name: str) -> dict:
        try:
            hdd = psutil.disk_usage(name)
        except Exception as e:
            logging.error("RestServer -> " + e.__str__())
            return
        return {
            "used": hdd.used,
            "free": hdd.free,
            "total": hdd.total,
            "percent": hdd.percent
        }