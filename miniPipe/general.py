import json



def save_json(filepath, data):
    try:
        with open(filepath, 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=True)
    except IOError or FileNotFoundError:
        print('Error writing file %s' % filepath)


def load_json(filepath):
    try:
        with open(filepath) as jsonfile:
            data = json.load(jsonfile)
        return data
    except IOError or FileNotFoundError:
        return None


def set_project(globals):
    '''
        takes in globals dic and configures project form keys
    :param globals:
    :type globals:
    :return:
    :rtype:
    '''

