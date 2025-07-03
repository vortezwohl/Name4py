class BaseGenerator(object):
    def __init__(self, names: list):
        self._names = names

    @property
    def names(self) -> list:
        return self._names

    def next_name(self): ...
