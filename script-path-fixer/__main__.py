import os
import argparse
import pathlib


def main():
    args = get_args()

    interpreter_path = pathlib.Path(args.interpreter)
    script_file = pathlib.Path(args.script)

    script_path = get_script_path(interpreter_path, script_file)

    exit_code = execute_script(script_path, *args.va_list)
    exit(exit_code)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interpreter', type=str, required=True)
    parser.add_argument('-s', '--script', type=str, required=True)
    parser.add_argument('va_list', nargs='*')
    return parser.parse_args()


def get_script_path(interpreter_path: pathlib.Path, script_file: pathlib.Path):
    path = pathlib.Path()
    path = path / interpreter_path / script_file \
        if is_interpreter_in_scripts(interpreter_path) \
        else path / interpreter_path / 'Scripts' / script_file

    assert path.isfile(), "Script not found."

    return path


def is_interpreter_in_scripts(interpreter_path: pathlib.Path):
    return interpreter_path.parts[-1] == 'Scripts'


def execute_script(script_path: pathlib.Path, *args):
    command = '%s %s' % (str(script_path), ' '.join(args))
    return os.system(command)


if __name__ == '__main__':
    main()
