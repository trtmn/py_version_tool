import json
import os

def read_version(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    else:
        default_version = {"major": 1, "minor": 0, "patch": 0}
        write_version(filename, default_version)
        return default_version

def write_version(filename, version):
    with open(filename, 'w') as file:
        json.dump(version, file, indent=4)

def increment_version(filename, part):
    version = read_version(filename)
    major, minor, patch = version['major'], version['minor'], version['patch']
    if part == 'major':
        major += 1
        minor = 0
        patch = 0
    elif part == 'minor':
        minor += 1
        patch = 0
    elif part == 'patch':
        patch += 1
    version['major'], version['minor'], version['patch'] = major, minor, patch
    write_version(filename, version)
    return f"{major}.{minor}.{patch}"
