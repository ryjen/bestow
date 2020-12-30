from os import path, makedirs, sep

from .util import msg, link_file, copy_file

from .exception import MetaException


class Action(object):

    __file = "file"
    __location = "location"
    __type = "type"
    __type_copy = "copy"
    __type_link = "link"

    def __init__(self, package, values):
        self.package = package
        self.values = values

    def validate(self) -> bool:
        if self.values is None:
            return False
        keys = (Action.__file, Action.__location)
        for key in keys:
            if key not in self.values:
                return False
        return True

    def file(self) -> str:
        if Action.__file not in self.values:
            return None

        value = self.values[Action.__file]

        if path.isabs(value):
            raise MetaException(
                "file {} must be relative to package".format(value))

        return path.join(self.package, value), value

    def location(self) -> str:
        if Action.__location not in self.values:
            return None
        value = self.values[Action.__location]
        if path.isabs(value):
            return value, path.basename(value)
        else:
            return path.join(self.package, value), value

    def on_files(self, mutator):
        fpath, src = self.file()
        if not path.isfile(fpath):
            return
        for lpath, dest in self.location():
            if lpath.endswith(sep):
                makedirs(lpath, exist_ok=True)
                lpath = path.join(lpath, src)
            elif path.isdir(lpath):
                lpath = path.join(lpath, src)
            msg("BESTOW: {} {} -> {}".format(self.type(),
                                             fpath, dest))
            mutator(fpath, lpath)

    def link_files(self):
        self.on_files(link_file)

    def copy_files(self):
        self.on_files(copy_file)

    def type(self):
        if Action.__type not in self.values:
            return Action.__default_type
        return self.values[Action.__type]

    def process(self):

        actions = {
            Action.__type_copy: self.copy_files,
            Action.__type_link: self.link_files
        }

        actions[self.type()]()
