import React, { useState } from 'react';


const FileView = ({fileName, fileIconUrl}) => {
  let [showFilename, setFilenameState] = useState(false);
  // console.log(showFilename)
  return (
<div>
    <div className="w-20 rounded hover:bg-gray-200 dark:hover:bg-gray-900 flex justify-center items-center flex-col sticky" >

      <div className="px-1 pt-2 w-10">
      {/* // showing full file name on hover now I'm leaving as disabled
        // onMouseEnter={e => setFilenameState(true)}
        // onMouseLeave={e => setFilenameState(false)} */}
          <img src={fileIconUrl} alt="fileIcon"/>
      </div>
      <span className={`${showFilename ? "hidden": "block"} text-slate-500 dark:text-slate-400 w-full px-2 text-sm text-center overflow-x-clip text-ellipsis `}>{fileName}</span>
      
    </div>
    {/* // also this */}
    {/* <span className={`${showFilename ? "block": "hidden"} text-slate-500 dark:text-slate-400 w-full px-2 text-sm text-center bg-gray-200 dark:bg-gray-900 filename-shower`}>{fileName}</span> */}
  </div>
  )
}
// 

export default FileView;