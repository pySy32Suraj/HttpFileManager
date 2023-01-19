import logging
import json
import os

from typing import BinaryIO


class Profiles:
    """
    Profile Structure :-
    {
        Name: "devicename or anyname"
        Dp: "profile photo url"
        Address: "http://ip:port"
        Ip: "just ip address"
        port: "just port"
    }
    """
    PROFILE_DIR = os.path.dirname(__file__)
    PROFILE_NAME = "profiles-date"

    def __init__(self) -> None: 
        self.profiles_data = self.load()
    
    def addProfile(self, profile: dict, this: bool=False) -> bool:
        """
        this: own profile
        Returns `True` if added successful else `False`
        """
        # later need to implement : To check profile existence and then take action
        if this:
            if self.profiles_data.get("this") != None:
                logging.info("this Profile already exists, You update")
                return False
            self.profiles_data["this"] = profile
        else:
            if self.profiles_data.get(profile['Ip']) != None:
                logging.info(f"{profile['Ip']} Profile already exists, You update")
                return False

            self.profiles_data[profile["Ip"]] = profile

        self.dump(indent=0)
        return True


    def updateProfile(self, ip: str, profile: dict) -> bool:
        if self.removeProfile(ip):
            self.profiles_data[ip] = profile
            self.dump(indent=0)
        else:
            logging.info(f"{ip} is not exists.")
            return False
        return True

    def removeProfile(self, ip: str) -> bool:
        try:
            self.profiles_data.pop(ip)
        except KeyError as e:
            logging.error(e.__str__())
            return False
        else:
            self.dump(indent=0)
            return True

    def getMyProfile(self) -> dict:
        return self.profiles_data.get("this")

    def getOthersProfile(self) -> list[dict]:
        profiles = []
        for key, profile in self.profiles_data.items():
            if key != "this":
                profiles.append(profile)

        return profiles
    
    def dump(self, **kw) -> None:
        f = self.__fileObjOfProfiles("w")
        json.dump(self.profiles_data, f, **kw)
        f.close()
    
    def load(self, **kw) -> dict:
        f = self.__fileObjOfProfiles()
        obj = json.load(f, **kw)
        f.close()
        return obj

    def __fileObjOfProfiles(self, method: str = "r") -> BinaryIO:
        _type = ".json"
        pfpath = os.path.join(self.PROFILE_DIR, self.PROFILE_NAME + _type)

        if not os.path.exists(pfpath):
            with open(pfpath, "w") as f:
                # json.dump({
                #     str(self.__class__): pfpath
                # }, f, indent=4)
                json.dump(dict(), f)
        
        return open(pfpath, method)

    def __str__(self) -> str:
        return f"<{type(self).__name__} : {self.profiles_data.__str__()}>"

if __name__ == "__main__":
    p = Profiles()
    print(p.addProfile({
        "Name": "Suraj",
        "Surname": "Yadav",

    }, this=True))

    print(p)