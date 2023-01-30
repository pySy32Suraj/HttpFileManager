import React from "react";

import ButtonBack from "../res/icons/button-back.svg";
import ButtonPrivous from "../res/icons/button-privous.svg";
import ButtonNext from "../res/icons/button-next.svg";
import Connected from "../res/icons/connected.svg";
import NotConnected from "../res/icons/not-connected.svg";
import PathView from "./view/PathView";
import Loader from "./Loader";

const Header = ({
  connectionStatus,
  path,
  pathStack,
  pathSetter,
  loaderState,
  onLoaderClick,
  onButtonsClick,
}) => {
  const update_path = (p) => {
    pathStack.pushAndSet(p, pathSetter);
  };


  return (
    <div className="bg-light-primary dark:bg-dark-primary flex flex-row fixed top-0 pt-px z-10  w-full ">
      <div className="flex flex-row gap-2 ml-2 mr-3 ">
        <button onClick={onButtonsClick.privous}>
          <img width="20" src={ButtonPrivous} alt="" />
        </button>
        <button onClick={onButtonsClick.next}>
          <img width="20" src={ButtonNext} alt="" />
        </button>
        <button onClick={onButtonsClick.back}>
          <img width="20" src={ButtonBack} alt="" />
        </button>
      </div>

      <div className="flex h-full flex-row border border-light-secondary dark:border-dark-secondary w-3/5 md:w-4/5 pl-1 pr-1">
        <button
          onClick={(e) => pathStack.pushAndSet(null, pathSetter)}
          className="mr-1 inline-block dark:text-dark-secondary"
        >
          {document.location.hostname}
        </button>
        <span className="mr-2 dark:text-dark-secondary">{">"}</span>

        {path && <PathView path={path} callback={update_path} />}
      </div>
      <Loader loaderState={loaderState} onClick={onLoaderClick} />

      <div className="ml-2 mr-3 mt-1">
        {connectionStatus ? (
          <img width="20" src={Connected} alt="" />
        ) : (
          <img width="20" src={NotConnected} alt="" />
        )}
      </div>
    </div>
  );
};

export default Header;
