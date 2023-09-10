import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("戦士とモンスターのバトルゲーム")

background = pygame.image.load('Halloween.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

warrior = pygame.image.load('yellowman.png')
warrior = pygame.transform.scale(warrior, (50, 50))

monster = pygame.image.load('Flanken.png')
monster = pygame.transform.scale(monster, (50, 50))

player_pos = [WIDTH / 2, HEIGHT - 1.5 * 50]
player_speed = 10

monster_pos = [random.randint(0, WIDTH - 50), 0]
monster_speed = 10

clock = pygame.time.Clock()

avoided_monsters = 0
speed_increase_interval = 5

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed

    monster_pos[1] += monster_speed
    if monster_pos[1] > HEIGHT:
        monster_pos = [random.randint(0, WIDTH - 50), 0]
        avoided_monsters += 1
        if avoided_monsters % speed_increase_interval == 0:
            monster_speed += 2

    win.blit(background, (0, 0))
    win.blit(warrior, (player_pos[0], player_pos[1]))
    win.blit(monster, (monster_pos[0], monster_pos[1]))
    
    pygame.display.update()

    if (monster_pos[1] >= player_pos[1] and monster_pos[1] <= player_pos[1] + 50) and \
       (monster_pos[0] >= player_pos[0] and monster_pos[0] <= player_pos[0] + 50):
        game_over = True
        print("ゲームオーバー！モンスターにやられてしまった...")

    clock.tick(30)

pygame.quit()

