import requests
import json


def scale_service(compute_definition, service_name, resource_number):
    connector_url = ''.join([compute_definition['connector'],
                             '/service/',
                             service_name,
                             '/scale'])
    payload = {"number": resource_number}
    r = requests.post(connector_url, json=payload)
    if r.status_code != 200:
        print("An error occured with service scaling.")
