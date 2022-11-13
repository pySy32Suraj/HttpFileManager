

class PathArgumentParser:

    # path like: /home?value=5&num=5&name=suraj#anchor 
    # define rules for python: /home?int: value&str: name
    def parse(self, path: str) -> dict:
        parsed = {}

        if "?" in path:
            parsed["Path"] = path[: path.find("?")]
            if "#" in path:
                args = path[path.find("?") + 1: path.find("#")]
                anchor = path[path.find("#") + 1: ]
            else:
                args = path[path.find("?") + 1:]
                anchor = ""
            
            parsed["Anchor"] = anchor
            parsed["Arguments"] = self.get_arguments(args)
        else:
            parsed["Path"] = path
            parsed["Arguments"] = None
            parsed["Anchor"] = None
        return parsed

    def type_cast(self, types: tuple, arguments: dict) -> dict:
        args = {}

        for i, item in enumerate(arguments.items()):
            args[item[0]] = types[i](item[1])
        
        return args

    def get_arguments(self, s):
        kw = {}
        for p in s.split("&"):
            k, v = p.split("=")
            kw[k] = v
        return kw
    
    def para_types_class(self, para):
        # str - default, int, float, bool
        classes = []
        for p in para.split("&"):
            if ":" in p:
                t = p.split(":")[0]
                classes.append(eval(f"{t}"))
            else:
                classes.append(str)

        return tuple(classes)

    def split_path_para(self, pathStr):
        if "?" in pathStr:
            path = pathStr[: pathStr.find("?")]
            if "#" in pathStr:
                para = pathStr[pathStr.find("?") + 1: pathStr.find("#")]
            else:
                para = pathStr[pathStr.find("?") + 1: ]
            return path, para
        else:
            return pathStr, None