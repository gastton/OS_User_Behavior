import os
import shutil

import ConfigParser


def create_folders():
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
    shutil.rmtree(del_folder)


if __name__ == "__main__":
    create_folders()
