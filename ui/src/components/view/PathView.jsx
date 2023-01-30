import React from "react";

const PathView = ({ path, callback }) => {
  const linux = (path.startsWith("/"));
  let pathStack = [];
  
  if (linux)
    pathStack.push("/")
  return (
    <div className=" flex flex-row w-90 h-full overflow-x-auto scroller-visible whitespace-nowrap ">
      {linux && <button
              className="dark:text-dark-secondary"
              onClick={(e) => callback(pathStack[0])}
            >
              /
            </button>
            
      }
      {path.split("/").map((d, i) => {
        if (d) {
          if (pathStack.length === 0) pathStack.push(d + "/");
          else pathStack.push(pathStack[pathStack.length - 1] + d + "/");
          return (
            <button
              className="dark:text-dark-secondary"
              onClick={(e) => callback(pathStack[i])}
              key={i + d}
            >
              {d + "/"}
            </button>
          );
        } else return ""
      })}
    </div>
  );
};

export default PathView;
