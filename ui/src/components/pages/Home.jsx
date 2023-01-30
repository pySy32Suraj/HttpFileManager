import React from "react";

import DeviceView from "../view/DeviceView";

const Home = ({ path, devices, onDeviceClick }) => {
  if (path !== null) return;

  if (devices === null) return <h1>Loading...</h1>;
  return (
    <div className="flex flex-col md:flex-row h-full overflow-y-auto">
      {devices.map((e, i) => (
        <DeviceView device={e} onClick={onDeviceClick} key={i + e.name} />
      ))}
    </div>
  );
};

export default Home;
