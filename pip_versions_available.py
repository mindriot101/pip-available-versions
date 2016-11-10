#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import
import logging
import json
import requests
import argparse
try:
    from typing import IO  # noqa
except ImportError:
    pass

logging.basicConfig(
    level=logging.WARNING, format='%(asctime)s : %(message)s')
logger = logging.getLogger(__name__)


PACKAGE_JSON_URL = 'https://pypi.python.org/pypi/{package}/json'  # type: str

session = requests.Session()  # type: requests.Session


def print_available_versions(package_name, output, json_format=False):
    # type: (str, IO[str], bool) -> None
    response = session.get(PACKAGE_JSON_URL.format(package=package_name))
    response.raise_for_status()
    result_json = response.json()
    versions = sorted(list(result_json['releases'].keys()))

    if json_format:
        payload = {'package': package_name, 'versions': versions}
        json.dump(payload, output, indent=2)
    else:
        for version in versions:
            output.write('{}\n'.format(version))


def main(args):
    # type: (argparse.Namespace) -> None
    if args.verbose:
        logger.setLevel('DEBUG')
    logger.debug('%s', args)

    for package in args.package:
        print_available_versions(
            package, output=args.output, json_format=args.json
        )


def __main__():
    # type: () -> None
    description = '''
    Fetch available versions of a package from pypi
    '''

    epilog = '''
    Output can either be a single list, or json format, to stdout (by default),
    or a file
    '''
    parser = argparse.ArgumentParser(description=description, epilog=epilog)
    parser.add_argument('package', nargs='+')
    parser.add_argument('-o', '--output', type=argparse.FileType(mode='w'),
                        default='-',
                        help='File to write results to (default: stdout)')
    parser.add_argument('-j', '--json', help='Output json format',
                        action='store_true', default=False)
    parser.add_argument('-v', '--verbose', action='store_true')
    main(parser.parse_args())

if __name__ == '__main__':
    __main__()
