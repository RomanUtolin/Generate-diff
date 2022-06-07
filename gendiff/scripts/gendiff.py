import argparse


parser = argparse.ArgumentParser(prog='gendiff', usage='%(prog)s [options] <filepath1> <filepath1>', description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()
print(args.indir)