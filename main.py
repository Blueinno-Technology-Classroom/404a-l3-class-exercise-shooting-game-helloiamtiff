import pgzrun
import random
import pygame

pygame.mouse.set_visible(False)
                                                                                        

WIDTH = 720
HEIGHT = 480

target1 = Actor("target_red1")
target1.x = WIDTH/2
target1.y = HEIGHT/2
target1.dx = random.randint(1,5)

yellow_duck = Actor("duck_outline_yellow")
yellow_duck.x = random.randint(0, WIDTH)
yellow_duck.top = random.randint(0, HEIGHT-yellow_duck.height) 
yellow_duck.dx = random.randint(1,5)

aim = Actor("crosshair_outline_large")

score = 0
yellow_duck.dx = 100
target1.dx = 10

def update():
   # global dx
    target1.x += target1.dx
    if target1.right >= WIDTH:
        target1.left = 0
        target1.y = random.randint(0,HEIGHT)
    if target1.top <= 0:
        target1.top = 0
    if target1.bottom >= HEIGHT:
        target1.bottom = HEIGHT
   
    yellow_duck.x += yellow_duck.dx
    if yellow_duck.right >= WIDTH:
        yellow_duck.left = 0
        yellow_duck.y = random.randint(0,HEIGHT)
    if yellow_duck.top <= 0:
        yellow_duck.top = 0
    if yellow_duck.bottom >= HEIGHT:
        yellow_duck.bottom = HEIGHT

def on_mouse_move(pos):
    #print(pos)
   aim.pos = pos

def on_mouse_down():
    #print("clicked")
    if aim.colliderect(target1):
        target1.left = 0
        target1.dx += 2
        target1.top =random.randint(0, HEIGHT-target1.height)
        score += 5

    if aim.colliderect(yellow_duck):
        yellow_duck.left = 0
        yellow_duck.dx += 2
        yellow_duck.top =random.randint(0, HEIGHT-yellow_duck.height)
        score += 15

def draw():
    screen.clear()
    target1.draw()
    yellow_duck.draw()
    aim.draw()
    screen.draw.text(str(score), (10,10))

pgzrun.go()