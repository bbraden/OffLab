import random
from target import targets
import pygame, sys
from pygame.locals import *

target_path = '/Users/braden/vs/graphics/target_adobespark.png'

highscoretxt_path = '/Users/braden/vs/data/highscore.txt'

target1x = 100
target1y = 100

target2x = 100
target2y = 100

target3x = 100
target3y = 100

score = 0

menu = True
game = False

mode = 10

played = 0

ogCounter = 0


def main():
    pygame.init()
    pygame.display.set_caption('offbrand aimlab')

    clock = pygame.time.Clock()

    counter, text = 10, '10'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    DISPLAY = pygame.display.set_mode((500, 400), 0, 32)
    bg = pygame.image.load('graphics/aimlabbg.png').convert()

    WHITE = (255, 255, 255)
    BLUE = (0, 145, 255)
    BLACK = (0, 0, 0)
    DARK_BLUE = (0, 115, 255)
    LIGHT_BLUE = (91, 188, 245)

    # INPUT BOX STUFF
    input_box = pygame.Rect(150, 200, 140, 50)
    color_inactive = pygame.Color(WHITE)
    color_active = pygame.Color(DARK_BLUE)
    color = color_inactive
    active = False
    text = ''
    done = False

    DISPLAY.fill(LIGHT_BLUE)

    pygame.font.init()
    font_path = "/Users/braden/vs/fonts/Quick Zap.ttf"
    font_size = 40
    myfont = pygame.font.Font(font_path, font_size)

    font_path2 = "/Users/braden/vs/fonts/Quick Zap.ttf"
    font_size2 = 35
    myfont2 = pygame.font.Font(font_path2, font_size2)

    def gameTime():
        global menu
        global game
        menu = False
        game = True

    def menuTime():
        global menu
        global game
        game = False
        menu = True

    def getHighScore():
        with open(highscoretxt_path, 'r') as hs:
            return hs.readline()

    def change():
        global x
        global y
        global score
        x = random.randint(1, 400)
        y = random.randint(1, 300)

    def changeargs(a, b):
        a = random.randint(1, 400)
        b = random.randint(1, 300)

    while True:
        global played
        global mode
        global ogCounter
        global target1x
        global target1y
        global target2x
        global target2y
        global target3x
        global target3y

        while menu:

            # quit
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            mode = int(text)
                            counter = int(text)
                            text = ''

                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # go to game
                    if r.collidepoint(m):
                        score = 0
                        try:
                            counter = mode
                            if counter <= 0:
                                counter = 10
                        except ValueError:
                            print('value error - counter == 10')
                            counter = 10
                        if len(str(counter)) >= 4:
                            print('length too long - counter == 10')
                            counter = 10
                        ogCounter = counter
                        gameTime()
            DISPLAY.fill(LIGHT_BLUE)
            # Render the current text.
            txt_surface = myfont.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            # Blit the text.
            DISPLAY.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(DISPLAY, color, input_box, 2)

            highscorelabel = myfont.render(f"High Score: {str(getHighScore())}", 1, DARK_BLUE)

            if played == 0:
                label = myfont2.render("play", 1, BLACK)
                Lpos = (210, 155)
                Rpos = (200, 150, 100, 50)
            if played >= 1:
                label = myfont2.render("play again?", 1, BLACK)
                Lpos = (160, 155)
                Rpos = (150, 150, 225, 50)

            # drawing and bliting everything
            r = pygame.draw.rect(DISPLAY, BLUE, Rpos)

            t = DISPLAY.blit(label, Lpos)
            hsl = DISPLAY.blit(highscorelabel, (10, 10))

            m = pygame.mouse.get_pos()

            # end stuff
            pygame.time.delay(10)
            pygame.display.update()

        while game:

            # quit
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                # countdown
                if event.type == pygame.USEREVENT:
                    counter -= 1
                    text = str(counter).rjust(3) if counter > 0 else '0'

            if counter <= 0:
                played += 1
                if ogCounter <= 10:
                    print('eligible for high score')
                    with open(highscoretxt_path, 'r') as hs:
                        possibleHS = str(score)
                        currentHS = hs.readline()
                        if int(currentHS) < int(possibleHS):
                            with open(highscoretxt_path, 'w') as h:
                                h.write(possibleHS)
                                print(f'new highscore ({possibleHS})')
                if ogCounter > 10:
                    print('not eligible for high score')
                # put go back to main menu here
                menuTime()

            # fills display with light blue
            # DISPLAY.blit(bg, (0, 0))
            DISPLAY.fill(LIGHT_BLUE)

            # score label
            label = myfont.render(f"Score: {str(score)}", 1, DARK_BLUE)

            # drawing and bliting everything
            t = DISPLAY.blit(label, (10, 10))

            allSpritesGroup = pygame.sprite.Group()

            target1 = targets(target_path, target1x, target1y, 50, 50)
            target2 = targets(target_path, target2x, target2y, 50, 50)
            target3 = targets(target_path, target3x, target3y, 50, 50)

            sqSpriteGroup = pygame.sprite.Group()

            sqSpriteGroup.add(target1, target2, target3)
            allSpritesGroup.add(target1, target2, target3)

            # r = pygame.draw.rect(DISPLAY, BLUE, (x, y, 50, 50))
            r = sqSpriteGroup.draw(DISPLAY)

            m = pygame.mouse.get_pos()

            # countdown timer
            c = DISPLAY.blit(myfont.render(text, True, DARK_BLUE), (420, 10))
            pygame.display.flip()
            clock.tick(60)

            # check collisions target 1
            if target1.rect.collidepoint(m):
                score += 1
                target1x = random.randint(1, 400)
                target1y = random.randint(1, 300)

            if target1.rect.colliderect(t):
                target1x = random.randint(1, 400)
                target1y = random.randint(1, 300)

            if target1.rect.colliderect(c):
                target1x = random.randint(1, 400)
                target1y = random.randint(1, 300)

            # check collisions target 2
            if target2.rect.collidepoint(m):
                score += 1
                target2x = random.randint(1, 400)
                target2y = random.randint(1, 300)

            if target2.rect.colliderect(t):
                target2x = random.randint(1, 400)
                target2y = random.randint(1, 300)

            if target2.rect.colliderect(c):
                target2x = random.randint(1, 400)
                target2y = random.randint(1, 300)

            # check collisions target 2
            if target3.rect.collidepoint(m):
                score += 1
                target3x = random.randint(1, 400)
                target3y = random.randint(1, 300)

            if target3.rect.colliderect(t):
                target3x = random.randint(1, 400)
                target3y = random.randint(1, 300)

            if target3.rect.colliderect(c):
                target3x = random.randint(1, 400)
                target3y = random.randint(1, 300)

            # check collisions with each other
            # --------
            # --------
            # --------
            # check collisions target 1

            # end stuff
            pygame.time.delay(10)
            pygame.display.update()


if __name__ == '__main__':
    main()
