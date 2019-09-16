import os
import argparse
import pathlib


def main():
    args = get_args()

    path = pathlib.Path()
    path = path / args.interpreter / args.script \
        if is_interpreter_in_scripts(args.interpreter) \
        else path / args.interpreter / 'Scripts' / args.script

    command = "%s %s" % (str(path), ' '.join(args.va_list))

    exit(os.system(command))


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interpreter', type=str, required=True)
    parser.add_argument('-s', '--script', type=str, required=True)
    parser.add_argument('va_list', nargs='*')
    return parser.parse_args()


def is_interpreter_in_scripts(interpreter_path):
    return os.path.split(interpreter_path)[-1] == 'Scripts'


if __name__ == '__main__':
    main()
