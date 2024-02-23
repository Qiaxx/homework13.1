class ReprMixin:
    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, ", ".join("{}={!r}".format(k, v) for k, v in self.__dict__.items()))