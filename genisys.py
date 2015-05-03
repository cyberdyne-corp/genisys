#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import run, get, post, put, abort, request
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


@post('/datacenter')
def create_datacenter_definition():
    data = request.json
    if not data:
        abort(400, 'No data received')
    try:
        datacenter_name = data["name"]
        datacenters[datacenter_name] = {}
        datacenters[datacenter_name]["name"] = datacenter_name
        datacenters[datacenter_name]["connector"] = data["connector"]
    except KeyError:
        abort(400, 'Missing parameters.')


@put('/datacenter/<datacenter_name>')
def update_datacenter_definition(datacenter_name):
    data = request.json
    if not data:
        abort(400, 'No data received')
    try:
        datacenters[datacenter_name] = {}
        datacenters[datacenter_name]["name"] = datacenter_name
        datacenters[datacenter_name]["connector"] = data["connector"]
    except KeyError:
        abort(400, 'Missing parameter.')


@get('/datacenter/<datacenter_name>')
def retrieve_datacenter_definition(datacenter_name):
    try:
        datacenter_definition = datacenters[datacenter_name]
        return datacenter_definition
    except KeyError:
        abort(501, "Undefined datacenter: %s." % datacenter_name)


if __name__ == '__main__':
    datacenters = load_datacenters_from_file("datacenters.py")
    run(host='localhost', port=7001)
