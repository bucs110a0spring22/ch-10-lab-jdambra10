import pygame
import random
#model
class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file, dmg_img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image

        #get the rectangle for positioning
        
        #set other attributes
        self.name = name
        self.speed = 3
        self.health = 10
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dmgSprite = dmg_img_file
        self.hltSprite = img_file

    #methods to make moving our hero easier
    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed

    def spriteChange(self):
      if(self.health <= 5):
        self.image = pygame.image.load(self.dmgSprite)
      else:
        self.image = pygame.image.load(self.hltSprite)

    def fight(self, opponent):
        d20 = random.randrange(1,20)
        if(d20 == 1):
            self.health -= 2
            self.spriteChange()
            print("attack critically failed! Remaining Health: ", self.health)
            return False
        elif(d20 < 10):
            self.health -= 1
            self.spriteChange()
            print("attack failed! Remaining Health: ", self.health)
            return False
        elif (d20 < 20):
            print("successful attack!")
            return True
        elif (d20 == 20):
          self.health += 1
          self.spriteChange()
          print("critical hit! You abosorbed the enemy's health! Remaining Health: ", self.health)
          return True

