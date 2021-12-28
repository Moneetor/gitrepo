#! python3

import argparse
import os
# from sys import stderr

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Git init helper')
    parser.add_argument('directory', type=str, help='destination directory')
    args = parser.parse_args()
    destinationDir = os.path.join(os.getcwd(), args.directory)
    print("Destination dir: {}".format(destinationDir))
    os.mkdir(destinationDir)
    os.chdir(destinationDir)
    os.system('git init --bare --shared')
