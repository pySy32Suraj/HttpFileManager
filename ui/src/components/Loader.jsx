import React from "react";

import LoaderIcon from "../res/icons/loader-icon.svg";
const Loader = ({ loaderState, onClick }) => {
  return (
    <button className="ml-2 mr-2" onClick={onClick}>
      <img id={`${loaderState}`} width="15" src={LoaderIcon} alt="" />
    </button>
  );
};

export default Loader;
