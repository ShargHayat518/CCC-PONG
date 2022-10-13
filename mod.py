import pygame
import sys


def ball_animation():

    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball Collision
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(obstacle1):
        if abs(ball.right - obstacle1.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.left - obstacle1.right) < 10:
            print('hitting left')
            ball_speed_x *= -1
        elif abs(ball.bottom - obstacle1.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - obstacle1.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
    if ball.colliderect(obstacle2):
        if abs(ball.right - obstacle2.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.left - obstacle2.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - obstacle2.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - obstacle2.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
    if ball.colliderect(obstacle3):
        if abs(ball.right - obstacle3.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.left - obstacle3.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - obstacle3.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - obstacle3.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
    if ball.colliderect(obstacle4):
        if abs(ball.right - obstacle4.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.left - obstacle4.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - obstacle4.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - obstacle4.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1


def player_animation():

    global player_speed

    player.y += player_speed

    # Player Collision
    if player.top <= 0:
        player.top = 0

    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():

    global opponent_speed

    if opponent.top < ball.top:  # opponent is above ball
        opponent.y += opponent_speed

    if opponent.bottom > ball.bottom:  # opponent is below ball
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0

    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game Rectangle
ball = pygame.Rect(screen_width/2-15, screen_height/2-15, 30, 30)
player = pygame.Rect(screen_width-20, screen_height /
                     2-70, 10, 140)  # -70 missing
opponent = pygame.Rect(10, screen_height/2-70, 10, 140)  # -70 missing

obstacle1 = pygame.Rect(300, 100, 100, 100)
obstacle2 = pygame.Rect(500, 300, 100, 100)
obstacle3 = pygame.Rect(700, 500, 100, 100)
obstacle4 = pygame.Rect(900, 700, 100, 100)


# Colors
light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')

# Game Variables
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7


# Game Loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 6
            if event.key == pygame.K_DOWN:
                player_speed += 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 6
            if event.key == pygame.K_DOWN:
                player_speed -= 6

    ball_animation()
    player_animation()
    opponent_ai()

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,
                                            0), (screen_width/2, screen_height))
    pygame.draw.rect(screen, light_grey, obstacle1)
    pygame.draw.rect(screen, light_grey, obstacle2)
    pygame.draw.rect(screen, light_grey, obstacle3)
    pygame.draw.rect(screen, light_grey, obstacle4)

    pygame.display.flip()
    clock.tick(60)
