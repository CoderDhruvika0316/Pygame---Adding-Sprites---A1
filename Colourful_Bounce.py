import pygame 
import random 

pygame.init()

sprite_color_change_event = pygame.USEREVENT + 1
background_color_change_event = pygame.USEREVENT + 2

# Background Colors
pink = pygame.Color("pink")
light_pink = pygame.Color("light pink")
dark_blue = pygame.Color("dark blue")

# Sprite Colors
white = pygame.Color("white")
light_blue = pygame.Color("light blue")
light_green = pygame.Color("light green")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = - self.velocity[0]
            boundary_hit = True

        if self.rect.top <= 0 or self.rect.bottom >= 500:
            self.velocity[1] = - self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_color_change_event)) 
            pygame.event.post(pygame.event.Event(background_color_change_event)) 

    def change_color(self):
        self.image.fill(random.choice([white, light_blue, light_green]))

def background_color():
    global bg_color
    bg_color = random.choice([pink, light_pink, dark_blue])

all_sprites_list = pygame.sprite.Group()

ME = Sprite(white, 40, 50)

ME.rect.x = random.randint(0, 480)
ME.rect.y = random.randint(0, 370)

all_sprites_list.add(ME)

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Colourful Bounce Game")

bg_color = pink
screen.fill(bg_color)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        
        elif event.type == sprite_color_change_event:
            ME.change_color()

        elif event.type == background_color_change_event:
            background_color()

    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(240)

pygame.quit()