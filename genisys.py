#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import run
import errno


def load_datacenters_from_file(filename):
    datacenters = {}
    try:
        exec(compile(open(filename, "rb").read(), filename, 'exec'),
             {},
             datacenters)
    except OSError as e:
        if e.errno == errno.ENOENT:
            print("No datacenters definitions file provided.")
        else:
            print("An error occured while trying to read \
                datacenters definitions file. Aborting.")
            raise
    return datacenters


if __name__ == '__main__':
    datacenters = load_datacenters_from_file("datacenters.py")
    run(host='localhost', port=7001)
