# -*- coding: utf-8 -*-

import time
import os
import glob

def wait_for(url, condition_func):
    """Wait until a function is true and raise an exception if false
    Arguments:
    url (str): url of the actual page
    condition_func (function): wait until this function is true
    """

    start_time = time.time()
    while time.time() < start_time + 60:
        if condition_func():
            return True
        else:
            time.sleep(0.1)
    raise Exception(
        '[Timeout in {}, URL: {} too long to load]'.format(
            condition_func.__name__, url))


def delete_file_line(filenames, lines):
    # delete line[s](str tuple) in filename[s](str tuple)

    for filename in filenames:
        for file in glob.glob(filename):
            file_path = os.path.abspath(file)
            f = open(file_path, "r")
            file_lines = f.readlines()
            f.close()
            f = open(file_path, "w")
            for file_line in file_lines:
                for line in lines:
                    if line not in file_line:
                        f.write(file_line)
            f.close()
