#!/usr/bin/env python
# coding=utf-8

import datetime
import getpass
import os
import shutil
import time


def move():
    today = datetime.datetime.today()
    prefix = os.path.join('/Users/', getpass.getuser())
    desktop = os.path.join(prefix, 'Desktop/')
    drawer = os.path.join(prefix, 'Documents/Drawer/')
    dst = os.path.join(drawer, today.strftime('%Y%m'))

    if not os.path.exists(dst):
        os.makedirs(dst)
        print("Folder created: %s" % dst)

    files = os.listdir(desktop)

    now = time.time()

    days = 86400 * 7

    for item in files:
        if item.startswith('.') or item.endswith('.icloud'):
            continue

        file = os.path.join(desktop, item)
        accessed = os.path.getatime(file)
        diff = now - accessed
        if diff > days:
            print("Stale File: %s (Last Accessed: %.2f days ago)" % (file, diff / 60 / 60 / 60))
            shutil.move(file, os.path.join(dst, item))
        else:
            print("Fresh File: %s (Last Accessed: %.2f days ago)" % (file, diff / 60 / 60 / 60))


if __name__ == "__main__":
    move()
