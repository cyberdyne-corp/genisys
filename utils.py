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
