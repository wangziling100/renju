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
        self.rob1.set_role(1)
        self.rob2.set_role(-1)
        for i in range(1000):
            self.cnt += 1
            self.turn = self.cnt % 2
            if self.turn == 1:
                pose = self.rob1.run()
                self.set_pose(pose, 1, 'X')
            else:
                pose = self.rob2.run()
                self.set_pose(pose, -1, 'O')
            obey_rule = self.check_rule()
            assert obey_rule, 'someone break the rule'
            self.draw()
            success = self.check_success()
            if success:
                break
            isfull = self.check_full()
            if isfull:
                break

    def get_check_wnd(self):
        x, y = self.pose
        x1 = max(0, x-4)
        y1 = max(0, y-4)
        x2 = min(self.scale-1, x+4)
        y2 = min(self.scale-1, y+4)
        self.check_wnd = self.stat[x1:x2+1, y1:y2+1]
        return self.check_wnd

    def check_success(self):
        check_mat1 = np.ones((1, 5))
        check_mat2 = np.ones((5, 1))
        check_mat3 = np.eye(5)
        check_wnd = self.get_check_wnd()

        length = len(check_wnd)
        for i in range(length-4):
            mat1 = check_wnd[i:i+5, i:i+5]
            mat2 = np.rot90(check_wnd)[i:i+5, i:i+5]
            tmp = np.dot(check_mat1, mat1)
            if -5 in tmp.tolist() or 5 in tmp.tolist():
                return True
            tmp = np.dot(mat1, check_mat2)
            if -5 in tmp.tolist() or 5 in tmp.tolist():
                return True
            tmp = (mat1*check_mat3).sum()
            if tmp == 5 or tmp == -5:
                return True
            tmp = (mat2*check_mat3).sum()
            if tmp == 5 or tmp == -5:
                return True
            i += 1
        return False

    def check_rule(self):
        if self.stat.sum() in [0, 1]:
            return True
        else:
            return False

    def check_full(self):
        if 0 in self.stat.reshape(1, -1).tolist()[0]:
            return True
        else:
            return False

    def set_pose(self, pose, value, signal):
        self.pose = pose
        self.frame[pose] = signal
        assert self.stat[pose] == 0, 'wrong pose is given'
        self.stat[pose] = value


if __name__ == '__main__':
    renju = RenjuPanel(17)
    renju.set_pose((8, 0), -1, 'O')
    renju.set_pose((7, 1), -1, 'O')
    renju.set_pose((6, 2), -1, 'O')
    renju.set_pose((5, 3), -1, 'O')
    renju.set_pose((4, 4), -1, 'O')
    # renju.draw()
    print(renju.check_success())
    #renju.loop()

