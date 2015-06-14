#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import run, get, post, put, abort, request
from connector import upscale_service, downscale_service
import errno


def load_computes_from_file(filename):
    computes = {}
    try:
        exec(compile(open(filename, "rb").read(), filename, 'exec'),
             {},
             computes)
    except OSError as e:
        if e.errno == errno.ENOENT:
            print("No compute definitions file provided.")
        else:
            print("An error occured while trying to read \
                compute definitions file. Aborting.")
            raise
    return computes


@post('/compute')
def create_compute_definition():
    data = request.json
    if not data:
        abort(400, 'No data received')
    try:
        compute_name = data["name"]
        computes[compute_name] = {}
        computes[compute_name]["name"] = compute_name
        computes[compute_name]["connector"] = data["connector"]
    except KeyError:
        abort(400, 'Missing parameters.')


@put('/compute/<compute_name>')
def update_compute_definition(compute_name):
    data = request.json
    if not data:
        abort(400, 'No data received')
    try:
        computes[compute_name] = {}
        computes[compute_name]["name"] = compute_name
        computes[compute_name]["connector"] = data["connector"]
    except KeyError:
        abort(400, 'Missing parameter.')


@get('/compute/<compute_name>')
def retrieve_compute_definition(compute_name):
    try:
        compute_definition = computes[compute_name]
        return compute_definition
    except KeyError:
        abort(501, "Undefined compute: %s." % compute_name)


@post('/service/<service_name>/upscale')
def upscale(service_name):
    data = request.json
    if not data:
        abort(400, 'No data received')
    try:
        compute_name = data["compute"]
    except KeyError:
        abort(400, 'Missing parameters.')
    try:
        compute_definition = computes[compute_name]
    except KeyError:
        abort(501, "Undefined compute: %s." % compute_name)
    upscale_service(service_name, compute_definition)


@post('/service/<service_name>/downscale')
def downscale(service_name):
    data = request.json
    if not data:
        abort(400, 'No data received')
    try:
        compute_name = data["compute"]
    except KeyError:
        abort(400, 'Missing parameters.')
    try:
        compute_definition = computes[compute_name]
    except KeyError:
        abort(501, "Undefined compute: %s." % compute_name)
    downscale_service(service_name, compute_definition)


if __name__ == '__main__':
    computes = load_computes_from_file("computes.py")
    run(host='localhost', port=7001)
