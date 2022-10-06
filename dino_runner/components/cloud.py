from pygame.sprite import Sprite
import random
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH

class Cloud(Sprite):
    
    def __init__(self):
        self.image = CLOUD
        self.cloud_rect = self.image.get_rect()
        self.cloud_rect.x = SCREEN_WIDTH
        self.cloud_rect.y = 100
    
    def draw(self, screen):
        screen.blit(self.image, (self.cloud_rect.x, self.cloud_rect.y))

    def update(self):
        self.cloud_rect.x -= 10

        if(self.cloud_rect.x < -50):
            self.cloud_rect.x = SCREEN_WIDTH
            self.cloud_rect.y = random.randint(0, 200)

