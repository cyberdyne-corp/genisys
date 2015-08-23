import requests


def get_value_for_key(consul, key):
    consul_url = ''.join([consul,
                          '/v1/kv/',
                          key,
                          '?raw'])
    request = requests.get(consul_url)
    value = None
    if request.status_code != 200:
        print('Unable to retrieve value for key: {}'.format(key))
    else:
        value = request.text
    return value


def get_services(consul, service_prefix):
    consul_url = ''.join([consul,
                          '/v1/catalog/services'])
    request = requests.get(consul_url)
    if request.status_code != 200:
        print('Failed to retrieve services from Consul.')
    services = []
    result = request.json()
    for service in result:
        if service.startswith(service_prefix):
            services.append(service)
    return services
