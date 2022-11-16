#!/usr/bin/env python3

import argparse
import os
# from sys import stderr
from urllib.parse import urljoin


def git_init_repo(directory=''):
    destination_dir = os.path.join(os.getcwd(), directory)
    print("Destination dir: {}".format(destination_dir))
    os.mkdir(destination_dir)
    os.chdir(destination_dir)
    os.system('git init --bare --shared')


def git_init_local(directory='', remote_path=''):
    destination_dir = os.path.join(os.getcwd(), directory)
    print("Destination dir: {}".format(destination_dir))
    os.mkdir(destination_dir)
    os.chdir(destination_dir)
    os.system('git init --bare --shared')
    origin = urljoin(remote_path, directory)
    os.system('git remote add origin {}'.format(origin))
    os.system('git add .')
    os.system("git commit -m 'Start project'")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Git init helper')
    parser.add_argument('directory', type=str, help='destination directory')
    parser.add_argument(
        '-c',
        type=bool,
        default=False,
        action='store_true',
        dest='client',
        help='Create repository at client side'
    )
    args = parser.parse_args()
    if args.client:
        remote_url = input('Base path on remote (in. e. ssh://login@example.com/your/repo/)')
        git_init_local(args.directory, remote_url)
