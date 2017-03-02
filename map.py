import pygame
import pytmx
from settings import *

pygame.init()

def load():

    loaded = {}
    loaded["ninjaIdle01"] = pygame.image.load("gameImages\_ninjaIdle\s_ninjaIdle_01.png")
    loaded["ninjaIdle02"] = pygame.image.load("gameImages\_ninjaIdle\s_ninjaIdle_02.png")
    loaded["ninjaIdle03"] = pygame.image.load("gameImages\_ninjaIdle\s_ninjaIdle_03.png")
    loaded["ninjaIdle04"] = pygame.image.load("gameImages\_ninjaIdle\s_ninjaIdle_04.png")
    loaded["ninjaIdle05"] = pygame.image.load("gameImages\_ninjaIdle\s_ninjaIdle_05.png")
    loaded["ninjaIdle06"] = pygame.image.load("gameImages\_ninjaIdle\s_ninjaIdle_06.png")
    loaded["ninjaIdle07"] = pygame.image.load("gameImages\_ninjaIdle\s_ninjaIdle_07.png")
    loaded["ninjaIdle08"] = pygame.image.load("gameImages\_ninjaIdle\s_ninjaIdle_08.png")
    loaded["ninjaIdle09"] = pygame.image.load("gameImages\_ninjaIdle\s_ninjaIdle_09.png")
    loaded["ninjaIdle10"] = pygame.image.load("gameImages\_ninjaIdle\s_ninjaIdle_10.png")
    loaded["ninjaJump01"] = pygame.image.load("gameImages\_ninjaJump\s_ninjaJump_01.png")
    loaded["ninjaJump02"] = pygame.image.load("gameImages\_ninjaJump\s_ninjaJump_02.png")
    loaded["ninjaJump03"] = pygame.image.load("gameImages\_ninjaJump\s_ninjaJump_03.png")
    loaded["ninjaJump04"] = pygame.image.load("gameImages\_ninjaJump\s_ninjaJump_04.png")
    loaded["ninjaJump05"] = pygame.image.load("gameImages\_ninjaJump\s_ninjaJump_05.png")
    loaded["ninjaJump06"] = pygame.image.load("gameImages\_ninjaJump\s_ninjaJump_06.png")
    loaded["ninjaJump07"] = pygame.image.load("gameImages\_ninjaJump\s_ninjaJump_07.png")
    loaded["ninjaJump08"] = pygame.image.load("gameImages\_ninjaJump\s_ninjaJump_08.png")
    loaded["ninjaJump09"] = pygame.image.load("gameImages\_ninjaJump\s_ninjaJump_09.png")
    loaded["ninjaJump10"] = pygame.image.load("gameImages\_ninjaJump\s_ninjaJump_10.png")
    loaded["ninjaRun01"] = pygame.image.load("gameImages\_ninjaRun\s_ninjaRun_01.png")
    loaded["ninjaRun02"] = pygame.image.load("gameImages\_ninjaRun\s_ninjaRun_02.png")
    loaded["ninjaRun03"] = pygame.image.load("gameImages\_ninjaRun\s_ninjaRun_03.png")
    loaded["ninjaRun04"] = pygame.image.load("gameImages\_ninjaRun\s_ninjaRun_04.png")
    loaded["ninjaRun05"] = pygame.image.load("gameImages\_ninjaRun\s_ninjaRun_05.png")
    loaded["ninjaRun06"] = pygame.image.load("gameImages\_ninjaRun\s_ninjaRun_06.png")
    loaded["ninjaRun07"] = pygame.image.load("gameImages\_ninjaRun\s_ninjaRun_07.png")
    loaded["ninjaRun08"] = pygame.image.load("gameImages\_ninjaRun\s_ninjaRun_08.png")
    loaded["ninjaRun09"] = pygame.image.load("gameImages\_ninjaRun\s_ninjaRun_09.png")
    loaded["ninjaRun10"] = pygame.image.load("gameImages\_ninjaRun\s_ninjaRun_10.png")
    loaded["distantCity"] = pygame.image.load("gameImages\other\s_distantCityFIX.png").convert()
    return loaded

class TiledMap():
    def __init__(self):
        self.gameMap = pytmx.load_pygame("CollisionMap.tmx")
        self.mapwidth = self.gameMap.tilewidth * self.gameMap.width
        self.mapheight = self.gameMap.tileheight * self.gameMap.height

    def renderMap(self, surface):
        for layer in self.gameMap.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x,y,gid in layer:
                    tile = self.gameMap.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * self.gameMap.tilewidth, y * self.gameMap.tileheight))

    def make_mapSurface(self):

        mapSurface = pygame.Surface((self.mapwidth, self.mapheight), pygame.SRCALPHA)
        self.renderMap(mapSurface)
        return mapSurface

class MovingTiledMap():
    def __init__(self):
        self.MovingMap = pytmx.load_pygame("MovingMap.tmx")
        self.MovingMapwidth = self.MovingMap.tilewidth * self.MovingMap.width
        self.MovingMapheight = self.MovingMap.tileheight * self.MovingMap.height
        self.yChange = 0

    def renderMovingMap(self, surface, yChange):
        for layer in self.MovingMap.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x,y,gid in layer:
                    tile = self.MovingMap.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * self.MovingMap.tilewidth, y * self.MovingMap.tileheight - yChange))

    def make_MovingMapSurface(self, yChange):

        MovingmapSurface = pygame.Surface((self.MovingMapwidth, self.MovingMapheight), pygame.SRCALPHA)
        self.renderMovingMap(MovingmapSurface, yChange)
        return MovingmapSurface

class Collision(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.groups = SolidGroup
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect = pygame.Rect(x, y, width, height)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.groups = platformGroup
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect = pygame.Rect(x, y, width, height)

class MovingPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.groups = MovingPlatformGroup
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect = pygame.Rect(x, y, width, height)

    def movePlatform(self, constant):
        self.rect.y -= constant

    def updatePlatform(self):
        pass

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.groups = ExitGroup
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect = pygame.Rect(x, y, width, height)

