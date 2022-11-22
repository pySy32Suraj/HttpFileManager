import React from 'react'

import { FileView, FolderView } from "../index";
import { getFileIcon, getFolderIcon } from '../../util';

const FilesFolderContianer = () => {
    let names = ["suraj", "raj"]
    let files = [];

  for (let i=0; i < 100; i++) {
    files.push("filenamendsghdsogndogb5");
  }
  return (
    <div className='flex gap-x-2 gap-y-2 flex-wrap justify-start items-start w-full h-full '>
    <FileView fileName={"filename-35-dfgoi"} fileIconUrl={getFolderIcon(true)} key={`key-${500}`} />
    {
      files.map((v, i) => (
        <FileView fileName={v} fileIconUrl={getFolderIcon(true)} key={`key-${i}`} />
      ))
    }
  <FileView fileName={"filename-35-dfgoi"} fileIconUrl={getFolderIcon(true)} key={`key-${500}`} />
  </div>
  )
};

export default FilesFolderContianer;