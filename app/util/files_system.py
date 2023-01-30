import os
import time
import shutil
import logging
from http import HTTPStatus

from .headers import Headers
from .guess_type import get_type


class FilesSystem:
    COPY_BUFSIZE = 0
    
    def linux_path(self, path: str) -> str:
        if os.name == "nt":
            return path.replace("\\", "/")
        return path

    def listDir(self, path: str) -> dict:
        files = []
        folders = []

        try:
            for i in os.listdir(path):
                abs_path = self.linux_path(os.path.join(path, i))
    
                if os.path.isfile(abs_path):
                    files.append(self.getFileInfo(abs_path))
                elif os.path.isdir(abs_path):
                    f_info = self.getFolderInfo(abs_path)
                    if f_info != None: folders.append(f_info)
        except Exception as e:
            logging.error("RestServer -> " + e.__str__())
            
        return {
            "Files": files,
            "Folders": folders
        }
    
    def getFolderInfo(self, fpath: str) -> dict:
        try:
            items = len(os.listdir(fpath))
        except Exception as e:
            logging.error("RestServer -> " + e.__str__())
            return
        else:
            return {
            "Name": os.path.basename(fpath),
            "AbsolutePath": fpath,
            "Items": items
            }
    
    def getFolderReservedSpace(self, fpath: str) -> int:
        """
        Returns: in Bytes
        """
        size = 0

        for p, _, files in os.walk(fpath):
            for file in files:
                size += os.path.getsize(os.path.join(p, file))

    def getFileInfo(self, fpath: str) -> dict:
        fname = os.path.basename(fpath)
        d_index = fname.rfind(".")
        return {
            "Name": fname,
            "AbsolutePath": fpath,
            "Size": os.path.getsize(fpath),
            "LastModifiedDate": time.ctime(os.path.getmtime(fpath)),
            "Type": fname[d_index:] if d_index != -1 else None,
       }
    
def send_file(request_handler, fpath: str, download: bool=False):
        Headers(request_handler, {
            "Content-Type": "application/" + get_type(fpath).split("/")[1] if download else get_type(fpath),
            "Content-Length": os.path.getsize(fpath)
        }).send(HTTPStatus.OK).end()

        with open(fpath, "rb") as f:
            shutil.copyfileobj(f, request_handler.wfile)