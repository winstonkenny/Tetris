import numpy as np
import random

class Player(object):
    def __init__(self):
        self.score = 0
        self.body = (
            ((1,1,0),(0,1,1)),  #0 z
            ((0,1,1),(1,1,0)),  #1 s
            ((1,1,1,1),),       #2 |
            ((1,1,1),(0,1,0)),  #3 T
            ((1,1,1),(0,0,1)),  #4 -L
            ((1,1,1),(1,0,0)),  #5 L
            ((1,1),(1,1)),      #6 <>
            )
        self.getted_list=[]
        self.size=[0,0]
        self.pos=[0,0]
    
    def set_score(self, score):
        self.score = score
    
    def get_random_list(self):
        body_index = random.randint(0,6)
        array = np.array(self.body[body_index])
        rotation_num = random.randint(0,3)
        for i in range(rotation_num):
            array = np.transpose(array)[::-1]
        self.getted_list = array.tolist()

        if body_index in [0,1,3,4,5]:
            if rotation_num%2==1:
                self.size=[3,2]
            else:
                self.size=[2,3]
        elif body_index == 2:
            if rotation_num%2==1:
                self.size=[4,1]
            else:
                self.size=[1,4]
        else:
            self.size=[2,2]
        self.pos[1] = random.randint(0, 20-self.size[1])
        return self.getted_list
    
    def get_list(self):
        return self.getted_list
    
if __name__ == "__main__":
    a = Player()
    a.get_list()
