import pygame

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)

#Sound Variables
pong_sound = pygame.mixer.Sound("./media/media_pong.ogg")
score_sound = pygame.mixer.Sound("./media/media_score.ogg")

def playPongSound():
    pygame.mixer.Sound.play(pong_sound)


def playScoreSound():
    pygame.mixer.Sound.play(score_sound)