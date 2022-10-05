import pygame
import random
import sys
import colours_module as colours
import variables as v
import score
import pongsounds

# GLOBAL VARIABLES

#pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game Rectangle
buffBall = pygame.Rect(screen_width/2-10, screen_height/2-10, 20, 20)
ball = pygame.Rect(screen_width/2-15, screen_height/2-15, 30, 30)
player = pygame.Rect(screen_width-20, screen_height /
                     2-70, 10, 140)  # -70 missing
opponent = pygame.Rect(10, screen_height/2-70, 10, 140)  # -70 missing


# Game Variables
# ball_speed_x = 7
# ball_speed_y = 7
# player_speed = 0
# opponent_speed = 3

# Score Text
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)

#Randomize buff ball direction when spawned
v.buffBall_speed_y *= random.choice((-1,1))


# FUNCTIONS

def ball_animation():

    global ball_speed_x, ball_speed_y, player_score, opponent_score

    ball.x += v.ball_speed_x
    ball.y += v.ball_speed_y

    # Ball Collision
    if ball.top <= 0 or ball.bottom >= screen_height:
        v.ball_speed_y *= -1

    # Ball Collision Left
    if ball.left <= 0:
        # pygame.mixer.Sound.play(score_sound)
        pongsounds.playScoreSound()
        player_score += 1
        ball_restart()

    # Ball Collision Right
    if ball.right >= screen_width:
        # pygame.mixer.Sound.play(score_sound)
        pongsounds.playScoreSound()
        opponent_score += 1
        ball_restart()

    # Ball Collision (Player)
    if ball.colliderect(player) or ball.colliderect(opponent):
        # pygame.mixer.Sound.play(pong_sound)
        pongsounds.playPongSound()
        v.ball_speed_x *= -1

    if ball.colliderect(buffBall):
        pongsounds.playBuffSound()
        v.ball_speed_x *= -1

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
    buffBall.y += v.buffBall_speed_y

    if buffBall.top <= 0 or buffBall.bottom >= screen_height:
        v.buffBall_speed_y *= -1


def ball_restart():

    global ball_speed_x, ball_speed_y

    ball.center = (screen_width/2, screen_height/2)

    v.ball_speed_y *= random.choice((1, -1))
    v.ball_speed_x *= random.choice((1, -1))


if __name__ == "__main__":

    # GAME LOOP
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    v.player_speed -= 6
                if event.key == pygame.K_DOWN:
                    v.player_speed += 6
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    v.player_speed += 6
                if event.key == pygame.K_DOWN:
                    v.player_speed -= 6

        ball_animation()
        player_animation()
        opponent_ai()
        spawnBuff()

        screen.fill(colours.bg_color)
        pygame.draw.rect(screen, colours.light_grey, player)
        pygame.draw.rect(screen, colours.light_grey, opponent)
        pygame.draw.ellipse(screen, colours.light_grey, ball)
        pygame.draw.aaline(screen, colours.light_grey, (screen_width/2,
                                                        0), (screen_width/2, screen_height))
        pygame.draw.ellipse(screen, 'YELLOW', buffBall)


        # Create a surface for the scores
        score.score(basic_font, player_score,
                    opponent_score, screen)

        pygame.display.flip()
        clock.tick(60)
