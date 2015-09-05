#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
from queue import Queue
from bottle import run, get, post, put, abort, request
from utils import load_computes_from_file, load_configuration
from intelligency import select_compute_definition
from connector import scale_service
from poller import poll_connectors


@get('/compute')
def retrieve_compute_definitions():
    return computes


@post('/compute')
def create_compute_definition():
    data = request.json
    if not data:
        abort(400, 'No data received')
    try:
        compute_name = data['name']
        computes[compute_name] = {}
        computes[compute_name]['name'] = compute_name
        computes[compute_name]['connector'] = data['connector']
    except KeyError:
        abort(400, 'Missing parameters.')


@put('/compute/<compute_name>')
def update_compute_definition(compute_name):
    data = request.json
    if not data:
        abort(400, 'No data received')
    try:
        computes[compute_name] = {}
        computes[compute_name]['name'] = compute_name
        computes[compute_name]['connector'] = data['connector']
    except KeyError:
        abort(400, 'Missing parameter.')


@get('/compute/<compute_name>')
def retrieve_compute_definition(compute_name):
    try:
        compute_definition = computes[compute_name]
        return compute_definition
    except KeyError:
        abort(501, 'Undefined compute: {}.'.format(compute_name))


@post('/service/<service_name>/scale')
def scale(service_name):
    data = request.json
    if not data:
        abort(400, 'No data received')
    try:
        resource_number = data['number']
    except KeyError:
        abort(400, 'Missing parameters.')
    try:
        compute_name = data['compute']
    except KeyError:
        compute_name = None
    try:
        if compute_name is not None:
            compute_definition = computes[compute_name]
        else:
            compute_definition = select_compute_definition(computes)
    except KeyError:
        abort(501, 'Undefined compute: {}.'.format(compute_name))
    services = shared_queue.get()
    services.add(service_name)
    shared_queue.put(services)
    scale_service(compute_definition, service_name, resource_number)


def start_webserver(host, port):
    run(host=host, port=port)


if __name__ == '__main__':
    config = load_configuration('genisys.yml')
    computes = load_computes_from_file(config['genisys']['compute_file'])
    shared_queue = Queue(1)
    try:
        api_thread_args = dict(host=config['genisys']['bind'],
                               port=config['genisys']['port'])
        api_thread = threading.Thread(target=start_webserver,
                                      kwargs=api_thread_args).start()
        poller_thread_args = dict(config=config,
                                  computes=computes,
                                  queue=shared_queue)
        poller_thread = threading.Thread(target=poll_connectors,
                                         kwargs=poller_thread_args).start()
    except Exception:
        print('The application failed to start.')
