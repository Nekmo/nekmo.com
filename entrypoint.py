#!/usr/bin/env python
import sys

import os

import subprocess


COMMIT_FILE = '.last_build_commit'
os.environ.setdefault('BUILD_DJANGO', '1')


def get_current_commit():
    return subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('utf-8').strip()


def read_file():
    if not os.path.lexists(COMMIT_FILE):
        return ''
    with open(COMMIT_FILE, 'r') as f:
        return f.read().strip('\n')


def write_file(data):
    with open(COMMIT_FILE, 'w') as f:
        return f.write(data)


def build_now():
    subprocess.check_call(['make', 'collectstatic'])
    subprocess.check_call(['make', 'migrate'])


def build():
    current_commit = get_current_commit()
    if read_file() != current_commit:
        build_now()
        write_file(current_commit)


def start(*parameters):
    subprocess.check_call(['gunicorn'] + list(parameters))


if __name__ == '__main__':
    if os.environ.get('BUILD_DJANGO') == '1':
        build()
    start(*sys.argv[1:])
