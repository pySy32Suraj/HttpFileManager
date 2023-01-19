import React from 'react'

import FileView from "../view/FileView";
import FolderView from "../view/FolderView";

import { getFileIcon, getFolderIcon } from '../../util';

const FilesFolderContianer = ({folders, files}) => {
  
  
  return (
    <div>FileFolderContainer</div>
  //   <div className='flex gap-x-2 gap-y-2 flex-wrap justify-start items-start w-full h-full '>
  //   <FileView fileName={"filename-35-dfgoi"} fileIconUrl={getFolderIcon(true)} key={`key-${500}`} />
  //   {
  //     files.map((v, i) => (
  //       <FileView fileName={v} fileIconUrl={getFileIcon(v)} key={`key-${i}`} />
  //     ))
  //   }
  // <FileView fileName={"filename-35-dfgoi"} fileIconUrl={getFolderIcon(true)} key={`key-${500}`} />
  // </div>
  )
};

export default FilesFolderContianer;