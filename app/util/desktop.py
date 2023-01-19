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
                "device": p.device,
                "mountpoint": p.mountpoint.replace("\\", "/") if self.WIN else p.mountpoint,
                "fstype": p.fstype,
                "opts": p.opts
            })
        return partitions
    
    def get_from_mnt(self) -> list[dict]:
        # only for linux
        partitions = []
        for i in os.listdir("/mnt/"):
                f = os.path.join("/mnt/", i)
                if os.path.ismount(f): partitions.append({
                    "device": i,
                    "mountpoint": f
                })
        return partitions


    def getDriveInfo(self, name: str) -> dict:
        try:
            hdd = psutil.disk_usage(name)
        except Exception as e:
            logging.error(e.__str__())
            return
        return {
            "Drive": os.path.basename(name),
            "Used": hdd.used,
            "Free": hdd.free,
            "Total": hdd.total,
            "Percent": hdd.percent
        }