import os


class Termux:

    
    def __init__(self) -> None:
        pass

    @staticmethod
    def is_termux() -> bool:
        if os.name == "posix" and "com.termux" in os.getcwd().split("/"):
            return True
        return False
    
    @property
    def home(self) -> str | None:
        p = "/data/data/com.termux/files/home/"
        if os.path.exists(p):
            return p
    
    @property
    def sdcard(self) -> str | None:
        p = "/sdcard/"
        if os.path.exists(p):
            return p
    
    def get_storage(self) -> list[dict]:
        return [{
            "Name": "Internal Storage",
            "Path": self.sdcard
        },
        {
            "Name": "Termux Home",
            "Path": self.home
        }]