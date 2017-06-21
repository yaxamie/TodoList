#!/usr/bin/env python

import argparse
import sys
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

todo_txt_location = os.path.join(__location__, "todo.txt")


def print_file():
    global todo_txt_location

    with open(todo_txt_location, 'r') as _f:
        all_lines = _f.readlines()
        for idx, line in enumerate(all_lines):
            if idx:
                leading_line = "[" + str(idx) + "]"
                print leading_line.ljust(5, ' '), line,
            else:
                print line,


def remove_line(idx):
    global todo_txt_location

    with open(todo_txt_location, 'r+') as _f:
        all_lines = _f.readlines()
        _f.seek(0)
        _f.truncate()

        for _idx, line in enumerate(all_lines):
            if _idx != idx:
                _f.write(line)


def main(args):
    global todo_txt_location

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-a", "--add", help="Add todo item", type=str, default='')
    arg_parser.add_argument("-r", "--remove", help="Remove a todo item by index.", type=int)
    arg_parser.add_argument("-l", "--list", help="List all the items.", action='store_true')

    # print help if no args provided
    if len(sys.argv) == 1:
        arg_parser.print_help()
        sys.exit(1)

    options = arg_parser.parse_args(args)

    if options.add:
        if not os.path.exists(todo_txt_location):
            with open(todo_txt_location, 'w') as create_file:
                create_file.write("Todo List:\n")

        with open(todo_txt_location, 'a') as write_file:
            write_file.write(options.add+"\n")

        print_file()

    if options.remove:
        remove_line(options.remove)
        print_file()

    if options.list:
        print_file()
    pass

if __name__ == "__main__":
    main(sys.argv[1:])
