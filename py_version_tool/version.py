import json
import os
import sys

VERSION_FILENAME = 'version.json'  # Define the filename as a global variable

def read_version():
    if os.path.exists(VERSION_FILENAME):
        with open(VERSION_FILENAME, 'r') as file:
            data = json.load(file)
        return data  # Return the version as a dictionary
    else:
        data = {"major": 0, "minor": 1, "patch": 0}
        write_version(data)
        return data  # Return the default version as a dictionary

def write_version(version):
    with open(VERSION_FILENAME, 'w') as file:
        json.dump(version, file, indent=4)  # Write version as properly formatted JSON

def format_version(version):
    major = str(version['major'])
    minor = str(version['minor'])
    patch = str(version['patch'])
    return f"{major}.{minor}.{patch}"

def increment_version(part):
    version = read_version()  # Get the version as a dictionary
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
    write_version(version)  # Write the updated version as a dictionary
    return format_version(version)  # Format and return the version as a string

def machine_readable_version():
    version = read_version()
    return json.dumps(version, indent=4)  # Return the version as machine-readable JSON

def human_readable_version():
    version = read_version()
    return format_version(version)  # Return the version as X.Y.Z format

def update_setup_py_if_package():
    # Check if the project is a package by examining the presence of an __init__.py file in the current directory
    is_package = os.path.exists('__init__.py')

    if is_package:
        # If the project is a package, update the setup.py file
        try:
            with open('setup.py', 'r') as setup_file:
                setup_code = setup_file.read()

            # Check if the setup.py file contains the correct package name
            package_name = os.path.basename(os.path.abspath(os.path.curdir))
            if package_name != "py_version_tool":
                setup_code = setup_code.replace("name='py_version_tool'", f"name='{package_name}'")

            with open('setup.py', 'w') as setup_file:
                setup_file.write(setup_code)

            print("Updated setup.py for the package.")
        except FileNotFoundError:
            print("setup.py not found. Please make sure it exists in your package directory.")
    else:
        print("The current directory does not appear to be a Python package.")

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'update-setup-py':
            update_setup_py_if_package()
        elif sys.argv[1] == 'machine-readable-version':
            print(machine_readable_version())
        elif sys.argv[1] == 'human-readable-version':
            print(human_readable_version())
    else:
        # Your existing code for reading, writing, and incrementing version numbers
        pass
