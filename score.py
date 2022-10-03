import colours_module


def score(basic_font, player_score, opponent_score, screen):
    player_text = basic_font.render(
        f"{player_score}", False, colours_module.light_grey)
    screen.blit(player_text, (660, 470))

    opponent_text = basic_font.render(
        f"{opponent_score}", False, colours_module.light_grey)
    screen.blit(opponent_text, (600, 470))
