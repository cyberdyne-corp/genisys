import time
from humanfriendly import parse_timespan
from consulregistry import ConsulRegistry
from connector import get_running_resources, scale_service
from intelligency import select_compute_definition


def poll_connectors(config, computes, queue):
    consul = ConsulRegistry(config['consul']['host'],
                            config['consul']['port'])
    consul_services = consul.get_services(config['consul']['service_prefix'])
    queue.put(consul_services)
    poll_interval = parse_timespan(config['connector']['poll_interval'])
    while True:
        services = queue.get()
        queue.put(services)
        for service in services:
            ensure_resources_for_service(consul,
                                         computes, service)
        time.sleep(poll_interval)


def ensure_resources_for_service(consul, computes, service_name):
    required_resources = consul.get_value_for_key('skynet/resources/' +
                                                  service_name)
    if required_resources is not None:
        print('Ensure {} running resources for service {}'.format(
            required_resources, service_name))
        current_resources = get_running_resources_in_computes(computes,
                                                              service_name)
        if current_resources != int(required_resources):
            autoscale_service(computes, service_name, required_resources)


def get_running_resources_in_computes(computes, service_name):
    resources = 0
    for name, definition in computes.items():
        connector_resources = get_running_resources(definition, service_name)
        if connector_resources is not None:
            resources += int(connector_resources)
    return resources


def autoscale_service(computes, service_name, resources):
    compute_definition = select_compute_definition(computes)
    scale_service(compute_definition, service_name, resources)
