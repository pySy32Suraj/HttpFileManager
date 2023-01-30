import React from "react";

const SpaceBar = ({ percent }) => {
  return (
    <div className="w-full h-4 rounded-sm bg-gray-200  pt-px pb-px pl-px pr-px">
      <div
        className="bg-green h-full max-w-full "
        style={{
          width: percent + "%",
        }}
      ></div>
    </div>
  );
};

export default SpaceBar;
