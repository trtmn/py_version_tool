import json
import os


# Function to create the version.json file with initial values if it doesn't exist
def _create_version_file(filename='version.json'):
    try:
        with open(filename, 'r') as file:
            pass  # File already exists
    except FileNotFoundError:
        # Create the file with initial values
        initial_version = {"major": 0, "minor": 0, "patch": 0}
        with open(filename, 'w') as file:
            json.dump(initial_version, file, indent=4)


# Function to read the version information from the JSON file
def _read_version(filename='version.json'):
    _create_version_file(filename)  # Check and create the file if it doesn't exist

    with open(filename, 'r') as file:
        return json.load(file)


# Function to write the version information to the JSON file and update setup.py
def _write_version(data, setup_py_filename='setup.py', filename='version.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    # Update setup.py with the new version
    update_setup_py_version(setup_py_filename, data)


# Function to convert version dictionary to human-readable format
def version_to_string(version_dict=None):
    if version_dict is None:
        version_dict = _read_version()  # Get the dictionary from _read_version

    return f"{version_dict['major']}.{version_dict['minor']}.{version_dict['patch']}"


# Function to update setup.py with the new version
def update_setup_py_version(setup_py_filename, version_data):
    if not os.path.exists(setup_py_filename):
        # print(f"{setup_py_filename} does not exist.")
        return

    with open(setup_py_filename, 'r') as file:
        setup_py_contents = file.readlines()

    for i, line in enumerate(setup_py_contents):
        if "version=" in line:
            setup_py_contents[i] = f"    version='{version_to_string(version_data)}',\n"
            break

    with open(setup_py_filename, 'w') as file:
        file.writelines(setup_py_contents)


# Function to increment the version components
def increment_version(component):
    data = _read_version()  # Read the initial version values

    if component == "major":
        data["major"] += 1
        data["minor"] = 0
        data["patch"] = 0
    elif component == "minor":
        data["minor"] += 1
        data["patch"] = 0
    elif component == "patch":
        data["patch"] += 1

    _write_version(data)  # Save the updated version back to the JSON file


# Function to set version based on a version string
def set_version(version_string, filename='version.json'):
    data = _read_version(filename)  # Read the initial version values

    major, minor, patch = map(int, version_string.split('.'))
    data["major"] = major
    data["minor"] = minor
    data["patch"] = patch

    _write_version(data)  # Save the updated version back to the JSON file


# Usage
# Increment the major version
increment_version("major")

# Set the version based on a version string
version_string = "2.3.1"  # Change this to the desired version string
set_version(version_string)
