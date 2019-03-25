import os
import shutil


def create_folder_base():
    """This function have the main goal of create the folder that will be the base folder for this script.
        In case that the base folder isn't empty, all the files/folder will be deleted
    """
    base_folder = r"C:\_TEST_FOLDER"

    if os.path.exists(base_folder):
        check_empty_folder(base_folder)
    else:
        os.mkdir(base_folder)


def check_empty_folder(b_folder):
    if os.listdir(b_folder):
        delete_files(b_folder)
    else:
        delete_folder(b_folder)

    os.mkdir(b_folder)


def delete_files(del_file_folder):
    for the_file in os.listdir(del_file_folder):
        file_path = os.path.join(del_file_folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

    delete_folder(del_file_folder)


def delete_folder(del_folder):
    try:
        shutil.rmtree(del_folder)
    except Exception as os_e:
        print os_e


def create_test_folder():

    create_folder_base()

    base_path = r"C:\_TEST_FOLDER"
    if os.path.isdir(base_path):
        for i in range(1, 11):
            os.mkdir(base_path + r"\Folder" + str(i))


def delete_test_folder():

    if os.listdir(r"C:\_TEST_FOLDER"):
        try:
            shutil.rmtree(r"C:\_TEST_FOLDER")
        except Exception as os_e:
            print os_e
    else:
        print "Empty folder"


if __name__ == "__main__":
    create_test_folder()
