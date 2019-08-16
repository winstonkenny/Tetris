import numpy as np
import random
import tkinter as tk
import threading
from tkinter import Canvas, Label, Frame
from player import Player

class MainWorld(object):
    def __init__(self, x1, y1, x2, y2, padding):
        self.player = Player()
        self.padding = padding
        self.window = tk.Tk()
        self.window.title('Teris Game By Tkinter')
        self.window.geometry('%sx%s'
                %(self.padding*4+x1+x2+2,
                    y1+self.padding*2 if y1>y2 else y2 +100))
        self.window.bind("<Key>", self.get_key)
        self.frame_root = Frame(self.window)
        self.frame_left = Frame(self.frame_root)
        self.frame_right = Frame(self.frame_root)
        self.frame_left.pack(side='left')
        self.frame_right.pack(side='top')
        self.frame_root.pack()
        self.canvas_main = Canvas(self.frame_left, 
                width=x1+2*self.padding, 
                height = y1+2*self.padding)
        self.canvas_next = Canvas(self.frame_right, 
                width=x2+2*self.padding, 
                height = y2+2*self.padding)
        self.label_score = Label(self.frame_right, text = '0', 
                                #bg = 'blue', 
                                font = ('Arial', 9), 
                                width = 8, height = 2,
                                )
        self.drew_world(x1, y1, x2, y2, self.padding)
        self.worldmap = []
    
    def drew_world(self, x1, y1, x2, y2, padding):
        self.canvas_main.create_rectangle(padding, padding, 
                                    x1+padding, 
                                    y1+padding, 
                                    width = 0, 
                                    #fill = 'red',
                                    )
        self.canvas_next.create_rectangle(padding, padding, 
                                    x2+padding, 
                                    y2+padding, 
                                    width = 2, 
                                    #fill = 'red',
                                    )
        self.canvas_main.pack()
        self.canvas_next.pack(side='top')
        Label(self.frame_right, text = 'Score:', 
                                #bg = 'green', 
                                font = ('Arial', 9), 
                                width = 8, height = 2,
                                ).pack(side='left')
        self.label_score.pack(side='left')

    def make_world(self, x, y):
        # Make World
        list_world = []
        for i in range(y+2):
            if i==0 or i==y+1:
                a = ''
                for j in range(x+2):
                    a += '1'
                list_world.append(a)
            else:
                a = ''
                for j in range(x+2):
                    if j==0 or j==x+1:
                        a += '1'
                    else:
                        a += '0'
                list_world.append(a)
        return list_world
    
    def drew_block(self, canvas, x, y, size, color, padding):
        canvas.create_rectangle(x+padding,y+padding,
                                        x+size[0]-padding,
                                        y+size[1]-padding,
                                        width = 0,
                                        fill = color,
                                        )

    def drew_main(self, x, y):
        # list_world get ["","",""]
        self.worldmap = np.zeros([y+1,x],int).tolist()
        for i in range(x):
            self.worldmap[y][i]=1
        list_world = self.make_world(x,y)
        for i in range(len(list_world)):
            for j in range(len(list_world[i])):
                if list_world[i][j]=='1':
                    self.drew_block(self.canvas_main, 
                            5+j*20, 5+i*20, (20,20), 'red', 1)
                    pass
                else:
                    self.drew_block(self.canvas_main, 
                            5+j*20, 5+i*20, (20,20), '#D9D9D9', 1)
                    pass

    def drew_next(self):
        self.drew_block(self.canvas_next, 5, 5, (120,120),'#D9D9D9', 0)
        list_player = self.player.get_random_list()
        y=20*(6-self.player.size[0])/2
        x=20*(6-self.player.size[1])/2
        
        for i in range(len(list_player)):
            for j in range(len(list_player[i])):
                if list_player[i][j]==1:
                    self.drew_block(self.canvas_next, 
                            x+5+j*20, y+5+i*20, (20,20), 'blue', 1)
                    pass
                else:
                    self.drew_block(self.canvas_next, 
                            x+5+j*20, y+5+i*20, (20,20),'#D9D9D9', 1)
                    pass
    
    def drew_worldmap(self):
        for i in range(len(self.worldmap)-1):
            for j in range(len(self.worldmap[i])):
                if self.worldmap[i][j]==1:
                    self.drew_block(self.canvas_main, 
                            25+j*20, 25+i*20, (20,20), 'yellow', 1)
                    pass
                else:
                    self.drew_block(self.canvas_main, 
                            25+j*20, 25+i*20, (20,20), '#D9D9D9', 1)
                    pass
        pass

    def run_show(self):
        self.window.mainloop()

    def print_worldmap(self):
        for i in self.worldmap:
            print(i)

    def get_key(self,event):
        # print(event.char,event.keycode)
        self.drew_next()
        #clear map
        for i in range(len(self.worldmap)):
            for j in range(len(self.worldmap[i])):
                self.worldmap[i][j]=0
        newlist = self.player.get_list()
        self.player.pos[0]=11
        self.player.pos[1]=4
        print(self.player.size)
        print(self.player.size)
        for i in range(len(newlist)):
            for j in range(len(newlist[i])):
                self.worldmap[self.player.pos[1]+i][self.player.pos[1]+j]=newlist[i][j]

        self.drew_worldmap()




