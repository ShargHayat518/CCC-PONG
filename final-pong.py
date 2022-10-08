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


#Select the random buff based on colors (Yellow: Color splash, Purple: Size Debuff) using random.choice
selectedBuffColor = random.choice(v.buffColor)

# Game Rectangle

buffWall = pygame.Rect(screen_width/2-1, random.randint(0+120,screen_height-120), 2, 120)
ball = pygame.Rect(screen_width/2-15, random.randint(0+30,screen_height-30), 30, 30)
player = pygame.Rect(screen_width-30, screen_height /
                     2-70, 20, 140)  # -70 missing
opponent = pygame.Rect(10, screen_height/2-70, 20, 140)  # -70 missing


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
v.buffWall_speed_y *= random.choice((-1,1))


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
        pongsounds.playScoreSound()
        player_score += 1
        ball_restart()

    # Ball Collision Right
    if ball.right >= screen_width:
        pongsounds.playScoreSound()
        opponent_score += 1
        ball_restart()

    # Ball Collision (Player)
    if ball.colliderect(player):
        pongsounds.playPongSound()
        v.ball_speed_x *= -1
        

        if v.playerHasBall == False and v.buffAcquired == True:
            v.playerHit = True

        
        v.buffAcquired = False
        v.playerHasBall = True
        

    if ball.colliderect(opponent):
        pongsounds.playPongSound()
        v.ball_speed_x *= -1
        

        if v.playerHasBall == True and v.buffAcquired == True:
            v.playerHit = False
            
        
        v.buffAcquired = False
        v.playerHasBall = False
        

    if ball.colliderect(buffWall):
        v.buffAcquired = True


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

    global ball_speed_x, ball_speed_y

    v.playerHasBall = None
    v.buffAcquired = None
    v.playerHit = None    

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

        #This triggers the color splash once the conditions of hitting the buff and if the ball was from player or opponent if the buff is YELLOW
        if (selectedBuffColor == "YELLOW"):
            if v.playerHit == True:
                pygame.draw.rect(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)),player, border_radius=15)
            else:
                pygame.draw.rect(screen, colours.light_grey, player, border_radius=15)
    
            if v.playerHit == False:
                pygame.draw.rect(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), opponent, border_radius=15)
            else:
                pygame.draw.rect(screen, colours.light_grey, opponent, border_radius=15)


        pygame.draw.ellipse(screen, colours.light_grey, ball)
        pygame.draw.aaline(screen, colours.light_grey, (screen_width/2,
                                                        0), (screen_width/2, screen_height))
       
       
        #This was a test to show color of the buffWall to see if it was completely hit by player or opponent in YELLOW buff
        if (selectedBuffColor == "YELLOW"):
            if v.playerHasBall == True and v.buffAcquired == True:
                pygame.draw.rect(screen, 'GREEN', buffWall)
            elif v.playerHasBall == False and v.buffAcquired == True:
                pygame.draw.rect(screen, 'RED', buffWall)
            else:
                pygame.draw.rect(screen, selectedBuffColor, buffWall)

        

        # Create a surface for the scores
        score.score(basic_font, player_score,
                    opponent_score, screen)

        pygame.display.flip()
        clock.tick(60)
