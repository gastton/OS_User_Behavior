import os
import shutil
import random

base_folder = r"C:\_TEST_FOLDER"


def create_base_folder():
    # This function have the main goal of create the folder that will be the base folder for this script.
    # In case that the base folder isn't empty, all the files/folder will be deleted

    if os.path.exists(base_folder):
        try:
            shutil.rmtree(base_folder)
        except Exception as os_e:
            print os_e

    os.mkdir(base_folder)


def verify_base_folder_exist(base_folder):
    return os.path.exists(base_folder)


def create_test_folder():
    # Create 50 folders as part of OS_Behavior

    create_base_folder()

    if os.path.isdir(base_folder):
        tot_folders = random.randint(1, 50)
        for i in range(1, random.randint(1, tot_folders)):
            os.mkdir(base_folder + r"\Folder" + str(i))


def delete_all_test_folder():
    # Delete all folders related to OS_Behavior

    if os.listdir(base_folder):
        try:
            shutil.rmtree(base_folder)
        except Exception as os_e:
            print os_e
    else:
        print "Empty folder"


def delete_n_test_folder(tot_folder):
    print tot_folder
    lst = os.listdir(base_folder)
    for i in range(0, tot_folder):
        shutil.rmtree(base_folder + r"\\" + lst[i])


def copy_test_folder(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    else:
        shutil.rmtree(dst)

    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copy_test_folder(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)


if __name__ == "__main__":
    create_test_folder()
    # delete_all_test_folder()
    # delete_n_test_folder(random.randint(1, len(os.listdir(r"C:\_TEST_FOLDER"))))
    # copy_test_folder(base_folder, tmp_folder)

