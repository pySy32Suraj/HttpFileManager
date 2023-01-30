export class PathStack {
  constructor() {
    this.paths = [];
    this.pathIndex = 0;
  }

  push(path) {
    this.paths.push(path);
    this.pathIndex = this.paths.length - 1;
  }
  pushAndSet(path, pathSetter) {
    this.push(path);
    pathSetter(path);
  }

  getPathNext() {
    if (this.paths.length) {
      if (this.pathIndex < this.paths.length - 1) this.pathIndex += 1;
      let path = this.paths[this.pathIndex];

      return path;
    }
  }
  getPathPrivous() {
    if (this.paths.length) {
      if (this.pathIndex > 0) this.pathIndex -= 1;
      let path = this.paths[this.pathIndex];

      return path;
    }
  }
}
