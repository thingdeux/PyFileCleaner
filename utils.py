from math import floor
from os.path import getsize
from os import walk, stat
from os.path import join

BYTES_TO_MEGABYTES = 1024 * 1024

def get_total_filesize(filenames):
    total_size = 0
    for filename in filenames:
        total_size = total_size + getsize(filename)

    return total_size / BYTES_TO_MEGABYTES


def process_files(folder_root, filenames):
    for filename in filenames:
        all_files.append(join(folder_root, filename))


def discover_folders(folder_root):
    for root, dirs, files in walk(folder_root, followlinks=False):
        process_files(root, files)

        for folder in dirs:
            discover_folders(join(root, folder))