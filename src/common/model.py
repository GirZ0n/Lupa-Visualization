import abc


class Page(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def show(cls):
        raise NotImplementedError
