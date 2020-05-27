from typing import List
from pathlib import Path


class ApplicationData:
    def __init__(self, name: str = '', path: str = '', arguments: List[str] = [], work_dir: str = '', description: str = '', *args, **kwargs):
        self.name = name
        self.path = Path(path)
        self.arguments = arguments
        self.description = description
        if not work_dir or work_dir.isspace():
            self.work_dir = Path.home()
        else:
            self.work_dir = Path(work_dir)

    def as_dict(self):
        return {
            "name": self.name,
            "path": str(self.path),
            "work_dir": str(self.work_dir),
            "arguments": self.arguments,
            "description": self.description
        }

    @staticmethod
    def from_dict(dct):
        name = dct["name"]
        path = str(Path(dct["path"]))
        if not dct["work_dir"] or dct["work_dir"].isspace():
            work_dir = str(Path.home())
        else:
            work_dir = str(Path(dct["work_dir"]))
        arguments = dct["arguments"]
        description = dct["description"]

        return ApplicationData(name, path, arguments, work_dir, description)
        #return ApplicationData(name, path, arguments, work_dir)
