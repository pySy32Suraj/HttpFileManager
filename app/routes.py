import json
import os
from http import HTTPStatus

from rest_request_handler.rest_request_handler import RestRequestHandler
from util.files_system import FilesSystem
from util.termux import Termux
from util.headers import Headers

if not Termux.is_termux():
    from util.desktop import Desktop
    desktop = Desktop()
else:
    termux = Termux()

fs = FilesSystem()


@RestRequestHandler.get("/")
def home(cls: RestRequestHandler):
    Headers(cls, {
        "Content-Type": "text/html"
    }).send(HTTPStatus.OK).end()

    return "<h1>Welcome to Rest Request Handler Server.</h1>"

@RestRequestHandler.get("/get_drives")
def get_dirives(cls: RestRequestHandler):
    Headers(cls, {
        "Content-Type": "application/json"
    }).send(HTTPStatus.OK).end()

    if Termux.is_termux():
        drives = termux.get_storage()
    else:
        drives = desktop.get_partitions()
        if Desktop.LINUX:
            for d in desktop.get_from_mnt():
                drives.append(d)

    return json.dumps(drives)

@RestRequestHandler.get("/list_dir?path")
def list_dir(cls: RestRequestHandler, path: str):
    if not os.path.isdir(path):
        raise Exception("This path is not exists or might be is a file.", path)
    
    Headers(cls, {
        "Content-Type": "application/json"
    }).send(HTTPStatus.OK).end()
    
    return json.dumps(fs.listDir(path))

@RestRequestHandler.get("/get_file_details?path")
def get_file_details(cls, path):
    if not os.path.isfile(path):
        raise Exception("This path is not exists or might be is a folder.", path)
    
    Headers(cls, {
        "Content-Type": "application/json"
    }).send(HTTPStatus.OK).end()

    return json.dumps(fs.getFileInfo(path))


@RestRequestHandler.get("/get_folder_details?path")
def get_folder_details(cls, path):
    if not os.path.isdir(path):
        raise Exception("This path is not exists or might be is a file.", path)
    
    Headers(cls, {
        "Content-Type": "application/json"
    }).send(HTTPStatus.OK).end()

    return json.dumps(fs.getFolderInfo(path))

@RestRequestHandler.get("/get_file?path&bool: open")
def get_file(cls: RestRequestHandler, path, open=True):
    if not os.path.isfile(path):
        raise Exception("This path is not exists or might be is a folder.", path)

    cls.send_file(path)

@RestRequestHandler.get("/end_points")
def get_end_points(cls: RestRequestHandler):
    Headers(cls, {
        "Content-Type": "application/json"
    }).send(HTTPStatus.OK).end()

    return json.dumps({"end_points": list(RestRequestHandler.get_PathMap.keys())})
