import requests


def scale_service(compute_definition, service_name, resource_number):
    connector_url = ''.join([compute_definition['connector'],
                             '/service/',
                             service_name,
                             '/scale'])
    payload = {'number': resource_number}
    request = requests.post(connector_url, json=payload)
    if request.status_code != 200:
        print('An error occured with service scaling.')


def get_running_resources(compute_definition, service_name):
    connector_url = ''.join([compute_definition['connector'],
                             '/service/',
                             service_name,
                             '/status'])
    request = requests.get(connector_url)
    if request.status_code != 200:
        print('Unable to retrieve service status on connector.')
        running_resources = None
    else:
        running_resources = request.json()['running_resources']
    return running_resources
