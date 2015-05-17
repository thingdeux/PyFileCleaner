from math import floor
from os.path import getsize

BYTES_TO_MEGABYTES = 1024 * 1024

def get_total_filesize(filenames):
    total_size = 0
    for filename in filenames:
        total_size = total_size + getsize(filename)

    return total_size / BYTES_TO_MEGABYTES