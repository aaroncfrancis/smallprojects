import pygame as pg
import time
import random

pg.init()

dis_w = 800
dis_h = 600

dis = pg.display.set_mode((dis_w, dis_h))

clock = pg.time.Clock()

snake_block = 5
snake_speed = 5

font_style = pg.font.SysFont("arial",20)
score_font = pg.font.SysFont("arial",20)


def your_score(score):
    value = score_font.render("Your score is:" +str(score), True)
    dis.blit(value, [0,0])

def snake(snake_block, snake_list): 
    for x in snake_list: 
        pg.draw.rect(dis, black, [x[0],x[1], snake_block, snake_block])