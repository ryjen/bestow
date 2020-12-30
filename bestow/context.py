from os import path, walk
from .meta import Meta


class Context(object):
    def __init__(self, arguments):
        self.packages = [*arguments]
        self.value = ["stow"]

    def option(self, val):
        self.value.append(val)

    def executable(self):
        return self.value

    def process(self):
        for pkg in self.packages:
            self.process_package(pkg)

    def process_package(self, pkg):

        if not path.isdir(pkg):
            return

        for dirpath, dirs, files in walk(pkg):
            for filename in files:
                meta = Meta.load(dirpath, filename)
                if meta is not None:
                    meta.process()
