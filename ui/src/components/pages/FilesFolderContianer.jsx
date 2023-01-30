import React from "react";

import FileView from "../view/FileView";
import FolderView from "../view/FolderView";

const FilesFolderContianer = ({
  path,
  files,
  folders,
  fileOnClick,
  folderOnClick,
}) => {
  if (path === null) {
    return;
  }
  if (files === null) {
    return <h1>Loading...</h1>;
  }

  return (

    <div className=" w-full h-full overflow-y-auto scroller-visible">
      <div className="flex flex-wrap justify-start items-start">
        {folders.map((v, i) => (
          <FolderView folder={v} onClick={folderOnClick} key={`key-${i}`} />
        ))}
        {files.map((v, i) => (
          <FileView file={v} onClick={fileOnClick} key={`key-${i}`} />
        ))}
      </div>
    </div>
  );
};

export default FilesFolderContianer;
