"""Controls processing of package meta data"""
import subprocess
from os import path, walk
from .meta_package import MetaPackage
from .util import generate_transient_for_template


class Controller():
    """Controls the meta data for the stow context"""

    def __init__(self, context):
        self.context = context
        self.packages = {}

    def __load(self, pkg: str):

        if not path.isdir(pkg):
            return

        for dirpath, _, files in walk(pkg):
            for filename in files:
                if filename == MetaPackage.Filename:
                    meta = MetaPackage(dirpath, filename)
                    self.packages[pkg] = meta.load()

    def load(self):
        """Loads the meta data in the packages specified in context"""
        for pkg in self.context.arguments:
            self.__load(pkg)

    def unload(self):
        """Unloads or cleans up any leftover resources"""
        self.packages = {}

    def execute(self):
        """performs configuration actions and calls stow as a subprocess"""
        for i in self.packages:
            for template in self.packages[i].templates():
                generate_transient_for_template(template)

        return subprocess.call(self.context.argv())
