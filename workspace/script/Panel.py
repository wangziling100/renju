import numpy as np
import os


class RenjuPanel:
    def __init__(self, scale, rob1=None, rob2=None, dist='  '):
        self.scale = scale
        tmp = [0 for i in range(scale*scale)]
        self.stat = np.array(tmp).reshape(scale, scale)
        tmp = ['·' for i in range(scale*scale)]
        self.frame = np.array(tmp).reshape(scale, scale)
        self.dist = dist
        self.pose = (0, 0)
        self.rob1 = rob1
        self.rob2 = rob2
        self.turn = 1
        self.cnt = 0

    def draw(self):
        os.system('clear')
        for i in range(self.scale):
            tmp = self.frame[i].tolist()
            string = self.dist.join(tmp)
            print(string)

    def loop(self):
        for i in range(1000):
            self.cnt += 1
            self.turn = self.cnt % 2
            if self.turn == 1:
                pose = rob1.run()
                self.set_pose(pose, 1, 'X')
            else:
                pose = rob2.run()
                self.set_pose(pose, -1, 'O')
            self.draw()
            self.check_success()

    def check_success(self):
        check_matrix1 = np.ones((5, 5))
        top_left_x = max(0, self.pose[0]-4)
        top_left_y = max(0, self.pose[1]-4)
        bottom_right_x = min(self.scale-1, self.pose[0]+4)
        bottom_right_y = min(self.scale-1, self.pose[1]+4)
        print(top_left_x, top_left_y, bottom_right_x, bottom_right_y)

        pass

    def set_pose(self, pose, value, signal):
        self.pose = pose
        self.frame[pose] = signal
        self.stat[pose] = value


if __name__ == '__main__':
    renju = RenjuPanel(17)
    renju.set_pose((6, 6), -1, 'O')
    renju.draw()
    renju.check_success()
    #renju.loop()


        

