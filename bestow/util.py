"""A module for miscellaneous utility methods"""
from os import path, sep, makedirs
import sys
import yaml
from .meta_file import MetaFile


def msg(args):
    """Displays a message on stderr"""
    sys.stderr.write(args)
    sys.stderr.write("\n")


def load_yaml(filename: str) -> dict:
    """Returns a dictionary loaded from YAML"""
    with open(filename, "r") as reader:
        return yaml.load(reader, Loader=yaml.FullLoader)


def expand_file(reader, writer):
    """copy open files by line, expanding environment variables"""
    line = reader.readline()
    while line:
        line = path.expandvars(line)
        writer.write(line)
        line = reader.readline()


def generate_file(infile: str, outfile: str) -> int:
    """Writes input to output, expanding environment variables"""
    with open(infile, "r") as reader:
        with open(outfile, "w") as writer:
            return expand_file(reader, writer)


def generate_transient_for_template(template: MetaFile):
    """Writes a template to a transient file from configuration"""
    fpath, src = template.file()
    if not path.isfile(fpath):
        return
    lpath, dest = template.location()
    # if a directory is specified...
    if lpath.endswith(sep):
        # make all directories in the path
        makedirs(lpath, exist_ok=True)
        # and append the file name
        lpath = path.join(lpath, src)
    # or if the path already exists as a directory
    elif path.isdir(lpath):
        # append the file name
        lpath = path.join(lpath, src)
    msg("BESTOW: template {} -> {}".format(fpath, dest))
    # copy the template to the location
    # substituting environment variables
    generate_file(fpath, lpath)
