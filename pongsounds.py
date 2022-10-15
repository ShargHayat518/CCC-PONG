import pygame

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)

#Sound Variables
pong_sound = pygame.mixer.Sound("./media/arcadeclicksound.wav")
score_sound = pygame.mixer.Sound("./media/robloxdeathsound.mp3")
buff_sound = pygame.mixer.Sound("./media/tribaldrumsound.wav")
power_up_sound = pygame.mixer.Sound("./media/power_up_sound.wav")

def playPongSound():
    pygame.mixer.Sound.play(pong_sound)


def playScoreSound():
    pygame.mixer.Sound.play(score_sound)


def playBuffSound():
    pygame.mixer.Sound.play(buff_sound)


def playPowerUpSound():
    pygame.mixer.Sound.play(power_up_sound)