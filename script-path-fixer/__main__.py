import os
import argparse
import pathlib
import sys


def main():
    args = parse_args(sys.argv[1:])

    interpreter_path = pathlib.Path(args.interpreter)
    script_file = pathlib.Path(args.script)

    script_path = get_script_path(interpreter_path, script_file)

    exit_code = execute_script(script_path, *args.va_list)
    exit(exit_code)


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interpreter', type=str, required=True)
    parser.add_argument('-s', '--script', type=str, required=True)
    parser.add_argument('va_list', nargs='*')
    return parser.parse_args(argv)


def get_script_path(interpreter_path: pathlib.Path, script_file: pathlib.Path):
    path = pathlib.Path()
    path = path / interpreter_path / script_file \
        if is_interpreter_in_scripts_directory(interpreter_path) \
        else path / interpreter_path / 'Scripts' / script_file

    return path


def is_interpreter_in_scripts_directory(interpreter_path: pathlib.Path):
    return interpreter_path.parts[-1] == 'Scripts'


def execute_script(script_path: pathlib.Path, *args):
    assert script_path.is_file(), "Script not found."

    command = '%s %s' % (str(script_path), ' '.join(args))
    return os.system(command)


if __name__ == '__main__':
    main()
