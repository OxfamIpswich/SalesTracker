from configparser import ConfigParser
from configparser import SafeConfigParser


def read_config(filename='config.ini', section=''):
    parser = ConfigParser()
    parser.read(filename)

    readitems = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            readitems[item[0]] = item[1]

    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return readitems


