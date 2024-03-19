import pygame 
pygame.init()
W,H = 800, 600
speed = 20
WHITE =(255,255,255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Red ball")
clock = pygame.time.Clock()
FPS = 60

x = W // 2
y = H //2
speed = 20

while True:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if key[pygame.K_UP]: y -= speed
    elif key[pygame.K_DOWN]: y+= speed
    elif key[pygame.K_RIGHT]: x+= speed
    elif key[pygame.K_LEFT]: x-= speed
    if x > 775: x -=speed
    elif x < 25: x +=speed
    if y > 575: y -= speed
    elif y < 25: y+= speed
    
    
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), 25)
    pygame.display.update()
            
    clock.tick(FPS)