import React from 'react';

const FileView = ({fileName, fileIconUrl}) => {
  return (
    
    <div className="w-20 rounded hover:bg-gray-200 dark:hover:bg-gray-900 flex justify-center items-center flex-col">
      <div className="px-1 pt-2 w-10">
          <img src={fileIconUrl} alt="fileIcon"/>
      </div>
      <span className="text-slate-500 dark:text-slate-400 block w-full px-2 text-sm overflow-x-clip text-ellipsis">{fileName}</span>
      
    </div>
    
  )
}


export default FileView;