import os
import time
import logging




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
                    folders.append(self.getFolderInfo(abs_path))
        except Exception as e:
            logging.error(e.__str__())
            
        return {
            "Files": files,
            "Folders": folders
        }
    
    def getFolderInfo(self, fpath: str) -> dict:
        try:
            items = len(os.listdir(fpath))
        except Exception as e:
            logging.error(e.__str__())
            items = None

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
    
    

if __name__ == "__main__":
    f = FilesSystem()
    
    for key, item in f.listDir(f.getDrives()[1]).items():
        print(key, ": ")
        for i in item:
            print(i)