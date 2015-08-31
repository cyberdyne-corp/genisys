import requests
import consul


class ConsulRegistry:

    def __init__(self, host, port):
        self.client = consul.Consul(host=host, port=port)

    def get_value_for_key(self, key):
        index, data = self.client.kv.get(key)
        value = None
        if data is None:
            print('Unable to retrieve value for key: {}'.format(key))
        else:
            value = data["Value"]
        return value

    def get_services(self, service_prefix):
        managed_services = set()
        index, services = self.client.catalog.services()
        for key, value in services.items():
            if key.startswith(service_prefix):
                managed_services.add(key)
        return managed_services
