import argparse
from gendiff import stylish, plain
from gendiff.gen_diff import generate_diff


def main():
    formatter = {
        'stylish': stylish.stylish,
        'plain': plain.plain
    }
    parser = argparse.ArgumentParser(description='Compares two configuration'
                                                 ' files and'
                                                 ' shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        dest='formatter',
                        default='stylish'
                        )

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file,
                        formatter[args.formatter]))


if __name__ == '__main__':
    main()
