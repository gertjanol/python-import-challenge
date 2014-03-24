
def check_file():
    return None


if not check_file():
    raise Exception('file not found')


class MyModule(object):

    def my_method(self):
        return 1
