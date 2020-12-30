from os import path
from .util import load_yaml
from .action import Action


class Meta(object):
    __meta_file = "bestow.yml"
    __templates = "templates"
    __targets = "targets"
    __version = "version"
    __current_version = "0.0.1"

    def load(dirname, filename):
        if filename == Meta.__meta_file:
            return Meta(dirname, filename)
        else:
            return None

    def __init__(self, dirname, filename=__meta_file):
        self.package = dirname
        self.filename = filename
        self.filepath = path.join(dirname, filename)
        self.values = None

    def validate(self) -> bool:
        keys = (Meta.__templates, Meta.__targets, Meta.__version)
        self.values = load_yaml(self.filepath)
        return all(key in keys for key in self.values)

    def process(self):
        self.values = load_yaml(self.filepath)

        for action in self.templates():
            action.process()

        for action in self.targets():
            action.process()

    def __actions(self, key):
        if key not in self.values:
            yield None
        for action in self.values[key]:
            yield Action(self.package, action)

    def templates(self):
        yield self.__actions(self, Meta.__templates)

    def targets(self):
        yield self.__actions(self, Meta.__targets)
