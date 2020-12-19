#Developed By: Nathan

from random import randint


score = 0
lives = 4

apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")
boots = Actor("boots")

def draw():
    screen.clear()
    screen.draw.text("Score: " + str(score), (50, 50), color = "green", fontsize = 64)
    screen.draw.text("Lives: " + str(lives), (600, 50), color = "red", fontsize = 64)
    apple.draw()
    orange.draw()
    pineapple.draw()
    boots.draw()


def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def place_orange():
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)

def place_pineapple():
    pineapple.x = randint(10, 800)
    pineapple.y = randint(10, 600)

def place_boots():
    boots.x = randint(10, 800)
    boots.y = randint(10, 600)

def on_mouse_down(pos):
    global score
    global lives

    if apple.collidepoint(pos):
        score = score + 1
        print("Good Shot! You Hit An Apple")
        place_apple()
        place_boots()
        return score
    
    elif orange.collidepoint(pos):
        score = score + 1
        print("Good Shot! You Hit An Orange!")
        place_orange()
        place_boots()
        return score
    
    elif pineapple.collidepoint(pos):
        score = score + 1
        print("Good Shot! You Hit A Pineapple")
        place_pineapple()
        place_boots()
        return score

    else:
        lives = lives - 1
        if lives == 0:
            print("You Are Out Of Lives!")
            print("Bye!")
            quit()
        
        else:
            print("You Did Not Hit Any Of The Fruit!")
        return lives

place_apple()
place_orange()
place_pineapple()
place_boots()