#1
import pygame
import datetime
pygame.init()

w = 600
h = 600
screen = pygame.display.set_mode((h,w))
pygame.display.set_caption("Clock")
pygame.display.set_icon(pygame.image.load("images/main-clock.png"))

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

background = pygame.image.load("images/main-clock.png")
right = pygame.image.load("images/right-hand.png")
left = pygame.image.load("images/left-hand.png")

background = pygame.transform.scale(background , (600 , 600))
right = pygame.transform.scale(right , (300 , 300))
left = pygame.transform.scale(left , (300 , 300))
left = pygame.transform.flip(left , 180 , 180)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    sec = datetime.datetime.now().second
    min = datetime.datetime.now().minute
    
    x = (-6*min)%360
    y = ((-1)*sec*6)%360
    
    rot_right , x = rot_center(right , x , 300 , 300)
    rot_left , y = rot_center(left , y , 300 , 300)
    
    screen.blit(background, (0 , 0))
    screen.blit(rot_right , x)
    screen.blit(rot_left , y)
    
    pygame.display.update()


    #2
    import pygame

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1080, 800))
pygame.display.set_caption("Дос-Мұқасан")
pygame.display.set_icon(pygame.image.load('images/1.jpg'))
_songs = [
    'music/Дос–Мукасан тобы - Алматы тунi.mp3',
    'music/Дос–Мукасан тобы - Кайдасын.mp3',
    'music/Дос–Мукасан тобы - Куа Бол.mp3',
    'music/Дос–Мукасан тобы - Куанышым Менин.mp3'
]
covers = [
    pygame.image.load('images/2.jpg'),
    pygame.image.load('images/1.jpg'),
    pygame.image.load('images/3.jpg'),
    pygame.image.load('images/4.jpg')
]

def play_next_song():
    global i 
    i = (i + 1) % len(_songs)
    screen.blit(covers[i], (0, 0))
    pygame.mixer.music.load(_songs[i])
    pygame.mixer.music.play()

def play_previous_song():
    global i 
    i = (i - 1) % len(_songs)
    screen.blit(covers[i], (0, 0))
    pygame.mixer.music.load(_songs[i])
    pygame.mixer.music.play()

done = True
playing = False
i = 0

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RETURN]:
        screen.blit(covers[i], (0, 0))
        pygame.mixer.music.load(_songs[i])
        pygame.mixer.music.play()
    
    if pressed[pygame.K_RIGHT]: 
        play_next_song()
    
    if pressed[pygame.K_LEFT]:
        play_previous_song()
    
    if pressed[pygame.K_SPACE]:
        if playing:
            pygame.mixer.music.pause()
            playing = False
        else:
            pygame.mixer.music.unpause()
            playing = True
    pygame.display.flip()
    clock.tick(15)


#3
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