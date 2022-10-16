import pygame as pg


class Node:

    
    def __init__(self, row, col,contains):
        self.square = 25
        self.row = row * self.square + self.square//.375
        self.col = col * self.square + self.square//1
        self.contains = contains 


        
        # t = 1 #dot
        # x =0    #wall
        # p = 2   #powerup
        # i =3    #emptyspace
        # w= 4 # door
        # g = 6
    
