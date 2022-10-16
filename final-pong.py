import pygame
import random
import sys
import colours_module as colours
import variables as v
import score
import pongsounds
import time

# GLOBAL VARIABLES

#pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game Rectangle

buffWall = pygame.Rect(screen_width/2-1, random.randint(0+120, screen_height-120), 2, 120)
ball = pygame.Rect(screen_width/2-15, random.randint(0+30, screen_height-30), 30, 30)

player = pygame.Rect(screen_width-70, screen_height /
                     2-70, 20, 140)
opponent = pygame.Rect(50, screen_height/2-70, 20, 140)
opponent_net = pygame.Rect(0, screen_height/2-70, 20, 250)
player_net = pygame.Rect(screen_width-20, screen_height /
                         2-70, 20, 250)
obstacle1 = pygame.Rect(325, 75, 50, 50)
obstacle2 = pygame.Rect(525, 275, 50, 50)
obstacle3 = pygame.Rect(725, 475, 50, 50)
obstacle4 = pygame.Rect(925, 675, 50, 50)

size_change_powerup = pygame.Rect(random.randint(100, 1180), random.randint(100, 700), 50, 50)

# Score Text
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)

# Randomize buff ball direction when spawned
v.buffWall_speed_y *= random.choice((-1, 1))


def ball_animation():

    global player_score, opponent_score, time_now

    ball.x += v.ball_speed_x
    ball.y += v.ball_speed_y

    # Ball Collision
    if (ball.top <= 0 or ball.bottom >= screen_height) and v.reverse_axis == False:
        v.ball_speed_y *= -1

    elif (ball.top <= 0 or ball.bottom >= screen_height) and v.reverse_axis == True:
        v.ball_speed_y *= -1
        v.ball_speed_x *= -1

    # Ball Collision Left
    if ball.left <= 0:
        v.ball_speed_x *= -1

    # Ball Collision Right
    if ball.right >= screen_width:
        v.ball_speed_x *= -1

    # Ball Collision (Player)
    if ball.colliderect(player):
        pongsounds.playPongSound()
        v.ball_speed_x *= -1

        if v.playerHasBall == False and v.buffAcquired == True:
            v.playerHit = True

        v.buffAcquired = False
        v.playerHasBall = True

    # Ball Collision w/ Powerup (sharg_mod)
    # sharg_mod
    if ball.colliderect(size_change_powerup) and v.powerup_exists:
        pongsounds.playPowerUpSound()
        v.powerup_exists = False
        time_now = time.time()

    if ball.colliderect(opponent):
        pongsounds.playPongSound()
        v.ball_speed_x *= -1

        if v.playerHasBall == True and v.buffAcquired == True:
            v.playerHit = False

        v.buffAcquired = False
        v.playerHasBall = False

    if ball.colliderect(buffWall):
        v.buffAcquired = True
        if v.reverse_axis == False:
            v.reverse_axis = True
        elif v.reverse_axis == True:
            v.reverse_axis = False

    if ball.colliderect(player_net):
        pongsounds.playScoreSound()
        opponent_score += 1
        ball_restart()

    if ball.colliderect(opponent_net):
        pongsounds.playScoreSound()
        player_score += 1
        ball_restart()

    if ball.colliderect(obstacle1):
        if abs(ball.right - obstacle1.left) < 10:
            v.ball_speed_x *= -1
        elif abs(ball.left - obstacle1.right) < 10:
            v.ball_speed_x *= -1
        elif abs(ball.bottom - obstacle1.top) < 10 and v.ball_speed_y > 0:
            v.ball_speed_y *= -1
        elif abs(ball.top - obstacle1.bottom) < 10 and v.ball_speed_y < 0:
            v.ball_speed_y *= -1
    if ball.colliderect(obstacle2):
        if abs(ball.right - obstacle2.left) < 10:
            v.ball_speed_x *= -1
        elif abs(ball.left - obstacle2.right) < 10:
            v.ball_speed_x *= -1
        elif abs(ball.bottom - obstacle2.top) < 10 and v.ball_speed_y > 0:
            v.ball_speed_y *= -1
        elif abs(ball.top - obstacle2.bottom) < 10 and v.ball_speed_y < 0:
            v.ball_speed_y *= -1
    if ball.colliderect(obstacle3):
        if abs(ball.right - obstacle3.left) < 10:
            v.ball_speed_x *= -1
        elif abs(ball.left - obstacle3.right) < 10:
            v.ball_speed_x *= -1
        elif abs(ball.bottom - obstacle3.top) < 10 and v.ball_speed_y > 0:
            v.ball_speed_y *= -1
        elif abs(ball.top - obstacle3.bottom) < 10 and v.ball_speed_y < 0:
            v.ball_speed_y *= -1
    if ball.colliderect(obstacle4):
        if abs(ball.right - obstacle4.left) < 10:
            v.ball_speed_x *= -1
        elif abs(ball.left - obstacle4.right) < 10:
            v.ball_speed_x *= -1
        elif abs(ball.bottom - obstacle4.top) < 10 and v.ball_speed_y > 0:
            v.ball_speed_y *= -1
        elif abs(ball.top - obstacle4.bottom) < 10 and v.ball_speed_y < 0:
            v.ball_speed_y *= -1


def player_animation():

    global player_speed

    player.y += v.player_speed

    # Player Collision
    if player.top <= 0:
        player.top = 0

    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():

    global opponent_speed

    if opponent.top < ball.top:  # opponent is above ball
        opponent.y += v.opponent_speed

    if opponent.bottom > ball.bottom:  # opponent is below ball
        opponent.y -= v.opponent_speed

    if opponent.top <= 0:
        opponent.top = 0

    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def spawnBuff():
    buffWall.y += v.buffWall_speed_y

    if buffWall.top <= 0 or buffWall.bottom >= screen_height:
        v.buffWall_speed_y *= -1


def ball_restart():

    v.playerHasBall = None
    v.buffAcquired = None
    v.playerHit = None

    ball.center = (screen_width/2, screen_height/2)

    v.ball_speed_y *= random.choice((1, -1))
    v.ball_speed_x *= random.choice((1, -1))


def net_animation():
    # Original code
    player_net.y += 10
    opponent_net.y += 10

    # player_net.y += v.player_net_speed_y
    # opponent_net.y += v.opponent_net_speed_y

    # Original Code
    if player_net.bottom >= screen_height:
        player_net.top = 0

    if opponent_net.bottom >= screen_height:
        opponent_net.top = 0

    # if player_net.top <= 0 or player_net.bottom >= screen_height:
    #     v.player_net_speed_y *= -1

    # if opponent_net.top <= 0 or opponent_net.bottom >= screen_height:
    #     v.opponent_net_speed_y *= -1


def obstacle_animation():
    speed = 10

    obstacle1.y += speed
    obstacle2.y += speed
    obstacle3.y -= speed
    obstacle4.y -= speed

    if obstacle1.bottom >= screen_height:
        obstacle1.top = 0
    if obstacle2.bottom >= screen_height:
        obstacle2.top = 0
    if obstacle3.top <= 0:
        obstacle3.bottom = screen_height
    if obstacle4.top <= 0:
        obstacle4.bottom = screen_height

if __name__ == "__main__":

    # GAME LOOP
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (opponent_score - player_score) >= 3:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        v.player_speed -= 10
                    if event.key == pygame.K_DOWN:
                        v.player_speed += 10
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        v.player_speed += 10
                    if event.key == pygame.K_DOWN:
                        v.player_speed -= 10
            elif (player_score - opponent_score) >= 3:
                v.opponent_speed = 10
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        v.player_speed -= 7
                    if event.key == pygame.K_DOWN:
                        v.player_speed += 7
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        v.player_speed += 7
                    if event.key == pygame.K_DOWN:
                        v.player_speed -= 7
            else:
                if event.type == pygame.KEYDOWN:
                    v.opponent_speed = 7
                    if event.key == pygame.K_UP:
                        v.player_speed -= 7
                    if event.key == pygame.K_DOWN:
                        v.player_speed += 7
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        v.player_speed += 7
                    if event.key == pygame.K_DOWN:
                        v.player_speed -= 7

        ball_animation()
        player_animation()
        opponent_ai()
        spawnBuff()
        net_animation()
        obstacle_animation()

        screen.fill(colours.bg_color)

        # This triggers the color splash once the conditions of hitting the buff and if the ball was from player or opponent if the buff is YELLOW
        if v.playerHit == True:
            pygame.draw.rect(screen, (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255)), player)

        else:
            pygame.draw.rect(screen, colours.light_grey, player)

        if v.playerHit == False:
            pygame.draw.rect(screen, (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255)), opponent)

        else:
            pygame.draw.rect(screen, colours.light_grey, opponent)

        # sharg_mod
        if v.powerup_exists:
            pygame.draw.ellipse(screen, colours.powerup_color, size_change_powerup)
        else:
            big_ball_delay = time_now + 1
            end_big_ball = time_now + 10

            if time.time() < big_ball_delay:
                ball = pygame.Rect.inflate(ball, 1, 1)

            if time.time() > end_big_ball:
                ball.height = 30
                ball.width = 30
                
        # This was a test to show color of the buffWall to see if it was completely hit by player or opponent in YELLOW buff
        
        if v.playerHasBall == True and v.buffAcquired == True:
            pygame.draw.rect(screen, 'GREEN', buffWall)
        elif v.playerHasBall == False and v.buffAcquired == True:
            pygame.draw.rect(screen, 'RED', buffWall)
        else:
            pygame.draw.rect(screen, "YELLOW", buffWall)

        pygame.draw.ellipse(screen, colours.light_grey, ball)
        pygame.draw.aaline(screen, colours.light_grey, (screen_width/2,
                                                        0), (screen_width/2, screen_height))

        pygame.draw.rect(screen, "RED", player_net)
        pygame.draw.rect(screen, "RED", opponent_net)

        pygame.draw.rect(screen, colours.light_grey, obstacle1)
        pygame.draw.rect(screen, colours.light_grey, obstacle2)
        pygame.draw.rect(screen, colours.light_grey, obstacle3)
        pygame.draw.rect(screen, colours.light_grey, obstacle4)

        # Create a surface for the scores
        score.score(basic_font, player_score,
                    opponent_score, screen)

        pygame.display.flip()
        clock.tick(60)
