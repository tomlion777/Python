# Developed By: Nathan John Madukar

from random import randint
from time import sleep


WIDTH = 400
HEIGHT = 400
fox_score = 0
hedgehog_score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100

hedgehog = Actor("hedgehog")
hedgehog.pos = 200, 100

coin = Actor("coin")
coin.pos = 200, 200


def draw(): # draw everything on the screen
    screen.fill("green")
    fox.draw()
    coin.draw()
    hedgehog.draw()
    screen.draw.text("Fox's Score: " + str(fox_score), color = 'black', topleft = (10, 10))
    screen.draw.text("Hedgehog's Score: " + str(hedgehog_score), color = 'black', topleft = (225, 10))

    if game_over: #if the variable game over is True:
        screen.clear()
        screen.fill("red")  
        screen.draw.text("Time's Up! You Had 20 Seconds! ", topleft = (50, 50), fontsize = 30)
        screen.draw.text("Fox's Final Score: " + str(fox_score), topleft = (50, 100), fontsize = 30)
        screen.draw.text("Fox's Coins: " + str(fox_score/10), topleft = (50, 150), fontsize = 30)
        screen.draw.text("Hedgehog's's Final Score: " + str(hedgehog_score), topleft = (50, 200), fontsize = 30)
        screen.draw.text("Hedgehog's Coins: " + str(hedgehog_score/10), topleft = (50, 250), fontsize = 30)


def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))



def time_up():
    global game_over
    game_over = True


def update():

    global fox_score
    global hedgehog_score

    if keyboard.up:
        fox.y = fox.y - 4
    
    elif keyboard.down:
        fox.y = fox.y + 4
    
    elif keyboard.right:
        fox.x = fox.x + 4

    elif keyboard.left:
        fox.x = fox.x - 4

    elif keyboard.w:
        hedgehog.y = hedgehog.y - 4
    
    elif keyboard.s:
        hedgehog.y = hedgehog.y + 4
    
    elif keyboard.d:
        hedgehog.x = hedgehog.x + 4

    elif keyboard.a:
        hedgehog.x = hedgehog.x - 4


    coin_collected_fox = fox.colliderect(coin)
    coin_collected_hedgehog = hedgehog.colliderect(coin)

    if coin_collected_fox: # if the variable coin_collected is True:
        fox_score = fox_score + 10
        place_coin()

    if coin_collected_hedgehog: # if the variable coin_collected is True:
        hedgehog_score = hedgehog_score + 10
        place_coin()
    


clock.schedule(time_up, 20.0)
place_coin()