import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle
paddleW = 250
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1
ball_acceleration = 0.05

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

def create_bonus_block():
    x = random.randint(0, W - 100)
    y = random.randint(100, H // 2)
    return pygame.Rect(x, y, 100, 50), (0, 255, 0)

# Block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
unbreakable_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(3, 7) for j in range(2)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in range(10) for j in range(4)]
unbreakable_color_list = [(100, 100, 100) for i in range(12)]

# Game over screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = winfont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    # Drawing blocks
    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]
    [pygame.draw.rect(screen, unbreakable_color_list[color], block) for color, block in enumerate(unbreakable_list)]
    
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    # Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    # Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # Collision blocks
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()
        
    # Collision unbreakable blocks
    unbreakable_hitIndex = ball.collidelist(unbreakable_list)

    if unbreakable_hitIndex != -1:
        dx, dy = detect_collision(dx, dy, ball, unbreakable_list[unbreakable_hitIndex])
        collision_sound.play()

    # Bonus block
    bonus_hitIndex = ball.collidelist(block_list)

    if bonus_hitIndex != -1 and random.randint(1, 10) == 1:
        hitRect = block_list.pop(bonus_hitIndex)
        hitColor = color_list.pop(bonus_hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 2
        collision_sound.play()
        
    # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    # Ball acceleration
    if ballSpeed < 12:
        ballSpeed += ball_acceleration

    # Paddle shrink
    if paddleW > 50:
        paddleW -= 0.01

    # Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)
