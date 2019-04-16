import numpy as np
from abc import ABC, abstractmethod
import pandas as pd
import random


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

    def run(self, stat, strat='greedy'):
        stat = self.my_view(stat)
        index = self.stat2index(stat)
        acts = self.act_tab[index]
        if strat == 'greedy':
            act = acts.loc[acts.p == acts.p.max(), ['x', 'y']]
        return act.tolist()

    def explore(self, stat):
        tmp = stat
        x_lim, y_lim = tmp.shape
        x = random.randint(1, x_lim)-1
        y = random.randint(1, y_lim)-1
        return (x, y)

    def feedback(self, fb):
        self.feedback = fb

    def calc_reward(self):
        if self.feedback is 'win':
            return 100
        elif self.feedback is 'lose':
            return -100
        elif self.feedback is None:
            return 0
        elif self.feedback is 'break_role':
            return -100

    def train(self):
        pass


    def set_role(self, role):
        self.role = role
        pass

    def get_opponents(self, opps):
        self.opps = opps

    def stat2index(self, stat):
        if self.stat_mapper is None:
            x, y = stat.shape
            self.stat_mapper = np.random.rand(x, y)
            tmp = pd.DataFrame(self.stat_mapper)
            tmp.to_csv('workspace/data/mapper.csv', index=False)
        return (stat*self.stat_mapper).sum()

    def view(self, index):
        pass

    def my_view(self, stat):
        return stat*self.role

    def opp_view(self, stat):
        return stat*self.opps[0]

    def load_act_tab(self, tab):
        self.act_tab = tab
        self.act_tab = self.act_tab.set_index('index')


if __name__ == '__main__':
    stat_mapper = pd.read_csv('workspace/data/mapper.csv')
    stat_mapper = stat_mapper.values
    rob1 = SimpleRobot(stat_mapper)
