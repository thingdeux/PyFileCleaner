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


def discover_files(folder_root):
    filenames_to_return = []

    for root, dirs, files in walk(folder_root, followlinks=False):
        for filename in files:
            filenames_to_return.append(join(root, filename))

    return filenames_to_return