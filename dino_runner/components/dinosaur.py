import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING



class Dinosaur(Sprite):
    X_POS = 50
    Y_POS = 300
    JUMP_VEL = 10

    def __init__(self):
        self.dino_run_img = RUNNING
        self.dino_jump_img = JUMPING
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.jump_vel = self.JUMP_VEL
        self.dino_run = True
        self.dino_jump = False
        self.dino_step = 0

    
    def update(self, input):

        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True

        if self.dino_step >= 10 :
            self.dino_step = 0
    
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y ))
    
    def run(self):
        self.image = RUNNING[0] if self.dino_step < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_step += 1

    def jump(self):
        self.image = self.dino_jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 2
            self.jump_vel -= 0.5
        if self.jump_vel <= -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.dino_run = True
            self.jump_vel = self.JUMP_VEL 
        
    