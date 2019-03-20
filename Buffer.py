import os





"""
import winshell
import os

file_path = r"C:\guru99.txt"
f = open(file_path, "w+")
for i in range(10):
    f.write("This is line %d\r\n" % (i + 1))
f.close()

winshell.delete_file(file_path)

all_deleted_files = list(winshell.recycle_bin())
for i in all_deleted_files:
    print(i)


winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
"""

"""
import ConfigParser
config = ConfigParser.RawConfigParser()
config.read(os.path.join(os.path.dirname(os.path.realpath(__file__))+r"\config", 'config_file.txt'))
v_py=config.get('eub-config','new_folders_path')
print v_py
"""

os.path.join(os.path.dirname(os.path.realpath(__file__))+r"\config", 'config_file.txt')
config.read(configFilePath)