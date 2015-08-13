import errno
from yaml import safe_load


def load_computes_from_file(filename):
    computes = {}
    try:
        exec(compile(open(filename, 'rb').read(), filename, 'exec'),
             {},
             computes)
    except OSError as e:
        if e.errno == errno.ENOENT:
            print('No compute definitions file provided.')
        else:
            print('An error occured while trying to read \
                compute definitions file. Aborting.')
            raise
    return computes


def load_configuration(configuration_file):
    with open(configuration_file, 'r') as stream:
        config = safe_load(stream)
        return config
