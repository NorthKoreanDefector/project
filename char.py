import pygame
from settings import *
from map import *

pygame.init()

class player(pygame.sprite.Sprite):
    def __init__(self):
        self.groups = playerGroup, allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.loadedData = load()
        self.image = self.loadedData["ninjaIdle01"]
        self.rect = self.image.get_rect()
        self.rect.center = (1280/2, 720/2)
        self.position = pygame.math.Vector2(640, 360)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.velocity = pygame.math.Vector2(0, 0)
        self.friction = -0.18
        self.falling = False
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.lastUpdate = 0
        self.loadImages()
        self.currentFrame = 0
        self.jumpFrame = 0

    def loadImages(self):
        self.idleImages = []
        self.idleImages.append(self.loadedData["ninjaIdle01"])
        self.idleImages.append(self.loadedData["ninjaIdle02"])
        self.idleImages.append(self.loadedData["ninjaIdle03"])
        self.idleImages.append(self.loadedData["ninjaIdle04"])
        self.idleImages.append(self.loadedData["ninjaIdle05"])
        self.idleImages.append(self.loadedData["ninjaIdle06"])
        self.idleImages.append(self.loadedData["ninjaIdle07"])
        self.idleImages.append(self.loadedData["ninjaIdle08"])
        self.idleImages.append(self.loadedData["ninjaIdle09"])
        self.idleImages.append(self.loadedData["ninjaIdle10"])

        self.walkingRight = []
        self.walkingRight.append(self.loadedData["ninjaRun01"])
        self.walkingRight.append(self.loadedData["ninjaRun02"])
        self.walkingRight.append(self.loadedData["ninjaRun03"])
        self.walkingRight.append(self.loadedData["ninjaRun04"])
        self.walkingRight.append(self.loadedData["ninjaRun05"])
        self.walkingRight.append(self.loadedData["ninjaRun06"])
        self.walkingRight.append(self.loadedData["ninjaRun07"])
        self.walkingRight.append(self.loadedData["ninjaRun08"])
        self.walkingRight.append(self.loadedData["ninjaRun09"])
        self.walkingRight.append(self.loadedData["ninjaRun10"])

        self.walkingLeft = []
        for frame in self.walkingRight:
            self.walkingLeft.append(pygame.transform.flip(frame, True, False))

        self.jumpRight = []
        self.jumpRight.append(self.loadedData["ninjaJump01"])
        self.jumpRight.append(self.loadedData["ninjaJump02"])
        self.jumpRight.append(self.loadedData["ninjaJump03"])
        self.jumpRight.append(self.loadedData["ninjaJump04"])
        self.jumpRight.append(self.loadedData["ninjaJump05"])
        self.jumpRight.append(self.loadedData["ninjaJump06"])
        self.jumpRight.append(self.loadedData["ninjaJump07"])
        self.jumpRight.append(self.loadedData["ninjaJump08"])
        self.jumpRight.append(self.loadedData["ninjaJump09"])
        self.jumpRight.append(self.loadedData["ninjaJump10"])

        self.jumpLeft = []
        for frame in self.jumpRight:
            self.jumpLeft.append(pygame.transform.flip(frame, True, False))

    def checkFalling(self):
        self.rect.y += 1
        if not pygame.sprite.spritecollideany(self, SolidGroup, False) and not (pygame.sprite.spritecollideany(self, platformGroup, False)):
                self.falling = True
                if self.velocity.y < 0:
                    self.up = True
                    self.down = False
                if self.velocity.y > 0:
                    self.up = False
                    self.down = True
        else:
            self.falling = False
            self.up = False
            self.down = False

        self.rect.y -= 1

    def move(self):
        #self.animate()
        self.checkFalling()
        if self.falling:
            self.acceleration = pygame.math.Vector2(0, 0.5)
        if not self.falling:
            self.acceleration = pygame.math.Vector2(0, 0)

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.acceleration.x = 1
            self.right = True
            self.left = False
        if key[pygame.K_LEFT]:
            self.acceleration.x = -1
            self.left = True
            self.right = False
        if key[pygame.K_SPACE]:
            self.jump()

        self.acceleration.x += self.velocity.x * self.friction
        self.velocity += self.acceleration
        if abs(self.velocity.x) < 0.1:
            self.velocity.x = 0
            self.right = False
            self.left = False

        self.position += self.velocity + 0.5 * self.acceleration

        self.rect.midbottom = self.position

        hits = pygame.sprite.spritecollide(self, SolidGroup, False)
        if hits:
            self.position.y = hits[0].rect.top
            self.velocity.y = 0

        hitsPlatform = pygame.sprite.spritecollide(self, platformGroup, False)
        if hitsPlatform:

            if self.up and not (self.left or self.right):
                self.rect.top = hitsPlatform[0].rect.bottom + 1
                self.velocity.y = 0
                print(self.rect.top)
                print(hitsPlatform[0].rect.bottom)

            if self.down and not (self.left or self.right):
                pass

            if self.left and not (self.up or self.down):
                pass

            if self.right and not (self.up or self.down):
                pass

            if self.up and self.left:
                pass

            if self.down and self.left:
                pass

            if self.up and self.right:
                pass

            if self.down and self.right:
                pass

    def ended(self):
        hitsExit = pygame.sprite.spritecollide(self, ExitGroup, False)
        if hitsExit:
            return True
        else:
            return False

    def jump(self):
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, SolidGroup, False)
        hitsPlatform = pygame.sprite.spritecollide(self, platformGroup, False)
        self.rect.y -= 1
        if hits:
            self.velocity.y = -15
        if hitsPlatform:
            self.velocity.y = -15

    def animate(self):
        now = pygame.time.get_ticks()
        if self.velocity.x != 0 and self.velocity.x != 0.5:
            self.walking = True
        else:
            self.walking = False

        if self.up or self.down:
            if now - self.lastUpdate > 100:
                self.lastUpdate = now
                if self.velocity.y != 0:
                    self.jumpFrame = (self.jumpFrame + 1) % len(self.jumpRight)
                bottom = self.rect.bottom
                if self.velocity.x > 0:
                    self.image = self.jumpRight[self.jumpFrame]
                else:
                    self.image = self.jumpLeft[self.jumpFrame]
                    self.rect = self.image.get_rect()
                    self.rect.bottom = bottom
        else:
            self.jumpFrame = 0

        if self.walking and (not self.up and not self.down):
            if now - self.lastUpdate > 50:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame + 1) % len(self.walkingRight)
                bottom = self.rect.bottom
                if self.velocity.x > 0:
                    self.image = self.walkingRight[self.currentFrame]
                else:
                    self.image = self.walkingLeft[self.currentFrame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        if not self.walking and not self.up:
            if now - self.lastUpdate > 100:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame + 1) % len(self.idleImages)
                bottom = self.rect.bottom
                self.image = self.idleImages[self.currentFrame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom


class Camera():
    def __init__(self, width, height):
        self.cameraRect = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def applyCamera(self, entity):
        return entity.rect.move(self.cameraRect.topleft)

    def applyCameraRect(self, rect):
        return rect.move(self.cameraRect.topleft)

    def updateCamera(self, target):
        self.x = -target.rect.x + 640
        self.y = -target.rect.y + 360

        self.x = min(0, self.x)
        self.x = max(-(self.width - 1280), self.x)
        self.y = max(-(self.height - 720), self.y)

        self.cameraRect = pygame.Rect(self.x, self.y, self.width, self.height)
