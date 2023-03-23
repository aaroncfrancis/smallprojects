import pygame as pg
import time
import random

pg.init()

white = (255,255,255)
black = (0,0,0)
blue = (55,150,215)

dis_w = 800
dis_h = 600

dis = pg.display.set_mode((dis_w, dis_h))

clock = pg.time.Clock()

snake_block = 5
snake_speed = 5

font_style = pg.font.SysFont("arial",20)
score_font = pg.font.SysFont("arial",20)


def yourScore(score):
    value = score_font.render("Your score is:" +str(score), True)
    dis.blit(value, [0,0])

def snake(snake_block, snake_list): 
    for x in snake_list: 
        pg.draw.rect(dis,black,[x[0],x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[dis_w/6],dis_h/3)

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_w / 2
    y1 = dis_h / 2

    x1_change = 0 
    y1_change = 0

    snakeList = []
    snakeLength = 1

    bitx = round(random.randrange(0,dis_w - snake_block)/10) * 10
    bity = round(random.randrange(0,dis_w - snake_block)/10) * 10

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press 'C' to Continue or 'Q' to quit")
            yourScore(snakeLength - 1)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pg.K_c:
                        gameLoop()


