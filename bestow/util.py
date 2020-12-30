from os import path, symlink
import sys
import yaml


def msg(args):
    sys.stderr.write(args)
    sys.stderr.write("\n")


def load_yaml(filename) -> dict:
    with open(filename, "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def copy_open_file(i, o) -> int:
    """ copy open files by line, respecting environment variables"""
    line = i.readline()
    count = 0
    while line:
        count += 1
        line = path.expandvars(line)
        o.write(line)
        line = i.readline()
    return count


def copy_file(i, o) -> int:
    with open(i, "r") as r:
        with open(o, "w") as w:
            return copy_open_file(r, w)


def link_file(r, w):
    symlink(r, w, path.isdir(w))
