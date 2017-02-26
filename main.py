import pygame
from map import *
from char import *
import time
import pickle

pygame.init()

class game():
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.quitGame = False
        self.gameRunning = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.loadMapData()
        self.preloadedData = load()
        self.camera = Camera(self.map.mapwidth, self.map.mapheight)
        self.frameCount = 1
        self.count = 0
        self.font = pygame.font.SysFont("Arial", 45, bold= True)
        self.takeTextPrev = self.font.render("Wait", True, black)
        self.name = ""
        self.yChange = 0
        self.constant = 3

    def update(self):

        if self.isEnded == True:
            self.gameRunning = False
        self.takeText = self.countFrames()
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.blit(self.preloadedData["distantCity"], (0, 0))
        self.screen.blit(self.map_img, self.camera.applyCameraRect(self.map_rect))
        self.screen.blit(self.MovingMap_img, self.camera.applyCameraRect(self.MovingMap_rect))
        self.camera.updateCamera(player1)
        for sprite in allSprites:
            self.screen.blit(sprite.image, self.camera.applyCamera(sprite))
        if self.takeText != None:
            self.takeText_rect = self.takeText.get_rect()
            self.screen.blit(self.takeText, (self.width/2 - self.takeText_rect.width/2, 30))
            self.takeTextPrev = self.takeText
        else:
            self.takeTextPrev_rect = self.takeTextPrev.get_rect()
            self.screen.blit(self.takeTextPrev, (self.width/2 - self.takeTextPrev_rect.width/2,30))
        pygame.display.update()

    def gameLoop(self):

        self.clock.tick(self.FPS)
        self.loadMovingMapData()
        self.countFrames()
        self.event()
        self.MovingPlatCollision()
        player1.move()
        self.isEnded = player1.ended()
        self.update()



    def countFrames(self):
        if self.frameCount == 12:
            self.frameCount = 1
            self.count += .1
            self.count = round(self.count, 1)
            self.text = self.font.render("Timer: " + str(self.count), True, (0,46,184))
            return self.text
        else:
            self.frameCount += 1


    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quitGame = True

    def loadMapData(self):

        self.map = TiledMap()
        self.map_img = self.map.make_mapSurface()
        self.map_rect = self.map_img.get_rect()
        for tile_object in self.map.gameMap.objects:
            if tile_object.name == "Floor":
                Collision(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == "Collision Box":
                Platform(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == "Exit":
                Exit(tile_object.x, tile_object.y, tile_object.width, tile_object.height)

    def loadMovingMapData(self):
        if self.yChange > 300:
            self.constant = -3
        if self.yChange < 0:
            self.constant = 3
        self.yChange += self.constant

        self.MovingMap = MovingTiledMap()
        self.MovingMap_img = self.MovingMap.make_MovingMapSurface(self.yChange)
        self.MovingMap_rect = self.MovingMap_img.get_rect()
        for tile_object in self.MovingMap.MovingMap.objects:
            if tile_object.name == "Moving Collision Box":
                self.moving_platform = MovingPlatform(tile_object.x, tile_object.y + self.yChange,
                                                      tile_object.width, tile_object.height)

    def MovingPlatCollision(self):
        hitsMoving = pygame.sprite.spritecollide(player1, MovingPlatformGroup, False)
        if hitsMoving:
            print("Collision")

g = game()
player1 = player()
while g.gameRunning == True and g.quitGame == False:
    g.gameLoop()

def enterName(alphabet_running, name, screen):
    while alphabet_running == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and len(name) != 15:
                screen.fill(black)
                g.screen.blit(EndText3, (g.width / 2 - EndText3_rect.width / 2, g.height / 2 -35))

                if event.key == pygame.K_a:
                    stringAddition = "a"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_b:
                    stringAddition = "b"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_c:
                    stringAddition = "c"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_d:
                    stringAddition = "d"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_e:
                    stringAddition = "e"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_f:
                    stringAddition = "f"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_g:
                    stringAddition = "g"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_h:
                    stringAddition = "h"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_i:
                    stringAddition = "i"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_j:
                    stringAddition = "j"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_k:
                    stringAddition = "k"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_l:
                    stringAddition = "l"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_m:
                    stringAddition = "m"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_n:
                    stringAddition = "n"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_o:
                    stringAddition = "o"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_p:
                    stringAddition = "b"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_q:
                    stringAddition = "q"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_r:
                    stringAddition = "r"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_s:
                    stringAddition = "s"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_t:
                    stringAddition = "t"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_u:
                    stringAddition = "u"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_v:
                    stringAddition = "v"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_w:
                    stringAddition = "w"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_x:
                    stringAddition = "x"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_y:
                    stringAddition = "y"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_z:
                    stringAddition = "z"
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

                if event.key == pygame.K_SPACE:
                    stringAddition = " "
                    name = "".join((name, stringAddition))
                    alphabet = font.render(name, True, white)
                    alphabet_rect = alphabet.get_rect()
                    screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                    pygame.display.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(name) != 0:
                        name = list(name)
                        lastChar = len(name) - 1
                        del name[lastChar]
                        name = "".join(name)
                        alphabet = font.render(name, True, white)
                        alphabet_rect = alphabet.get_rect()
                        screen.blit(alphabet, (1280 / 2 - alphabet_rect.width / 2, 720 / 2 + 35))
                        pygame.display.update()

                if event.key == pygame.K_RETURN:
                    alphabet_running = False
                    return name


if g.gameRunning == False:
    font = pygame.font.SysFont("Arial", 70, bold= True)
    EndText = font.render("Gz", True, green)
    EndText2 = font.render("Time: " + str(g.count), True, white)
    g.screen.fill(black)
    EndText_rect = EndText.get_rect()
    EndText2_rect = EndText2.get_rect()
    g.screen.blit(EndText, (g.width/2 - EndText_rect.width/2, g.height/2))
    g.screen.blit(EndText2, (g.width/2 - EndText2_rect.width/2, g.height/2 + 70))
    pygame.display.update()
    time.sleep(2)
    g.screen.fill(black)
    EndText3 = font.render("Enter name", True, white)
    EndText3_rect = EndText3.get_rect()
    g.screen.blit(EndText3, (g.width / 2 - EndText3_rect.width / 2, g.height / 2 - 35))
    pygame.display.update()

    alphabet_running = True
    name = enterName(alphabet_running, g.name, g.screen)

    try:
        openFile = open("times.txt", "rb")
        runTimes = pickle.load(openFile)
        openFile.close()
        runTimes.append([name, g.count])

    except FileNotFoundError:
        runTimes = []
        runTimes.append([name, g.count])
        openFile = open("times.txt", "wb")
        openFile.close()

    if len(runTimes) > 1:
        for i in range(1, len(runTimes)):
            j = i
            while j > 0 and runTimes[j][1] < runTimes[j - 1][1]:
                tempVar = runTimes[j - 1][1]
                runTimes[j - 1][1] = runTimes[j][1]
                runTimes[j][1] = tempVar
                j -= 1

    openFile = open("times.txt", "wb")
    pickle.dump(runTimes, openFile)
    openFile.close()
    time.sleep(3)

    g.screen.fill(black)
    FastestTimes = font.render(runTimes[0][0] + " got the fastest time" , True, white)
    FastestTimes2 = font.render("which was " + str(runTimes[0][1]) + " seconds", True, white)
    FastestTimes_rect = FastestTimes.get_rect()
    FastestTimes2_rect = FastestTimes2.get_rect()
    g.screen.blit(FastestTimes, (g.width / 2 - FastestTimes_rect.width / 2, g.height / 3))
    g.screen.blit(FastestTimes2, (g.width / 2 - FastestTimes2_rect.width / 2, g.height / 2))
    pygame.display.update()
    time.sleep(3)
