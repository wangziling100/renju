import numpy as np
from abc import ABC, abstractmethod
import pandas as pd


class BaseRobot(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def set_role(self):
        pass

    @abstractmethod
    def stat2index(self, stat):
        pass


class SimpleRobot(BaseRobot):
    def __init__(self, stat_mapper=None):
        self.stat_mapper = stat_mapper
        pass

    def run(self, stat):
        pass

    def set_role(self, role):
        pass

    def stat2index(self, stat):
        if self.stat_mapper is None:
            x, y = stat.shape
            self.stat_mapper = np.random.rand(x, y)
            tmp = pd.DataFrame(self.stat_mapper)
            tmp.to_csv('workspace/data/mapper.csv', index=False)
        return (stat*self.stat_mapper).sum()
        pass


if __name__ == '__main__':
    stat_mapper = pd.read_csv('workspace/data/mapper.csv')
    stat_mapper = stat_mapper.values
    rob1 = SimpleRobot(stat_mapper)
