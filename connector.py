import requests


def upscale_service(service_name, datacenter_definition):
    connector_url = ''.join([datacenter_definition['connector'],
                             '/service/',
                             service_name,
                             '/start'])
    r = requests.get(connector_url)
    if r.status_code != 200:
        print("An error occured with service upscaling.")


def downscale_service(service_name, datacenter_definition):
    connector_url = ''.join([datacenter_definition['connector'],
                             '/service/',
                             service_name,
                             '/kill'])
    r = requests.get(connector_url)
    if r.status_code != 200:
        print("An error occured with service downscaling.")
