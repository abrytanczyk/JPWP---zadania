import json
from pathlib import Path

from app.model.ApplicationData import ApplicationData

json_data = r'{"name": "App1", "path": "C:\\Windows\\notepad.exe", "arguments": [], "work_dir": "", "description": "super apka"}'

if __name__ == '__main__':
    obj = ApplicationData(**json.loads(json_data))

    assert obj.name == "App1"
    assert str(obj.path) == str(Path(r"C:\Windows\notepad.exe"))
    assert all([i for i, j in zip(obj.arguments, []) if i == j])
    assert str(obj.work_dir) == str(Path.home())
