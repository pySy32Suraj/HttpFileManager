import React from "react";

import DownloadIcon from "../../res/icons/download.png";
import { getFileIcon } from "../../util";

const FileView = ({ file, onClick }) => {
  // console.log(file.Type)
  const url = `http://${document.location.host}/${encodeURIComponent(file.AbsolutePath)}`; 
  // const url = `http://${document.location.hostname}:8080/${file.AbsolutePath}`; //testing
  return (
    <div className="hover:bg-gray-200 dark:hover:bg-gray-900">
      <a className="relative inline-block left-1 top-6 z-10" target="_black" href={url + "?download=true"} download={file.Name}>
        <img width="15" src={DownloadIcon} alt="" />
      </a>
      <div
        className="w-20 rounded  flex justify-center items-center flex-col"
        onClick={(e) => onClick(file.AbsolutePath)}
      > 
        <div className="px-1 pt-2 w-10">
          <img src={getFileIcon(file.Type)} alt="fileIcon" />
        </div>
        <span
          className={`fg-light-secondary dark:fg-dark-secondary w-full px-2 text-xs text-center break-words`}
        >
          {file.Name.length <= 20
            ? file.Name
            : file.Name.substring(0, 19) + "..."}
        </span>
      </div>
    </div>
  );
};
//

export default FileView;
