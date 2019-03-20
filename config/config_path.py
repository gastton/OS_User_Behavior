import os


def get_config_path():
    p_path = ".."
    os.getcwd()
    os.chdir(p_path)
    return os.getcwd() + r'\config'
