import React from 'react';
import millify from 'millify'

import SpaceBar from '../SpaceBar';
import { getDriveIcon } from '../../util/icons';

const DeviceView = ({device, onClick}) => {
  const units = ["B", "KB", "MB", "GB", "TB"];
  // console.log(device)
  return (
    <div
    className="hover:border  m-3 p-1 h-20 w-4/5  md:w-40  border-light-secondary dark:border-dark-secondary"
    onClick={(e) => onClick(device.mountpoint)}
    >

      <div className='flex'>
        <img width="50" height="50" src={getDriveIcon()} alt="Profile Pciture" />
        <div>
          <h3 className='fg-black dark:text-dark-secondary'>{device.name}</h3>
          <p className='text-xs fg-light-secondary dark:fg-dark-secondary'>{millify(device.details.used, {units})}\{millify(device.details.total, {units})}</p>
        </div>
      </div>

      <div>
        <SpaceBar percent={device.details.percent}/>
      </div>

    </div>
  )
}

export default DeviceView;