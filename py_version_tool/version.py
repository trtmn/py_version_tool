import json

# Function to check for the presence of version.json and create it with initial values if it doesn't exist
def create_version_file(filename='version.json'):
    try:
        with open(filename, 'r') as file:
            pass  # File already exists
    except FileNotFoundError:
        # Create the file with initial values
        initial_version = {"major": 0, "minor": 0, "patch": 0}
        with open(filename, 'w') as file:
            json.dump(initial_version, file, indent=4)

# Function to read the version information from the JSON file
def read_version(filename='version.json'):
    create_version_file(filename)  # Check and create the file if it doesn't exist

    with open(filename, 'r') as file:
        return json.load(file)

# Function to write the version information to the JSON file
def write_version(data, filename='version.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Function to increment the version components
def increment_version(component):
    data = read_version()  # Read the initial version values

    if component == "major":
        data["major"] += 1
        data["minor"] = 0
        data["patch"] = 0
    elif component == "minor":
        data["minor"] += 1
        data["patch"] = 0
    elif component == "patch":
        data["patch"] += 1

    write_version(data)  # Save the updated version back to the JSON file

# Function to set version based on a version string
def set_version(version_string, filename='version.json'):
    data = read_version(filename)  # Read the initial version values

    major, minor, patch = map(int, version_string.split('.'))
    data["major"] = major
    data["minor"] = minor
    data["patch"] = patch

    write_version(data)  # Save the updated version back to the JSON file

# Usage
# Increment the major version
increment_version("major")

# Set the version based on a version string
version_string = "2.3.1"  # Change this to the desired version string
set_version(version_string)
