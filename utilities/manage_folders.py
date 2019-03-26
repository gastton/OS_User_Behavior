import os
import shutil
import random


def create_base_folder():
    # This function have the main goal of create the folder that will be the base folder for this script.
    # In case that the base folder isn't empty, all the files/folder will be deleted

    base_folder = r"C:\_TEST_FOLDER"

    if os.path.exists(base_folder):
        check_empty_base_folder(base_folder)
    else:
        os.mkdir(base_folder)


def check_empty_base_folder(b_folder):
    # Due to that the base folder exist, here I'll verify if it's empty or not
    # In case that the base folder isn't empty I'll deleted and created again

    if os.listdir(b_folder):
        delete_base_folder(b_folder)

    os.mkdir(b_folder)


def delete_base_folder(del_folder):
    try:
        shutil.rmtree(del_folder)
    except Exception as os_e:
        print os_e


def create_test_folder():
    # Create ten folders as part of OS_Behavior

    create_base_folder()

    base_path = r"C:\_TEST_FOLDER"
    if os.path.isdir(base_path):
        for i in range(1, 11):
            os.mkdir(base_path + r"\Folder" + str(i))


def delete_all_test_folder():
    # Delete all folders related to OS_Behavior

    if os.listdir(r"C:\_TEST_FOLDER"):
        try:
            shutil.rmtree(r"C:\_TEST_FOLDER")
        except Exception as os_e:
            print os_e
    else:
        print "Empty folder"


def delete_n_test_folder(tot_folder):
    print tot_folder
    lst = os.listdir(r"C:\_TEST_FOLDER")
    for i in range(0, tot_folder):
        shutil.rmtree(r"C:\_TEST_FOLDER" + r"\\" + lst[i])


if __name__ == "__main__":
    create_test_folder()
    # delete_all_test_folder()
    delete_n_test_folder(random.randint(1, len(os.listdir(r"C:\_TEST_FOLDER"))))
