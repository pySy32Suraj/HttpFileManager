import React from 'react';

import { getFolderIcon } from '../../util';

const FolderView = ({ folder, onClick }) => {

  return (
    <div
    onClick={(e) => onClick(folder.AbsolutePath)}
    >
      <div className="w-20 rounded hover:bg-gray-200 dark:hover:bg-gray-900 flex justify-center items-center flex-col sticky">
        <div className="px-1 pt-2 w-10">
          <img src={getFolderIcon(folder.Items)} alt="folderIcon" />
        </div>
        <span
          className={`fg-light-secondary dark:fg-dark-secondary w-full px-2 text-sm text-center break-words `}
        >
          {(folder.Name.length <= 20) ? folder.Name: (folder.Name.substring(0, 19) + "...")}
        </span>
      </div>
    </div>
  )
}


export default FolderView;