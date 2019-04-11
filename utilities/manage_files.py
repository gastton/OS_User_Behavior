from utilities import manage_folders as m_folder
import random
import os
import shutil

text_file = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
            "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip " \
            "ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu " \
            "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia " \
            "deserunt mollit anim id est laborum. "


def create_test_file():
    if not (m_folder.verify_base_folder_exist(m_folder.base_folder)):
        m_folder.create_base_folder()

    tot_files = random.randint(1, 50)
    print "Created: " + str(tot_files)

    for i in range(0, tot_files):
        name_file = str(random.randint(1, 894))
        f = open(m_folder.base_folder + r"\File" + name_file + ".txt", "w")
        f.write(text_file)
        f.close()


def select_files():
    # This function will be return the amount of files to copy/delete, etc

    os.chdir(m_folder.base_folder)
    path, dirs, total_files = next(os.walk(m_folder.base_folder))
    print "Selected:" + str(len(total_files))
    return total_files


def delete_test_files():
    # Delete random files

    tot_files = select_files()
    print "Delete: " + str(tot_files)
    for i in range(1, random.randint(0, len(tot_files))):
            os.remove(tot_files[i])


def copy_test_files():
    tmp_folder = r'C:\TEMP_FOLDER'
    if os.path.exists(tmp_folder):
        try:
            shutil.rmtree(tmp_folder)
        except Exception as os_e:
            print os_e

    os.mkdir(tmp_folder)

    tot_files = select_files()
    print "Copied: " + str(tot_files)

    for i in range(1, random.randint(1, len(tot_files))):
        shutil.move(tot_files[i], tmp_folder)


if __name__ == "__main__":
    # create_test_file()
    # copy_test_files()
    # delete_test_files()