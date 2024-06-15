"""
Module Description:
This module implements an endless runner game using Pygame. It includes functionalities for player movement, obstacle generation and collision detection, score tracking, and game speed increase over time.
"""

import pygame
from game_object.player import Player
from game_object.obstacle import add_obstacle
from game_state import game_state
from screen_display import show_start_screen, show_game_over_screen

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coureur - Endless Runner")

road = pygame.image.load('assets/road.png')
background = pygame.image.load('assets/background.png')
screen_img = pygame.image.load('assets/screen.png')
music = pygame.mixer.Sound('assets/music.mp3')
crash_sound = pygame.mixer.Sound('assets/crash.mp3')
music.play(-1)

player = Player()

clock = pygame.time.Clock()
running = True
game_active = False
game_over = False

obstacle_timer = 0
OBSTACLE_INTERVAL = 1000

road_x = 0
background_x = 0

road_speed = 3
background_speed = 1

GAME_SPEED_INCREASE_INTERVAL = 5000
game_speed_increase_timer = 0

font = pygame.font.SysFont(None, 36)

score_time = 0
SCORE_INTERVAL = 100

def check_collision(player):
    """
    Checks for collisions between the player character and obstacles on the screen.
    """
    player_left_collision_point = (player.rect.left, player.rect.bottom)
    player_right_collision_point = (player.rect.right, player.rect.bottom)

    for obstacle in game_state.obstacles:
        obstacle_collision_area = (
            obstacle.rect.left,
            obstacle.rect.right,
            obstacle.rect.bottom - 120 + 4,
            obstacle.rect.bottom + 4
        )

        if ((obstacle_collision_area[0] <= player_left_collision_point[0] <= obstacle_collision_area[1] or
             obstacle_collision_area[0] <= player_right_collision_point[0] <= obstacle_collision_area[1]) and
            obstacle_collision_area[2] <= player_left_collision_point[1] <= obstacle_collision_area[3]):
            return True

    return False

def game_loop():
    """
    Executes the main game loop.

    This function updates the game state, including player movement, obstacle generation, collision detection, score tracking, and rendering of game objects and UI elements.
    It returns False if the game is over due to collision and True otherwise.
    """
    global road_x, background_x, score_time, game_speed_increase_timer, obstacle_timer

    player.update(pygame.key.get_pressed())

    if pygame.time.get_ticks() - obstacle_timer > OBSTACLE_INTERVAL:
        add_obstacle()
        obstacle_timer = pygame.time.get_ticks()

    for obstacle in game_state.obstacles:
        obstacle.update()

    if check_collision(player):
        return False

    road_x -= road_speed
    background_x -= background_speed
    if road_x <= -road.get_width():
        road_x = 0
    if background_x <= -background.get_width():
        background_x = 0

    if pygame.time.get_ticks() - game_speed_increase_timer > GAME_SPEED_INCREASE_INTERVAL:
        game_state.game_speed_rate += 0.1
        game_speed_increase_timer = pygame.time.get_ticks()

    score_time += clock.get_rawtime()

    if score_time >= SCORE_INTERVAL:
        game_state.score += 1
        score_time = 0

    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + background.get_width(), 0))

    screen.blit(road, (road_x, 0))
    screen.blit(road, (road_x + road.get_width(), 0))

    draw_list = [player] + game_state.obstacles
    draw_list.sort(key=lambda obj: obj.rect.bottom)

    for obj in draw_list:
        screen.blit(obj.image, obj.rect)

    text = font.render("Score: " + str(game_state.score), True, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH - 150, 20))

    pygame.display.flip()
    return True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not game_active:
                    game_state.reset()
                    player.rect.center = (360, (240 + 720) // 2)
                    game_active = True
                    game_over = False

    if game_active:
        game_active = game_loop()
        if not game_active:
            game_over = True
            crash_sound.play()
    else:
        if game_over:
            show_game_over_screen(screen, screen_img, font, game_state.score, SCREEN_WIDTH, SCREEN_HEIGHT)
        else:
            show_start_screen(screen, screen_img, font, SCREEN_WIDTH, SCREEN_HEIGHT)

    clock.tick(60)

pygame.mixer.stop()
pygame.quit()
