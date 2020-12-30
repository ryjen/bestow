"""A module for package meta data"""
from __future__ import annotations
from os import path
from .util import load_yaml
from .meta_file import MetaFile


class MetaPackage:
    """properties and methods of a package meta data"""
    Filename = "bestow.yml"
    __templates = "templates"
    __version = "version"
    __current_version = "0.0.1"

    def __init__(self, dirname, filename=Filename):
        self.package = dirname
        self.filename = filename
        self.filepath = path.join(dirname, filename)
        self.values = None

    def load(self) -> MetaPackage:
        """loads the meta file, processing the templates and targets"""
        self.values = load_yaml(self.filepath)
        return self

    def templates(self):
        """Returns a list of template files"""
        if MetaPackage.__templates not in self.values:
            yield None
        for value in self.values[MetaPackage.__templates]:
            yield MetaFile(self.package, value)
