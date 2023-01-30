import React, { useEffect, useState } from "react";

import { getDrives, getDirList, PathStack, connectionError } from "./util";
import { Home, Header, FilesFolderContianer } from "./components";

const pathStack = new PathStack();
pathStack.push(null);

let mountpoint = null;

const App = () => {
  const [connected, setConnectionStatus] = useState(false);
  const [path, setPath] = useState(null);
  const [devices, setDevices] = useState(null);
  const [files, setFiles] = useState(null);
  const [folders, setFolders] = useState(null);

  const [loaderState, setLoaderState] = useState("");

  let [refresh, makeRefresh] = useState(false);

  const fetch_devices = () => {
    if (path === null) {
      setLoaderState("loading");
      setDevices([]); // without it, it will gone in loop
      getDrives()
        .then(({ data }) => {
          let d = data.filter((v) => v.fstype !== "");
          setDevices(d);
          setConnectionStatus(true);
        })
        .catch((re) => {
          connectionError(re, setConnectionStatus);
        })
        .finally(() => setLoaderState(""));
    }
  };

  if (devices === null) {
    fetch_devices();
  }

  useEffect(() => fetch_devices(), [refresh]);

  useEffect(() => {
    setFiles([]);
    setFolders([]);

    if (path !== null) {
      setLoaderState("loading");

      getDirList(encodeURIComponent(path))
        .then(({ data }) => {
          setFiles(data.Files);
          setFolders(data.Folders);
          setConnectionStatus(true);
        })
        .catch((re) => {
          connectionError(re, setConnectionStatus);
        })
        .finally(() => setLoaderState(""));
    }
  }, [path, refresh]);

  const file_callback = (path) => {
    path = encodeURIComponent(path);
    window.open(`http://${document.location.host}/${path}`, "_blank");
  };
  const folder_callback = (path) => {
    if (!path.endsWith("/")) pathStack.pushAndSet(path + "/", setPath);
    else pathStack.pushAndSet(path, setPath);
  };

  return (
    <div className=" bg-light-primary dark:bg-dark-primary h-full w-full">
      <Header
        connectionStatus={connected}
        path={path}
        pathStack={pathStack}
        pathSetter={setPath}
        loaderState={loaderState}
        setLoaderState={setLoaderState}
        onLoaderClick={() => {
          makeRefresh(!refresh);
        }}
        onButtonsClick={{
          next: () => {
            setPath(pathStack.getPathNext());
          },
          privous: () => {
            setPath(pathStack.getPathPrivous());
          },

          back: () => {
            if (path !== null) {
              if (path === mountpoint) {
                pathStack.pushAndSet(null, setPath);
                mountpoint = null;
              } else {
                let s = path.split("/");
                s.splice(-2);
                pathStack.pushAndSet(s.join("/") + "/", setPath);
              }
            }
          },
        }}
      />

      <div className="mt-6 p-3 h-full">
        <Home
          path={path}
          devices={devices}
          onDeviceClick={(mp) => {
            if (!mp.endsWith("/")) mp += "/";
            pathStack.pushAndSet(mp, setPath);
            mountpoint = mp;
          }}
        />

        <FilesFolderContianer
          path={path}
          files={files}
          folders={folders}
          fileOnClick={file_callback}
          folderOnClick={folder_callback}
        />
      </div>
    </div>
  );
};

export default App;
