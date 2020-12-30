"""A module for configuring files in a package configuration"""
from os import path
from .exception import MetaException


class MetaFile():
    """A file definition in a meta package"""
    __file = "file"
    __location = "location"
    __required_keys = (__file, __location)

    def __init__(self, package, values):
        self.package = package
        self.values = values

    def validate(self) -> bool:
        """validates required keys in data"""
        if self.values is None:
            return False
        for key in MetaFile.__required_keys:
            if key not in self.values:
                return False
        return True

    def file(self) -> str:
        """Returns the source file"""
        if MetaFile.__file not in self.values:
            return None

        value = self.values[MetaFile.__file]

        if path.isabs(value):
            raise MetaException(
                "file {} must be relative to package".format(value))

        return path.join(self.package, value), value

    def location(self) -> str:
        """Returns the intended location of the file"""
        if MetaFile.__location not in self.values:
            return None

        value = self.values[MetaFile.__location]

        if path.isabs(value):
            return value, path.basename(value)

        return path.join(self.package, value), value
