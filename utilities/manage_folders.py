import os
import ConfigParser



global globalPath


def get_config_path():
    p_path = ".."
    os.getcwd()
    os.chdir(p_path)
    return os.getcwd() + r'\config\config_file.txt'


def folder_file_path(f_path):
    config = ConfigParser.RawConfigParser()
    config.read(get_config_path())

    global globalPath

    if f_path == "folder":
        globalPath = config.get('eub-config', 'new_folders_path')
    elif f_path == "file":
        globalPath = config.get('eub-config', 'new_files_path')
    else:
        print "error"

    return globalPath


if __name__ == "__main__":
    print folder_file_path("folder")
