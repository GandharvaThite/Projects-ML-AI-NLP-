import math

import pygame
import random
import math as m
pygame.init()
WIDTH,HEIGHT = 1200,700
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Cool!")
FPS = 60
PADDLE_WIDTH,PADDLE_HEIGHT=20,100
BALL_RADIUS = 7
SCORE_FONT = pygame.font.SysFont("comicsans",50)
WINING_SCORE = 10
class Box:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw_it(self,win):
        pygame.draw.rect(win,'BLUE',(self.x,self.y,self.width,self.height))
    def move(self,vel_x,vel_y):
        self.x+=vel_x
        self.y+=vel_y
    def get_loc(self):
        return self.x,self.y
    def move_up(self,target):
        self.y=target
class Sonar:
    def __init__(self,x,y):
        self.x=self.original_x=x
        self.y=self.original_y=y
    def draw(self,win,sx,sy,fx,fy):
        pygame.draw.line(win,'YELLOW',(sx,sy),(fx,fy),1)
        pygame.display.update()
    def move(self,factor_x,factor_y):
        self.x+= 0.1*factor_x
        self.y -= 0.1* factor_y
class Obstacles:
    MAX_VEL = 3

    def __init__(self, x, y, width,height):
        self.x = self.original_X = x
        self.y = self.original_Y = y
        self.width = width
        self.height = height
        self.x_vel = self.MAX_VEL
        self.y_vel = random.randint(1, self.MAX_VEL + 1)

    def draw(self, win):
        pygame.draw.rect(win, 'RED', (self.x, self.y,self.width,self.height))
        # pygame.display.update()


    def move(self):
        self.x -= self.x_vel
        # if self.x<0:
        #     hurdles.pop()
        # self.y += self.y_vel
    def get_loc(self):
        return self.x
    def reset(self):
        self.x = random.randint(120,650)
        self.y = self.y

def draw(win,box,obstacles):
    win.fill('WHITE')
    # pygame.draw.line(WIN, 'WHITE', (0, 350), (WIDTH, 350), 4)
    # box.draw_it(win)
    for obs in obstacles:
        obs.draw(win)
    # rays.draw(win)
    pygame.display.update()
def radar(rays,x,y):
    arr = []
    for i in range(0,91):
        arr.append([ x + (x*0.2 * m.cos(m.radians(i))), y - y*0.2 * m.sin(m.radians(i))])
        rays.draw(WIN, x, y, x + (x *0.2* m.cos(m.radians(i))), y - y *0.2* m.sin(m.radians(i)))
    for i in range(90,-1,-1):
        rays.draw(WIN, x, y, x - (x *0.2* m.cos(m.radians(i))), y - y *0.2* m.sin(m.radians(i)))
        arr.append([x - (x*0.2 * m.cos(m.radians(i))), y - y *0.2* m.sin(m.radians(i))])
    return arr
def collision(obstacle,obs_w,obs_h,ray):
    r = []
    for i in range(len(ray)):
        if(ray[i][0]<=obstacle[0]+obs_w and ray[i][1]<=obstacle[1]+obs_h):
            continue
        else:
            r.append([ray[i][0],ray[i][1]])
    return r
def best_ch(r,xx,yy):
    zz = []
    for i in range(len(r)):
        zz.append((((yy-r[i][1])**2))**0.5)
    mm = zz.index(min(zz))
    return r[mm]

def main():
    global hurdles
    run = True
    clock = pygame.time.Clock()
    box = Box(350,650,20,50)
    rad = random.randint(15,31)
    obstacle1 = Obstacles(120, 500, 600,50)
    obstacle2 = Obstacles(500,200,400,20)
    x, y = box.get_loc()
    x+=10
    rays = Sonar(x,y)
    draw(WIN, box, [obstacle1,obstacle2])
    hurdles = []

    while run:
        clock.tick(FPS/6)
        # pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break
        keys = pygame.key.get_pressed()
        # while(y>0):
        arr = radar(rays,x,y)
        clock.tick(2)
        WIN.fill('WHITE')
        draw(WIN, box, [obstacle1,obstacle2])

        cross = 0
        if(y>500):
            r = collision([120, 500], 480, 50, arr)
            if(len(r)<len(arr)):
                q = best_ch(r,300,550)
                dx,dy  = box.get_loc()
                dx = q[0]-dx
                dy = q[1] - dy+25
                box.move(dx,dy)
                box.draw_it(WIN)
                pygame.display.update()
                x,y= box.get_loc()
                # if y<500:
                #     break
                # print(y)
                # print("--------------------------------------------------")
            else:

                box.move_up(arr[90][1])
                box.draw_it(WIN)
                x,y = box.get_loc()
                pygame.display.update()
            print(x,y)
        else:
            r = collision([500, 200], 400, 20, arr)
            if (len(r) < len(arr)):
                q = best_ch(r, 300, 220)
                dx, dy = box.get_loc()
                dx = q[0] - dx
                dy = q[1] - dy + 25
                box.move(dx, dy)
                box.draw_it(WIN)
                pygame.display.update()
                x, y = box.get_loc()
                # if y<500:
                #     break
                # print(y)
                # print("--------------------------------------------------")
            else:
                box.move_up(arr[90][1])
                box.draw_it(WIN)
                x, y = box.get_loc()
                pygame.display.update()
            print(x,y)




    pygame.quit()


main()
