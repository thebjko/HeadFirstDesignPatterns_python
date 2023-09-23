from abc import ABCMeta, abstractmethod


class Command(metaclas=ABCMeta):
    '''<< interface >>'''
    @abstractmethod
    def execute(self) -> None:
        pass


