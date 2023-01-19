import React from 'react';

const DeviceView = ({deviceName, deviceIconUrl, deviceAddress, onClick}) => {
  return (
    <div
    className=""
    onClick={onClick}
    >

      <div>
        <img src={deviceIconUrl} alt="Profile Pciture" />
      </div>

      <div>
        <h3>{deviceName}</h3>
        <p>{deviceAddress}</p>
      </div>

    </div>
  )
}

export default DeviceView;