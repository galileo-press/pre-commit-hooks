"""Script to check translation files for fuzzy strings."""

from __future__ import print_function

import argparse
import sys


def check_translations(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    fuzzy_files = []

    for filename in args.filenames:
        with open(filename, 'rb') as f:
            content = f.read()
            if 'fuzzy' in content:
                fuzzy_files.append(filename)
    if fuzzy_files:
        for fuzzy_file in fuzzy_files:
            print('Fuzzy translation found: {}'.format(fuzzy_file))
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(check_translations())
